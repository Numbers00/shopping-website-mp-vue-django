<template>
<div class="container">
  <div class="main-body">
    <!-- Breadcrumb -->
    <nav aria-label="breadcrumb" class="main-breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a @click="$router.push({ name: 'Books' })"
                style="text-decoration: none; color: inherit;">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page">User Profile</li>
      </ol>
    </nav>
    <!-- /Breadcrumb -->
    <div class="row gutters-sm">
      <div class="col-md-4 mb-3">
          <div class="col-12 bg-light border border-light rounded">
              <div class="col-12 bg-light border border-light rounded" style="padding: 20px 10px 20px 10px;">
                  <div class="d-flex flex-column align-items-center text-center">
                      <img src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/profile-icon.png"
                          alt="User" class="rounded-circle" width="150">
                      <div class="mt-3">
                          <h4>{{userDetails[0].full_name}}</h4>
                          <p class="text-secondary mb-1">{{userDetails[0].email}}</p>
                          <p class="text-muted font-size-sm">{{userDetails[0].address}}</p>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-12 bg-light border border-light rounded mt-3">
              <h1 style="text-align: center; padding-top: 20px; font-family: Quicksand;">{{booksPurchased}}
              </h1>
              <h5 style="text-align: center;">Books Purchased</h5>
              <hr>
              <h6 style="text-align: center; text-transform:uppercase; letter-spacing: 2px;">Genre</h6>
              <h3 style="text-align: center; padding-top: 20px; letter-spacing: 3px;">MANGA</h3>
              <br>
          </div>
      </div>
      <div class="col-md-8">
        <div class="col-12 bg-light border border-light rounded mb-3">
          <div class="col-12 bg-light border border-light rounded" style="padding: 20px 10px 20px 10px;">
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Full Name</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails[0].full_name}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Email</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails[0].email}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Phone</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails[0].phone}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <h6 class="mb-0">Address</h6>
              </div>
              <div class="col-sm-9 text-secondary">
                {{userDetails[0].address}}
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-12" style="text-align: left;">
                <a class="btn btn-info " target="__blank"
                    href="https://www.bootdey.com/snippets/view/profile-edit-data-and-skills">Edit</a>
              </div>
            </div>
          </div>
        </div>
        <div class="row gutters-sm">
          <div class="col-sm-8 mb-3">
            <div class="col-12 bg-light border border-light rounded h-100">
              <div class="col-12 bg-light border border-light rounded" style="padding: 20px 10px 20px 10px;">
                <h6 class="d-flex align-items-center mb-3">Previous Orders:</h6>
                <hr>
                <OrderSummary
                    v-for='order in orders'
                    :key='order.id'
                    :order='order'
                />
              </div>
            </div>
          </div>
          <div class="col-sm-4 mb-3" style="max-height: 270px; min-height: 270px; height: 270px;">
            <div class="col-12 bg-light border border-light rounded h-100">
              <div class="col-12 bg-light border border-light rounded"
                style="height: 255px; background: linear-gradient(white, rgb(235, 234, 232)); padding: 20px 10px 20px 10px;">
                <h6 class="d-flex align-items-center mb-3">Quote of the
                  Day</h6>
                <hr>
                <i class="fa fa-quote-left"></i>
                <br>
                If you're the king that rules the court, I'll have to defeat you, and I'll be
                the last one standing.
                <br>
                <i class="fa fa-quote-right" style="float: right;"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'Profile',
    components: {
        OrderSummary
    },
    data () {
        return {
            orders: [],
            userDetails: []
        }
    },
    mounted () {
      document.title = 'Profile | Code & Chill'

      this.getMyOrders()
      this.getMyDetails()
    },
    watch: {
      orders () {
        console.log(this.orders)
      }
    },
    computed: {
      booksPurchased () {
        let numberOfBooks = 0
        for (let order in this.orders) {
          for (let item in this.orders[order].items) {
            numberOfBooks += this.orders[order].items[item].quantity
          }
        }

        return numberOfBooks
      }
    },
    methods: {
        logout () {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders () {
          this.$store.commit('setIsLoading', true)

          await axios
            .get('api/v1/orders/')
            .then(response => {
                this.orders = response.data
            })
            .catch(error => {
                console.log(error)
            })
          
          this.$store.commit('setIsLoading', false)
        },
        async getMyDetails () {
          this.$store.commit('setIsLoading', true)

          await axios
            .get('api/v1/users/')
            .then(response => {
                this.userDetails = response.data
            })
            .catch(error => {
                console.log(error)
            })

          this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>
body {
  background-color: #eeeeee !important;
}
</style>

<style scoped src='@/assets/css/profile.css'></style>
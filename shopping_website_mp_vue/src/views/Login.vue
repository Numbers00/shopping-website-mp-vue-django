<template>
<div>
    <div class="container-fluid">
      <div class="row no-gutter">
        <div class="col-md-6 d-none d-md-flex bg-image"></div>
        <div class="col-md-6" style="background-color: black">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-lg-7 col-xl-6 mx-auto">
                  <h3
                    class="display-4"
                    style="color: white; letter-spacing: 4px"
                  >
                    LOGIN
                  </h3>
                  <br />
                  <form @submit.prevent="submitForm">
                    <div class="form-group mb-3">
                      <input
                        id="inputEmail"
                        type="email"
                        v-model="email"
                        placeholder="Email address"
                        required
                        autofocus=""
                        class="form-control rounded-pill border-0 shadow-sm px-4"
                      />
                    </div>
                    <div class="form-group mb-3">
                      <input
                        id="inputPassword"
                        type="password"
                        v-model="password"
                        placeholder="Password"
                        required
                        class="form-control rounded-pill border-0 shadow-sm px-4 text-danger"
                      /><br />
                    </div>
                    <button
                      type="submit"
                      class="btn btn-danger btn-block text-uppercase mb-2 rounded-pill shadow-sm"
                    >
                      Sign in
                    </button>
                    <div style="padding-top: 10px">
                      <p class="signup">
                        <a @click="$router.push({ name: 'Signup' })" style="text-decoration: none"
                          >New User? Register here!</a
                        >
                      </p>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div
            class="row px-3 text-center justify-content-center mb-0 social"
            style="padding-top: 70px; transform: translateY(-150px)"
          >
            <a @click="$router.push({ name: 'Books' })"
              ><span
                class="fa fa-home"
                style="font-size: 2rem; color: white"
              ></span
            ></a>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

import '@/assets/css/login.css'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  mounted () {
    document.title = 'Login | Code & Chill'
  },
  methods: {
    async submitForm () {
      axios.defaults.headers.common['Authorization'] = ''

      localStorage.removeItem('token')

      const formData = {
        email: this.email,
        username: this.email,
        password: this.password
      }

      await axios
        .post('/api/v1/token/login/', formData)
        .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
            localStorage.setItem('token', token)
            
            const toPath = this.$route.query.to || '/cart'
            this.$router.push(toPath)
        })
        .catch(error => {
            if (error.response) {
              console.log(JSON.stringify(error.response.data))
            } 
            else {
              console.log(JSON.stringify(error))
            }
        })
    }
  }
}
</script>

<style>
.login,
.image {
  min-height: 100vh;
}
.bg-image {
  background-image: url("https://images.pexels.com/photos/3879495/pexels-photo-3879495.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  background-size: cover;
  background-position: center;
}
</style>

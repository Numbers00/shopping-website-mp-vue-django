<template>
<div class="container px-4 py-5 mx-auto" style="margin-bottom: 200px">
  <ul class="bs4-order-tracking" style="padding-top: 10px;">
    <li class="step active" style="font-size: 14px;">
      <div><i class="fa fa-user"></i></div>
      <a @click="$router.push({ name: 'Books' })" style="text-decoration: none; color: inherit">Shop More</a>
    </li>
    <li class="step active" style="font-size: 14px;">
      <div><i class="fa fa-user"></i></div>
      <a style="text-decoration: none; color: inherit">Cart</a>
    </li>
    <li class="step" style="font-size: 14px;">
      <div><i class="fa fa-money"></i></div>
      Payment
    </li>
    <li class="step" style="font-size: 14px;">
      <div><i class="fa fa-truck"></i></div>
      Delivery
    </li>
  </ul>
  <br><br>
  <div class="row d-flex justify-content-space-around">
    <div class="col-5" style="text-align: center">
      <h5 class="mt-2">Selected items</h5>
    </div>
    <div class="col-7">
      <div class="row" style="text-align: center">
        <div class="col-6">
          <h6 class="mt-2">Quantity & Price</h6>
        </div>
        <div class="col-6">
          <h6 class="mt-2">Options</h6>
        </div>
      </div>
    </div>
  </div>
  <CartItem 
    v-for='item in cart.items'
    :key='item.id'
    :initialItem='item'
    v-on:removeFromCart='removeFromCart'
  />
  <br />
  <button class="subscribe btn btn-primary btn-block shadow-sm" style="float: right">
    <a @click="$router.push({ name: 'Payment' })" style="text-decoration: none; color: inherit">Proceed to Payment</a>
  </button>
</div>
</template>

<script>
import '@/assets/js/cart.js'

import CartItem from '@/components/CartItem.vue'

export default {
  name: 'Cart',
  components: {
    CartItem
  },
  data () {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
        this.cart = this.$store.state.cart
        document.title = 'Cart | Code & Chill'
        console.log(this.cart)
    },
    methods: {
        removeFromCart (item) {
          console.log('yes')
          console.log(item.book.id + ' ' + item.author.id)
          this.cart.items = this.cart.items.filter(i => {
            console.log(i.book.id + ' vs. ' + item.book.id)
            return i.book.id !== item.book.id
          })
        }
    },
    computed: {
        cartTotalLength () {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice () {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.book.price * curVal.quantity
            }, 0)
        }
    }
}
</script>

<style>
body {
  background-color: white !important;
}
</style>

<style scoped src='@/assets/css/cart.css'>
.inline {
  display: inline-block;
}
.hover {
  transition: all 0.5s ease;
  background: white;
  padding: 10px;
}
.selected {
  transition: all 0.5s ease;
}
.hover:hover {
  background: rgb(240, 242, 243);
  padding: 20px;
  color: black;
}
.hover:hover .selected {
  background: rgb(14, 50, 78);
  color: white;
  border-radius: 5px;
}
input,
button {
  display: inline-block;
}
#add {
  border-radius: 5px;
  border: 1.5px solid black;
}
#subtract {
  border-radius: 5px;
  border: 1.5px solid black;
}
</style>
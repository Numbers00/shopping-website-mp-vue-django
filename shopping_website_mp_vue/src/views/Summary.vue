<template>
<div>
  <div id="container py-5" style="padding: 45px 100px;">
        <ul class="bs4-order-tracking" style="padding-top: 10px;">
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-user"></i></div>
                <a @click="$router.push({ name: 'Books' })" style="text-decoration: none; color: inherit">Shop More</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-user"></i></div>
                <a @click="$router.push({ name: 'Cart' })" style="text-decoration: none; color: inherit">Cart</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-money"></i></div>
                <a @click="$router.push({ name: 'Payment' })" style="text-decoration: none; color: inherit">Payment</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-truck"></i></div>
                Delivery
            </li>
        </ul>
        <!-- ****** Checkout Area Start ****** -->
        <div class="checkout_area section_padding_100">
            <div class="container">
                <div class="row">
                    <div class="col-12 col-md-6" style="margin-right: 40px;">
                        <div class="checkout_details_area mt-50 clearfix">

                            <div class="cart-page-heading">
                                <div class="row">
                                    <div class="col-2">
                                        <i class="fa fa-truck" style="font-size: 2.5rem; padding-left: 20px;"></i>
                                    </div>
                                    <div class="col-10" style="text-align: left;">
                                        <h5>Delivery Method</h5>
                                        <p>Kindly choose from options below.</p>
                                    </div>
                                </div>
                            </div>

                            <form action="#" method="post">
                                <div class="row">
                                    <div class="col-12">
                                        <label>
                                            <input type="radio" name="standard" class="card-input-element" />
                                            <div class="col-12 card-input mb-3" @click="handleClickFree"  style="border: 1px solid gray; max-width: 540px;">
                                                <div class="row g-0">
                                                    <div class="col-md-4">
                                                        <img src="https://thumbs.dreamstime.com/b/deliveryvantimeoutline-194934255.jpg"
                                                            style="padding-top: 20px; max-width: 170px; display: block; margin-left: auto; margin-right: auto;"
                                                            alt="...">
                                                    </div>
                                                    <div class="col-md-8">
                                                        <div class="card-body" style="margin: 10px 10px 10px 10px;">
                                                            <h5 class="card-title">Free Delivery</h5>
                                                            <p class="card-text">Code&Chill loves bibliophiles like you!
                                                                Just wait for your book right at your doorstep
                                                                with our free delivery service.
                                                            </p>
                                                            <p class="card-text"><small class="text-muted">Est. Delivery
                                                                    Time: 7 - 14 days</small></p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </label>
                                    </div>
                                    <div class="col-12">
                                        <label>
                                            <input type="radio" name="standard" class="card-input-element" />
                                            <div class="col-12 card-input mb-3" @click="handleClickExpress" style="border: 1px solid gray; max-width: 540px;">
                                                <div class="row g-0">
                                                    <div class="col-md-4">
                                                        <img src="https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/B2b8RSzfgivu3v9nb/logistic-shipping-and-freight-transportation-business-animated-icons-set-of-truck-cardboard-box-train-available-in-4k-uhd-fullhd-and-hd-3d-video-animation-footage_s9cl4f5gx_thumbnail-1080_09.png"
                                                            style="padding-top: 20px; max-width: 170px; display: block; margin-left: auto; margin-right: auto;"
                                                            alt="...">
                                                    </div>
                                                    <div class="col-md-8">
                                                        <div class="card-body" style="margin: 10px 10px 10px 10px;">
                                                            <h5 class="card-title">Express Delivery</h5>
                                                            <p class="card-text">Wait for your book right at your
                                                                doorstep in few days time with our
                                                                standard delivery service. Just add P50 and you're good
                                                                to go.
                                                            </p>
                                                            <p class="card-text"><small class="text-muted">Est. Delivery
                                                                    Time: 1 - 5 days</small></p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </label>
                                    </div>
                                </div>
                            </form>
                            <br>
                            <br>
                        </div>
                    </div>

                    <div class="col-12 col-md-6 col-lg-5 ml-lg-auto">
                        <div class="order-details-confirmation">
                            <div class="cart-page-heading">
                                <h5>Your Order</h5>
                                <p>The Details</p>
                            </div>

                            <ul class="order-details-form mb-4">
                                <li><span>Product</span> <span>Total</span></li>
                                <li
                                  v-for="item in cart.items"
                                  :key="item"
                                >
                                  <span>{{item.book.title}}</span> <span>{{'(' + item.quantity + ') $' + (Math.round(getItemTotal(item)*100)/100).toFixed(2)}}</span>
                                </li>
                                <li><span>Subtotal</span> <span>${{(Math.round(cartTotalPrice*100)/100).toFixed(2)}}</span></li>
                                <li><span>Shipping</span> 
                                    <span v-if="freeToggle">Free</span>
                                    <span v-if="expressToggle">$1</span>
                                </li>
                                <li><span>Total</span> <span>${{computeTotal}}</span></li>
                            </ul>


                            <p style="padding-left: 25px; padding-bottom: 20px;">
                              Selected Method: 
                              <strong v-if="viaCredit"> Credit Card</strong> 
                              <strong v-if="!viaCredit"> Cash on Delivery</strong> 
                            </p>

                            <a @click="placeOrder" class="btn karl-checkout-btn" style="color: white;">Place Order</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        <!-- ****** Checkout Area End ****** -->
    </div>
</div>
</template>

<script>
import axios from 'axios'

import '@/assets/js/summary_jquery-2.2.4.min.js'
import '@/assets/js/summary_popper.min.js'
import '@/assets/js/summary_plugins.js'

export default {
  name: 'Summary',
  props: {
    viaCredit: Boolean,
    fullName: String,
    address: String,
    phone: String
  },
  data () {
    return {
      cart: {
        items: [],
      },
      freeToggle: true,
      expressToggle: false
    }
  },
  mounted () {
    this.cart = this.$store.state.cart

    document.title = 'Summary | Code & Chill'
  },
  methods: {
    getItemTotal (item) {
        return item.quantity * item.book.price
    },
    async placeOrder () {
        const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    book: item.book.id,
                    author: item.author.id,
                    quantity: item.quantity,
                    price: (Math.round(item.book.price * item.quantity *100)/100).toFixed(2)   
                }
                items.push(obj)
            }
        const data = {
            'full_name': this.$store.state.paymentCredentials.fullName,
            'address': this.$store.state.paymentCredentials.address,
            'phone': this.$store.state.paymentCredentials.phone,
            'items': items
        }

        console.log(data)

        await axios
            .post('/api/v1/checkout/', data)
            .then(response => {
                this.$store.commit('clearCart')
                this.$router.push('/confirmation')
            })
            .catch(error => {
                console.log(error)
            })

        this.$store.commit('setIsLoading', false)
    },
    handleClickFree () {
        if (!this.freeToggle) {
          this.freeToggle = true
          this.expressToggle = false
        }
      },
    handleClickExpress () {
      if (!this.expressToggle) {
        this.expressToggle = true
        this.freeToggle = false
      }
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
        },
        computeTotal () {
            if (this.expressToggle) {
                return (Math.round((this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.book.price * curVal.quantity
                }, 0) + 1)*100)/100).toFixed(2)
            }
            else return (Math.round(this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.book.price * curVal.quantity
                }, 0)*100)/100).toFixed(2)
        }
    }
}
</script>

<style scoped src='@/assets/css/summary_core-style.css'></style>
<style scoped src='@/assets/css/summary_responsive.css'></style>


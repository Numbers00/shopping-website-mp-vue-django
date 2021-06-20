<template>
<div style="display: block; margin: auto; position: relative; bottom: 50px;">
    <br /><br /><br />
    <div class="container">
      <div class="row">
        <div class="col-lg-7 col-12">
          <div class="row">
            <div class="col-md-4 col-5">
              <img
                :src="book.image"
                alt=""
                width="100%"
              />
              <div class="rating" style="text-align: center; margin: 10px">
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star-half-o"></i>
              </div>
            </div>
            <div class="col-md-8 col-7">
              <h4 class="book-title" style="text-align: left;">{{ book.title }}</h4>
              <vue-show-more-text
                :text="book.sypnosis"
                :lines="10"
                additional-container-css="max-height: 360px; padding-right: 20px; overflow: auto; margin: 24px 14px 14px 0; text-align: left; position: relative; right: 30px; bottom: 12px;"
                @click="change"
              />
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-3">
              <img
                :src="author.image"
                alt=""
                style="width: 100px; height: 100px; border-radius: 50%"
                class="author-img"
              />
            </div>
            <div class="col-9">
              <p class="author-desc">
                <small
                  ><strong>About the Author.</strong><i class="fa fa-leaf ml-2"></i>
                  <template v-if="author.description != '' && author.description != null">
                    <vue-show-more-text
                      :text="author.description"
                      :lines="5"
                      additional-container-css="max-height: 100px; padding-right: 20px; overflow: auto; margin:14px; text-align: left; position: relative; right: 45px; bottom: 12px;"
                      @click="change"
                    />
                  </template>
                  <template v-else>
                    <vue-show-more-text
                      text="the author has no available information."
                      :lines="5"
                      additional-container-css="color: gray; max-height: 100px; padding-right: 20px; overflow: auto; margin:14px; text-align: left; position: relative; right: 25px; bottom: 12px;"
                      @click="change"
                    />
                  </template>
                </small>
              </p>
            </div>
          </div>
          <hr />
        </div>
        <div class="col-lg-5 col-12" style="text-align: left; max-height: 550px" id="payment">
          <h1 class="inline"><sup id="symbol">$</sup></h1><h1 id="value" class="inline">{{ book.price }}</h1>
          <button class="inline" id="convert" onclick="DollarToPHP()" style="float: right; border-radius: 5px; border: 1px solid gray;">Convert to PHP</button>
          <div class="row mb-4">
            <div class="col-9">
              <div class="buttons">
                <button class="cart-button" @click="addToCart">
                  <span class="add-to-cart">Add to cart</span>
                  <span class="added">Item added</span>
                  <i class="fa fa-shopping-cart"></i>
                  <i class="fa fa-circle-thin"></i> <i class="fa fa-check"></i>
                </button>
              </div>
            </div>
            <div class="col-3">
              <div class="buttons">
                <button class="buy-button" style="background: black;">
                  <a href="login.html" style="text-decoration: none; color: inherit;">Buy</a>
                </button>
              </div>
            </div>
          </div>

          <div class="row mb-5" style="margin: auto;">
            <div class="col-6">
              <h6 style="color: gray;">Quantity</h6>
              <button @click="decrementQuantity" class="inline" id="subtract" style="padding: 10px;">-</button>
              <input v-model.number="quantity" class="inline" id="quantity" type="number" min="1" style="width: 80px; padding: 10px;">
              <button @click="incrementQuantity" class="inline" id="add" style="padding: 10px;">+</button>
            </div>
            <div class="col-6">
              <i class="fa fa-lock" style="padding-top: 25px;"></i>
              <small>Secure Checkout</small><br>
              <small><em>Available nationwide.</em></small>
            </div>
            <div class="col-6"></div>
          </div>
          <h6 style="text-align: center; padding: 15px 0 0 5px;">You can pay through</h6>
          <hr />
          <div class="payment-option">
            <img style="width: 160px;" src="@/assets/img/gallery/american_express.png" alt="" />
            <img style="width: 160px;" src="@/assets/img/gallery/mastercard.png" alt="" />
            <img style="width: 160px;" src="@/assets/img/gallery/paypal.png" alt="" />
          </div>
        </div>
      </div>

      <h6 class="title">Product Details</h6>
      <div class="row" style="padding: 20px">
        <table class="table table-dark table-hover">
          <thead style="display: none">
            <tr>
              <th scope="col" id="table-aligned">Name</th>
              <th scope="col" id="table-aligned">Birthday</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="col-4" id="table-aligned">Author Name</td>
              <td class="col-8" id="table-aligned">{{ author.name }}</td>
            </tr>
            <tr>
              <td id="table-aligned">Publisher</td>
              <td id="table-aligned">{{ book.publishers }}</td>
            </tr>
            <tr>
              <td id="table-aligned">Genres</td>
              <td id="table-aligned">{{ book.genres }}</td>
            </tr>
            <tr>
              <td id="table-aligned">Origin</td>
              <td id="table-aligned">International</td>
            </tr>
            <tr>
              <td id="table-aligned">Book Format</td>
              <td id="table-aligned">Trade Paperback</td>
            </tr>
            <tr>
              <td id="table-aligned">Weight</td>
              <td id="table-aligned">0.42 kg</td>
            </tr>
            <tr>
              <td id="table-aligned">Length</td>
              <td id="table-aligned">20.42 cm</td>
            </tr>
            <tr>
              <td id="table-aligned">Width</td>
              <td id="table-aligned">15.24 cm</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import vueShowMoreText from 'vue-show-more-text'
import {toast} from 'bulma-toast'

export default {
  name: 'Product',
  components: {
    vueShowMoreText
  },
  data () {
    return {
      book: {},
      author: {},
      quantity: 1
    }
  },
  mounted () {
    this.getBook()
  },
  methods: {
    async getBook () {
      this.$store.commit('setIsLoading', true)

      const book_type_slug = this.$route.params.book_type_slug
      const author_slug = this.$route.params.author_slug
      const book_slug = this.$route.params.book_slug

      await axios
        .get(`api/v1/books/${book_type_slug}/${author_slug}/${book_slug}`)
        .then(response => {
          this.book = response.data
        })
        .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        })

      await axios
        .get(`api/v1/books/${author_slug}`)
        .then(response => {
          this.author = response.data
        })
        .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        })

      this.$store.commit('setIsLoading', false)
    },
    incrementQuantity () {
      this.quantity += 1
    },
    decrementQuantity () {
      this.quantity -= 1
    },
    addToCart () {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                book: this.book,
                author: this.author,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The book was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
  }
}
</script>

<style scoped>
.intro-content {
  padding-left: 20px;
}

.author-img {
  margin: auto;
  display: block;
  padding-top: 5px;
}

.rating {
  color: orange;
}

.author-desc {
  text-align: left;
}

.book-title {
  font-weight: bold;
  padding-bottom: 15px;
}

.book-desc {
  padding-right: 20px;
  text-align: left;
}

#payment {
  border: 0.5px solid rgb(134, 134, 134);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 30px;
}

.payment-option img {
  width: 100px;
  margin: 10px 5px;
}

.payment-option {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

.title {
  text-align: center;
  margin: 0 auto 15px;
  color: rgb(27, 26, 26);
  line-height: 60px;
  position: relative;
  text-transform: uppercase;
  letter-spacing: 3px;
}

.title::after {
  content: "";
  background: rgb(161, 85, 34);
  width: 100px;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}

#table-aligned {
  text-align: left;
  padding-left: 20px;
}

/* cart */

.buttons {
  margin: 0;
  padding: 0;
  height: 15vh;
  display: flex;
  justify-content: left;
  align-items: center;
}

.buy-button {
  position: relative;
  outline: 0;
  background-color: black;
  color: #fff;
  border: none;
  height: 60px;
  width: 100%;
  padding: 10px;
  border-radius: 10px;
  line-height: 0px;
  overflow: hidden;
}

.buy-button:focus {
  outline: none !important;
}

.cart-button {
  position: relative;
  outline: 0;
  background-color: blue;
  color: #fff;
  border: none;
  height: 60px;
  width: 100%;
  padding: 10px;
  border-radius: 10px;
  line-height: 0px;
  overflow: hidden;
}

.cart-button:focus {
  outline: none !important;
}

.cart-button .fa-shopping-cart {
  position: absolute;
  z-index: 2;
  top: 50%;
  left: 18%;
  font-size: 1.2em;
  transform: translate(-50%, -50%);
}

.cart-button .fa-circle-thin {
  position: absolute;
  z-index: 1;
  top: 50%;
  left: -20%;
  font-size: 1.5em;
  transform: translate(-50%, -50%);
}

.cart-button .fa-check {
  position: absolute;
  z-index: 1;
  top: -52%;
  left: 20%;
  font-size: 0.7em;
  transform: translate(-50%, -50%);
}

.cart-button span {
  position: absolute;
  left: 50%;
  top: 50%;
  color: #fff;
  transform: translate(-50%, -50%);
  font-size: 16px;
}

.cart-button span.added {
  opacity: 0;
}

.cart-button.clicked .fa-shopping-cart {
  animation: addicon 2s ease-in forwards;
}

.cart-button.clicked {
  animation: color 2s ease-in forwards;
}

.cart-button.clicked .fa-circle-thin {
  animation: circle 1s ease-in forwards;
}

.cart-button.clicked .fa-check {
  animation: check 2s ease-in forwards;
}

.cart-button.clicked span.add-to-cart {
  animation: addcart 2s ease-in forwards;
}

.cart-button.clicked span.added {
  animation: added 2s ease-in forwards;
}

/* Wishlist Button */

.wishlist-button {
  position: relative;
  outline: 0;
  background-color: black;
  color: #fff;
  border: none;
  height: 60px;
  width: 100%;
  padding: 10px;
  border-radius: 10px;
  line-height: 0px;
  overflow: hidden;
}

.wishlist-button:focus {
  outline: none !important;
}

.wishlist-button span {
  position: absolute;
  left: 50%;
  top: 50%;
  color: #fff;
  transform: translate(-50%, -50%);
  font-size: 16px;
}

.wishlist-button span.added {
  opacity: 0;
}

.wishlist-button.clicked .fa-shopping-cart {
  animation: addicon 2s ease-in forwards;
}

.wishlist-button.clicked {
  animation: color 2s ease-in forwards;
}

.wishlist-button.clicked .fa-circle-thin {
  animation: circle 1s ease-in forwards;
}

.wishlist-button.clicked .fa-check {
  animation: check 2s ease-in forwards;
}

.wishlist-button.clicked span.add-to-cart {
  animation: addcart 2s ease-in forwards;
}

.wishlist-button.clicked span.added {
  animation: added 2s ease-in forwards;
}

@keyframes addicon {
  0% {
    opacity: 1;
  }

  30%,
  100% {
    opacity: 0;
  }
}

@keyframes circle {
  0% {
    left: -10%;
  }

  100% {
    left: 20%;
  }
}

@keyframes check {
  0%,
  40% {
    top: -20%;
  }

  60% {
    top: 48%;
  }

  100% {
    top: 48%;
  }
}

@keyframes addcart {
  0%,
  30% {
    opacity: 1;
  }

  30%,
  100% {
    opacity: 0;
  }
}

@keyframes added {
  0%,
  80% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes color {
  0% {
    background-color: blue;
  }

  80%,
  100% {
    background-color: green;
  }
}

/* delete */

.sale {
  flex-direction: row-reverse;
}

.card {
  width: 80%;
  transition: transform 0.5s ease-in;
}

.card-body {
  width: auto;
}

.btn {
  border-radius: 0;
  width: fit-content;
  background-color: #69f0ae;
  box-shadow: 0px 10px 10px #e0e0e0;
  z-index: 1;
  color: rgb(26, 75, 236);
  width: 100px;
  font-size: 14px;
  font-weight: 900;
}

.img-thumbnail {
  border: none;
  padding: 10px;
}

.card {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  padding-bottom: 10px;
  width: 225px;
}

.card:hover {
  transform: translateY(-3px);
}

.card-title {
  font-size: 14px;
  font-weight: 900;
}

.card-text {
  font-size: 14px;
  font-family: sans-serif;
  font-weight: 500;
}

.inline {
  display: inline-block;
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

<style scoped src="@/assets/css/books.css">
</style>

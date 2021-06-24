<template>
<div class="hover row d-flex justify-content-center border-top">
  <div class="selected col-5">
    <div class="row d-flex">
      <div class="col-5">
        <div class="book">
          <img :src="item.book.image" class="book-img" />
        </div>
      </div>
      <div class="col-7">
        <div class="my-auto position-relative" style="right: 50px;">
          <vue-show-more-text
            :text="item.book.title + '\n' + item.author.name + '\n$ ' + item.book.price"
            :lines="4"
            additional-container-css="overflow: auto; margin:14px; text-align: left; position: relative; right: 25px; bottom: 12px;"
            @click="change"
          />
        </div>
      </div>
    </div>
  </div>
  <div class="my-auto col-7">
    <div class="row" style="text-align: center">
      <div class="col-6">
        <input disabled class="inline quantity" type="text" :value="item.quantity + '  ($' + (Math.round(getItemTotal(item)*100)/100).toFixed(2) + ')'" style="background-color: white; width: 40%; padding: 10px; border-radius: 0; margin: 0 3px 0 3px;" />
      </div>
      <div class="col-6">
        <button @click='incrementQuantity(item)' class='btn btn-danger btn-outline-dark btn-lg'><i class="fa fa-plus"></i></button>
        <button @click='decrementQuantity(item)' class='btn btn-success btn-outline-dark btn-lg'><i class="fa fa-minus"></i></button>
        <button class="btn trash-btn btn-outline-dark btn-lg" @click="removeFromCart(item)">
          <i class="fa fa-trash" style="text-align: center;"></i>
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import vueShowMoreText from 'vue-show-more-text'

export default {
  name: 'CartItem',
  components: {
    vueShowMoreText
  },
  props: {
    initialItem: Object
  },
  data () {
    return {
      item: this.initialItem
    }
  },
  methods: {
    getItemTotal (item) {
        return item.quantity * item.book.price
    },
    decrementQuantity (item) {
        item.quantity -= 1
        if (item.quantity === 0) {
            this.$emit('removeFromCart', item)
        }
        this.updateCart()
    },
    incrementQuantity (item) {
        item.quantity += 1
        this.updateCart()
    },
    updateCart () {
        localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },
    removeFromCart (item) {
      this.$emit('removeFromCart', item)
      this.updateCart()
    }
  }
}
</script>

<style scoped src='@/assets/css/cart.css'>
</style>
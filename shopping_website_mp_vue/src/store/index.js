import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cart: {
        items: [],
    },
    paymentCredentials: {
      fullName: '',
      address: '',
      phone: '',
      cashInHand: '',
      cardNumber: '',
      expirationMM: '',
      expirationYY: '',
      CVV: ''
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    windowWidth: window.innerWidth
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('paymentCredentials')) {
        state.paymentCredentials = JSON.parse(localStorage.getItem('paymentCredentials'))
      } else {
        localStorage.setItem('paymentCredentials', JSON.stringify(state.paymentCredentials))
      }


      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.book.id === item.book.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    confirmPayment(state, item) {
      state.paymentCredentials.fullName = item.fullName
      state.paymentCredentials.address = item.address
      state.paymentCredentials.phone = item.phone
      state.paymentCredentials.cashInHand = item.cashInHand
      state.paymentCredentials.cardNumber = item.cardNumber
      state.paymentCredentials.expirationMM = item.expirationMM
      state.paymentCredentials.expirationYY = item.expirationYY
      state.paymentCredentials.CVV = item.CVV

      localStorage.setItem('paymentCredentials', JSON.stringify(state.paymentCredentials))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    clearPaymentCredentials(state) {
      state.paymentCredentials = {
        fullName: '',
        address: '',
        phone: '',
        cashInHand: '',
        cardNumber: '',
        expirationMM: '',
        expirationYY: '',
        CVV: ''
      }

      localStorage.setItem('paymentCredentials', JSON.stringify(state.paymentCredentials))
    },
    setWindowWidth(state) {
      state.windowWidth = window.innerWidth;
    }
  },
  actions: {
  },
  modules: {
  }
})


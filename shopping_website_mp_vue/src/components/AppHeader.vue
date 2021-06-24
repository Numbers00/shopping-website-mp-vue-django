<template>
<div>
<nav
  id="site-header"
  class="navbar navbar-expand-lg navbar-dark bg-dark"
  style="padding: 15px"
>
  <div class="container-fluid">
    <a class="navbar-brand" @click="$router.push({ name: 'Homepage' })">
      <img
        src="@/assets/img/chill_logo.png"
        alt=""
        style="width: 200px; border-radius: 5px; padding-left: 15px"
      />
    </a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarText"
      aria-controls="navbarText"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0"
        v-for="(view, index) in views"
        :key="index"
      >
        <li class="nav-item" style="padding-left: 15px; font-size: 20px">
          <a class="nav-link active" aria-current="page" @click="$router.push({ name: view.name })">{{ view.name }}</a>
        </li>
      </ul>
      <form
        class="d-flex"
        style="padding-right: 10px; padding-left: 15px; padding-bottom: 5px"
        method="get"
        action="/books/search"
      >
        <input
          class="form-control me-2"
          type="search"
          placeholder="Search"
          aria-label="Search"
          name="query"
        />
        <button class="btn btn-outline-success" type="submit">
          Search
        </button>
      </form>
      <router-link to="/cart" class="btn btn-success position-relative" style="bottom: 2px">
        <span class="icon"><i class="fa fa-shopping-cart"></i></span>
        <span> Cart ({{ cartTotalLength }})</span>
      </router-link>
      <div class="hover-dropdown">
      <span class="navbar-text">
        <a href="#">
          <i
            class="fa fa-user"
            aria-hidden="true"
            style="font-size: 2rem; padding: 0 10px"
          ></i>
        </a>
      </span>
      <div class="hover-dropdown-content">
        <template v-if="$store.state.isAuthenticated">
          <p @click="$router.push({name: 'Profile'})">Profile</p>
          <p @click="logout()">Logout</p>
        </template>
        <template v-else>
          <p @click="$router.push({name: 'Login'})">Login</p>
          <p @click="$router.push({name: 'Signup'})">Signup</p>
        </template>
      </div>
      </div>
    </div>
  </div>
</nav>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AppHeader',
  data () {
    return {
      cart: {
        items: []
      },
      views: [
        { name: 'Books', to: '/books' },
        { name: 'AboutUs', to: 'aboutus' },
        { name: 'Cafe', to: '/cafe' },
        { name: 'Tutors', to: '/tutors' }
      ],
      bookViews: [
        { name: 'Bestsellers', to: '/bestsellers' },
        { name: 'Manga', to: '/manga' },
        { name: 'Light Novels', to: '/light-novels' },
        { name: 'Western Novels', to: '/western-novels' }
      ]
    }
  },
  mounted () {
    this.cart = this.$store.state.cart
    console.log(this.$store.state.isAuthenticated)
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
  },
  computed: {
      cartTotalLength() {
          let totalLength = 0
          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }
          return totalLength
      }
  }
}
</script>

<style scoped src='@/assets/css/nav.css'></style>

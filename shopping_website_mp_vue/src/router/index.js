import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import store from '../store'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/lowerhomepage',
    name: 'LowerHomepage',
    component: () => import('../views/LowerHomepage.vue')
  },
  {
    path: '/aboutus',
    name: 'AboutUs',
    component: () => import('../views/AboutUs.vue')
  },
  {
    path: '/books',
    name: 'Books',
    component: () => import('../views/Books.vue'),
    props: true
  },
  {
    path: '/cafe',
    name: 'Cafe',
    component: () => import('../views/Cafe.vue'),
    props: true
  },
  {
    path: '/tutors',
    name: 'Tutors',
    component: () => import('../views/Tutors.vue'),
    props: true
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    props: true
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/Signup.vue'),
    props: true
  },
  {
    path: '/:book_type_slug/:author_slug/:book_slug/',
    name: 'Product',
    component: () => import('../views/Product.vue'),
    props: true
  },
  {
    path: '/tutelage',
    name: 'Tutelage',
    component: () => import('../views/Tutelage.vue'),
    props: true
  },
  {
    path: '/books/manga',
    name: 'Manga',
    component: () => import('../views/Manga.vue'),
    props: true
  },
  {
    path: '/books/light-novels',
    name: 'LightNovels',
    component: () => import('../views/LightNovels.vue'),
    props: true
  },
  {
    path: '/books/western-novels',
    name: 'WesternNovels',
    component: () => import('../views/WesternNovels.vue'),
    props: true
  },
  {
    path: '/books/bestsellers',
    name: 'Bestsellers',
    component: () => import('../views/Bestsellers.vue'),
    props: true
  },
  {
    path: '/books/scholarly',
    name: 'Scholarly',
    component: () => import('../views/Scholarly.vue'),
    props: true
  },
  {
    path: '/books/card-bestsellers',
    name: 'CardBestsellers',
    component: () => import('../views/CardBestsellers.vue'),
    props: true
  },
  {
    path: '/books/search',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../views/Cart.vue')
  },
  {
    path: '/confirmation',
    name: 'Confirmation',
    component: () => import('../views/Confirmation.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/error',
    name: 'Error',
    component: () => import('../views/Error.vue')
  },
  {
    path: '/payment',
    name: 'Payment',
    component: () => import('../views/Payment.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/summary',
    name: 'Summary',
    component: () => import('../views/Summary.vue'),
    props: true,
    meta: {requireLogin: true}
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
    meta: {requireLogin: true}
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.length === 0) {
    next({path: '/error'})
  }
  else {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
      next({path: '/login', query: {to: to.path}})
    } else {
      next()
    }
  }
})

export default router

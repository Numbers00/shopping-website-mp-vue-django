<template>
<div style="background-color: #446072; font-family: monospace; height: 700px;">
  <br>
  <br>
  <br>
  <nav class=" shelf">
      <a @click="$router.push({ name: 'Books' })" class="book home-page" href="#" style="text-decoration: none;">Books</a>
      <a @click="$router.push({ name: 'AboutUs' })" class="book about-us" href="#" style="text-decoration:none">About us</a>
      <a @click="$router.push({ name: 'Signup' })" class="book contact" href="#" style="text-decoration:none">Sign Up</a>
      <a @click="$router.push({ name: 'Homepage' })" class="book faq" href="#" style="text-decoration:none">Home</a>

      <span class="book not-found"></span>

      <span class="door left"></span>
      <span class="door right"></span>
  </nav>
  <h1>Error 404</h1>
  <p>The page you're looking for may be on another bookshelf.</p>
</div>
</template>

<script>

export default {
  name: 'Error',
  mounted () {
    document.title = 'Error Encountered :<< | Code & Chill'
  }
}
</script>

<style scoped src='@/assets/css/error.css'></style>
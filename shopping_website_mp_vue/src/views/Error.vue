<template>
<div>
  <nav class=" shelf">
      <a class="book home-page" href="#" style="text-decoration: none;">Books</a>
      <a class="book about-us" href="#" style="text-decoration:none">About us</a>
      <a class="book contact" href="#" style="text-decoration:none">Sign Up</a>
      <a class="book faq" href="#" style="text-decoration:none">Home</a>

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

<style sourced src='@/assets/css/error.css'></style>
<template>
<div class="container-xl p-5 m-auto">
<div class="row mx-5" style="font-size: large;">

    <div class="col p-3 m-auto" style="text-align: center;  color: #4A558F; background-color: #a4a9c2;">

        <h1 style="font-family: Fredoka One;">
            Welcome, let's code and chill!
          </h1>
          <h3 style="font-family: quicksand;">
            Is this your first time here? Come and join us!
          </h3>
          <button type="button" class="btn btn-outline-light" id="register" @click="$router.push({ name: 'Signup' })" style="color: #373973; font-family: quicksand;"><b>Sign Up</b></button>
          <h3 style="font-family: quicksand;">
            Ready to start the Code & Chill experience?
          </h3>
          <button type="button" class="btn btn-outline-light" id="showBanners" @click="isHidden == true ? isHidden = false : isHidden = true" style="color: #373973; font-family: quicksand;"><b>READY!</b></button>

        </div>
    <div class="col mx-0">
            <img src="@/assets/img/illustrations/codinggif.gif" width="100%">
            <div id="overlay0"></div>
    </div>

    <div class="overlay0" style="top: 0%; min-height: 10%; max-height: 10%;"></div>

</div><!-- end of row -->

<div id="homepage2" class="container-xl p-5 m-5"  v-if="!isHidden">

  <div class="overlay0" style="bottom: 33%; height: 10%;"></div>

  <div class="mx-auto">
  <div class="row mx-auto m-5 offset-3" style="font-size: large; text-align: center; color:#ED8A61;">
  <br><br><br>
  <h1 style="font-family: fredoka one;">What do you want to do right now?</h1>
  </div>
  <div class="row mx-auto offset-3" style="font-size: large; width: 75vw; position: relative; left: 50%; transform: translate(-50%);">

      <div class="col-md p-3 m-auto offset-md-3">
         <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/books_dark.jpeg') + ')'}">
              <div class="panel">
              <h1><b>Rent or Buy a Book</b></h1>
              <p>Choose from our handpicked selection of books with reasonable prizes
                  <a @click="$router.push({ name: 'Books' })">here</a>
              </p>
          </div>
      </div>
      </div>

      <div class="col-md p-3 m-auto offset-1" >
          <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/collaboration.jpg') + ')'}">
          <div class="panel">
              <h1><b>Tutorial Services</b></h1>
              <p>Having a hard time? Looking for a study buddy? Read about our study hub
                  <a @click="$router.push({ name: 'Tutors' })">here</a>
              </p>
          </div>
          </div>

      </div>
      <div class="col-md p-3 m-auto offset-1 " >
          <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/kimchiFR.jpg') + ')'}">
          <div class="panel">
              <h1><b>About Us</b></h1>
              <p>Know more about the developers
                  <a @click="$router.push({ name: 'Tutors' })">here</a>
              </p>
          </div>
          </div>
      </div>
      <div class="col-md p-3 m-auto offset-1 " >
          <div class="item" :style="{'background-image': 'url(' + require('@/assets/img/gallery/donutcoffee.jpg') + ')'}">
          <div class="panel">
              <h1><b>Donuts & Coffee</b></h1>
              <p>
                Brew & Bake corner coming
                <a @click="$router.push({ name: 'Cafe' })">here</a>
                soon!
              </p>
          </div>
          </div>
      </div>
      <button type="button" class="btn btn-outline-light" id="showHomepage2" @click="$router.push({ name: 'LowerHomepage' })" style="color: #373973; font-family: quicksand;"><b>Open in a new window</b></button>
      </div>

  </div>
</div>

</div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data () {
    return {
      isHidden: true
    }
  }
}
</script>

<style scoped src="@/assets/css/design.css"></style>

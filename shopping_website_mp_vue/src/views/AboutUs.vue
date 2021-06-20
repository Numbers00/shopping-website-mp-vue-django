<template>
<div>
<div class="headBox">
  <div class="headerPhoto2" :style="{'background-image': 'url(' + require('@/assets/img/gallery/frying.gif') + ')'}">
    <div class="headIcon">
    </div>

  </div>
</div>

<div class="container-md  mx-auto" >
    <div class="row mx-auto" style="text-align: center; color: #ED8A61; font-family: fredoka one;">
  <h1> <b>Kimchi Fried Rice</b> </h1>

    <i>About the Developers</i>
  </div>
    <div class="row mx-auto p-5" style="text-align:center; color:white;background-color: #ED8A61; font-family: 'quicksand';">
        <div class="col" >
            <div class="row">
            Kyle, Fed, and Rice are blockmates who formed a trio to craft a simple shopping website.
            They did it to fulfill the requirements as students of Computer Science, and with this,
            tried to combine their interests to make an amiable prototype shopping website. <br>
          </div>
          <div class="row">

            <i>Behind The Name</i>
            When you call developers, Fed and Rice in a fast way, someone might mistake you for asking
            for a bowl of hot, fried rice. The Kimchi stands for Kyle. It could've been Korean but we're Filipino.
          </div><div class="row">

            <br> <i>To be continued...</i></div>

        </div>
        <div class="col p-5" >
            <img src="@/assets/img/gallery/1.jpg" alt="A pic with Fed, Kyle, and Rice" style="position:relative;width: 100%;">

        </div>

    </div>
<br>
<button type="button" class="btn btn-outline-light" id="showBanners" @click="$router.push({ name: 'Homepage' })" style="position:absolute; left:50% ;color: #373973; font-family: quicksand;"><b>Back to homepage</b></button>
<br>
<br>
<br>
<br>
<br>
</div>
</div>
</template>

<style scoped src='@/assets/css/design.css'></style>

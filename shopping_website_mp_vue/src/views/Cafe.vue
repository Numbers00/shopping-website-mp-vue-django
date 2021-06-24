<template>
<div class="container-xl p-5 m-auto">
    <div class="row mx-5" style="font-size: large;">

        <div class="col p-3 m-auto" style="text-align: center;  color: #4A558F; background-color: #a4a9c2;">

            <h1 style="font-family: Fredoka One;">
                Brewing and baking new treats for you!
              </h1>

              <h3 style="font-family: quicksand;">
                Tune in for this bright new feature. In the meantime you can browse through our other features.
              </h3>
              <button type="button" class="btn btn-outline-light" id="showBanners" @click="$router.push({ name: 'LowerHomepage' })" style="color: #373973; font-family: quicksand;"><b>Go back and browse</b></button>

        </div>
        <div class="col mx-0">
          <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/3e2a0443163649.57f1d6ec22833.gif" width="100%">
          <div id="overlay0"></div>
  </div>
</div>

</div><!-- end of row -->
</template>

<script>

export default {
  name: 'Cafe',
  mounted () {
    document.title = 'Cafe | Code & Chill'
  }
}
</script>

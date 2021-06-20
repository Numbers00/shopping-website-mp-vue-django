<template>
<div class="col-lg-3 col-md-4 col-sm-6 col-12">
    <div class="card mx-auto col-md-3 col-10 mt-5 pt-4" :class="{'card-shadow': hasShadow, 'card-no-border': hasNoBorder}" :style="{'min-width': cardMinWidth, 'min-height': cardHeight, 'max-height': cardHeight, 'transform': cardScale + ' ' + cardTranslateY}">
      <div class="d-flex sale">
        <div class="btn card-btn" @click="$router.push({ path: '' + bookAbsoluteUrl, append: false})"><sup>$</sup>{{price}}</div>
        </div>
        <a href="#" style="margin-left: auto; margin-right: auto;">
            <img
                class="mx-auto img-thumbnail"
                :src="bookImg"
                width="auto"
                height="auto"
                :style="{'height': '250px'}"
            />
        </a>
        <div class="card-body text-center" :class="{'card-body-bg': hasBlackBackground}">
        <h5 class="card-title" :class="{'lightblue-color': isLightblue}">{{bookName}}</h5>
        <span class="card-text">
            <div class="rating">
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
                <i class="fa fa-star"></i>
            </div>
        </span>
        </div>
    </div>
</div>
</template>

<script>
export default {
  props: {
    bookName: String,
    price: String,
    bookImg: String,
    cardMinWidth: String,
    cardHeight: String,
    cardScale: String,
    hasShadow: Boolean,
    hasNoBorder: Boolean,
    hasBlackBackground: Boolean,
    isLightblue: Boolean,
    cardTranslateY: String,
    bookDesc: String,
    bookGenres: String,
    author: String,
    authorImg: String,
    authorDesc: String,
    comments: String,
    publishers: String,
    bookAbsoluteUrl: String
  }
}
</script>

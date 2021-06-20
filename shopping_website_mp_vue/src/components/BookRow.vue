<template>
<div id='book-row' :style="limitRowWidth">
  <BookCard
    :price="price"
    :bookImg="bookImg"
    :bookName="bookName"
    :cardMinWidth="cardMinWidth"
    :cardHeight="cardHeight"
    :cardScale="cardScale"
    boxShadow="null"
    :hasShadow="false"
    :hasBlackBackground="true"
    :isLightblue="true"
    cardTranslateY="translateY(-130px)"
    :bookDesc="bookDesc"
    :bookGenres="bookGenres"
    :author="author"
    :authorImg="authorImg"
    :authorDesc="authorDesc"
    :comments="comments"
    :publishers="publishers"
    :bookAbsoluteUrl="bookAbsoluteUrl"
  />
  <div id='right-text' class='mt-3'>
    <div id='book-params'>
      # {{ index }}
      <i class="fa fa-book ml-2 mr-1 mt-1"></i> 8 Volumes
      <i class="fa fa-user ml-2 mr-1 mt-1"></i> 10200 Copies Sold
      <i class="fa fa-comment ml-2 mr-1 mt-1"></i> 105 Reviews
    </div>
    <div id='genres-flex' v-if="bookGenres != null">
      <template
        v-for="(genre, index) in bookGenres.split(', ')"
      >
        <span class='colored-genre' :key="index">{{ genre }}</span>
      </template>
    </div>
    <vue-show-more-text
      :text="bookDesc"
      :lines="4"
      additional-container-css="overflow: auto; margin:14px; text-align: left; position: relative; right: 25px; bottom: 12px;"
      @click="change"
    />
  </div>
</div>
</template>

<script>
import '@/assets/css/bestsellers.css'

import vueShowMoreText from 'vue-show-more-text'
import BookCard from './BookCard'

export default {
  components: {
    vueShowMoreText,
    BookCard
  },
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
    index: String,
    bookDesc: String,
    bookGenres: String,
    maxRowWidth: String,
    author: String,
    authorImg: String,
    authorDesc: String,
    comments: String,
    publishers: String,
    bookAbsoluteUrl: String
  },
  computed: {
    limitRowWidth () {
      return 'max-width: ' + this.maxRowWidth
    }
  }
}
</script>

<style>
#book-row {
  display: flex;
  flex-direction: row;
  height: 300px;
  min-height: 300px;
  max-height: 300px;
}

#right-text {
  display: flex;
  flex-direction: column;
}

#book-params {
  display: flex;
  flex-direction: row;
}

#genres-flex {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.colored-genre {
  background-color: lightblue;
  border: 1px solid #5bc0de;
  border-radius: 5px;
  margin: 4px 5px 0 0;
  padding: 0 2px 0 2px;
}
</style>

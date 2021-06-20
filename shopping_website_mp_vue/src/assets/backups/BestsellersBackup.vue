<template>
<div>
  <div id='bestsellers-books-toggle' class='top-divs'>
    <h5><b>You Are Viewing:</b></h5>
    <b-navbar-nav class='d-flex flex-row'>
      <b-link
        v-for="(bookView, index) in bookViews"
        :key="index"
        :to="bookView.to"
      >
          {{ bookView.name }}<span class='ml-1 mr-1' style="border-right: 1px solid gray"></span>
      </b-link>
    </b-navbar-nav>
  </div>
  <div id='nav-view-output' class='top-divs'>
      test
  </div>
    <div class="container" :style="{'margin-bottom': '90px', 'position': 'relative', 'top': '160px'}">
        <h4 class="title">Prime Selections</h4>
        <div class="row">
            <template v-for="(book, index) in booksArr">
                <BookCard
                  :key="index"
                  :price="book.price"
                  :bookImg="book.img"
                  :bookName="book.title"
                  cardMinWidth="230px"
                  cardHeight="85%"
                  :hasShadow="true"
                  :bookDesc="book.desc"
                  :genres="book.genres"
                  cardScale="scale(0.75)"
                  cardTranslateY="translateY(0)"
                />
            </template>
        </div>
    </div>
</div>
</template>

<script>
import '@/assets/css/bestsellers.css'
import BookCard from '@/components/BookCard.vue'
import database from '@/assets/js/booksDatabase.json'

export default {
  components: {
    BookCard
  },
  data () {
    return {
      booksArr: database,
      bookViews: [
        { name: 'Bestsellers', to: '/bestsellers' },
        { name: 'Manga', to: '/manga' },
        { name: 'Light Novels', to: '/light-novels' },
        { name: 'Western Novels', to: '/western-novels' }
      ]
    }
  }
}
</script>

<style>
#bestsellers-books-toggle {
  top: 75px;
  height: 80px;
  background-color: lightblue;
  border: 2px solid #5bc0de;
}

.top-divs {
  position: absolute;
  width: 78%;
  right: 300px;
  border-radius: 5px;
  padding: 10px 0 0 20px;
  text-align: left;
}

#nav-view-output {
  top: 165px;
  height: 40px;
  background-color: lightgray;
  border: 2px solid gray;
  padding-top: 8px;
}
</style>

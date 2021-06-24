<template>
<div class="container">
  <div id='bestsellers-books-toggle' class='cbs-top-divs'>
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
  <div id='nav-view-output' class='cbs-top-divs'>
      Books > Bestsellers
  </div>
  <div id='cbs-popular-books' class='white-div'>
    🟤 Popular Books
  </div>
  <div :style="{'margin-bottom': '90px', 'position': 'relative', 'top': '210px'}">
      <div class="row">
          <template v-for="(book, index) in books">
              <BookCard
                :key="index"
                :price="book.price"
                :bookImg="book.image"
                :bookName="book.title"
                cardMinWidth="230px"
                cardHeight="85%"
                :hasShadow="true"
                :bookDesc="book.sypnosis"
                :genres="book.genres"
                cardScale="scale(0.9)"
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
import axios from 'axios'

export default {
  components: {
    BookCard
  },
  data () {
    return {
      books: [],
      bookViews: [
        { name: 'Bestsellers', to: '/books/bestsellers' },
        { name: 'Manga', to: '/books/manga' },
        { name: 'Light Novels', to: '/books/light-novels' },
        { name: 'Western Novels', to: '/books/western-novels' }
      ]
    }
  },
  mounted () {
    this.getBooks()

    document.title = 'Bestsellers | Code & Chill'
  },
  methods: {
    async getBooks () {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/alphabetical-books/')
        .then(response => {
          for (let book in response.data) {
            if (response.data[book].is_bestseller) {
              this.books.push(response.data[book])
            }
          }
        })

      this.$store.commit('setIsLoading', false)
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

.cbs-top-divs {
  position: absolute;
  width: 90%;
  border-radius: 5px;
  padding: 10px 0 0 20px;
  text-align: left;
  left: 50%;
  transform: translate(-50%);
}

#nav-view-output {
  top: 165px;
  height: 40px;
  background-color: lightgray;
  border: 2px solid gray;
  padding-top: 8px;
}

#cbs-popular-books {
  top: 215px;
  width: 90%;
  height: 40px;
  text-align: left;
  padding-top: 10px;
  padding-left: 20px;
  color: rgb(161, 85, 34);
  font-weight: bold;
  left: 50%;
  transform: translate(-50%);
}

.white-div {
  position: absolute;
  background-color: white;
}

.white-div:before {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
  top: 0;
}

.white-div:after {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
  bottom: 0;
}
</style>

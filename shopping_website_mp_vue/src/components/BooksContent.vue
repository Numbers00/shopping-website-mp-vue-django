<template>
<div style="position: relative; bottom: 40px;" id='bookContent'>
  <div>
    <div id='books-toggle' class='top-divs'>
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
      Books > 
      <span v-if="type === 'Search'">Search ({{query}})</span> 
      <span v-else>{{ bookPath }}</span> 
      <span v-if='genreFilters.length'>{{' > ' + genreFilters}}</span> 
      <span v-if='timeFilters.length'>{{' > ' + timeFilters}}</span> 
      <span v-if='priceFilters.length'>{{' > ' + priceFilters}}</span> 
      <span v-if='ratingFilters.length'>{{' > ' + ratingFilters}}</span> 
      <span v-if='statusFilters.length'>{{' > ' + statusFilters}}</span>
    </div>
    <div id='popular-books' class='white-div d-flex flex-row'>
      🟤 Popular Books
      <b-navbar-nav class='d-flex flex-row ml-2'>
        <b-link
          v-for="(interval, index) in timeIntervals"
          :key="index"
          to="#"
          @click="handleClickTime(interval)"
        >
            {{ interval }}<span class='ml-1 mr-1' style="border-right: 1px solid gray"></span>
        </b-link>
      </b-navbar-nav>
    </div>
    <swiper id='top-cards-swiper' class="swiper" :options="swiperOption">
      <template v-if="type === 'Search'">
        <swiper-slide
          v-for="(book, index) in searchedBooks"
          :key="index"
        >
          <BookCard
            :price="book.price"
            :bookImg="book.image"
            :bookName="book.title"
            cardMinWidth="230px"
            cardHeight="380px"
            cardScale="scale(0.75)"
            cardTranslateY="translateY(0)"
            boxShadow="null"
            :hasShadow="false"
            :hasBlackBackground="true"
            :isLightblue="true"
            :bookDesc="book.sypnosis"
            :bookGenres="book.genres"
            :author="getMatchingAuthor(book).name"
            :authorImg="getMatchingAuthor(book).image"
            :authorDesc="getMatchingAuthor(book).description"
            :publishers="book.publishers"
          />
        </swiper-slide>
      </template>
      <template v-else>
        <swiper-slide
          v-for="(book, index) in relevantBooks.filter(book => {
            if (type == 'Bestseller') return book.is_bestseller
            else return book
          })"
          :key="index"
        >
          <BookCard
            :price="book.price"
            :bookImg="book.image"
            :bookName="book.title"
            cardMinWidth="230px"
            cardHeight="380px"
            cardScale="scale(0.75)"
            cardTranslateY="translateY(0)"
            boxShadow="null"
            :hasShadow="false"
            :hasBlackBackground="true"
            :isLightblue="true"
            :bookDesc="book.sypnosis"
            :bookGenres="book.genres"
            :author="getMatchingAuthor(book).name"
            :authorImg="getMatchingAuthor(book).image"
            :authorDesc="getMatchingAuthor(book).description"
            :publishers="book.publishers"
            :bookAbsoluteUrl="book.get_absolute_url"
          />
        </swiper-slide>
      </template>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
  <div id='price-div' class='white-div'>
    <div class='div-header'>🟤 Price</div>
    <div class="filtering-links">
      <li
        v-for="(link, index) in priceLinks"
        :key="index"
      >
        <a @click="handleClickPrice(link)">
          {{ link }} <span style="color: gray">({{ countPrices(link) }})</span><router-link></router-link>
        </a>
      </li>
      <div class='d-flex w-100 mt-1' id='price-input-div'>
        <span class='mt-1 mr-1'>$</span> <input class='filter-input-tag w-25' type="number" id="price-from" name="price-from" />
        <span class='ml-1 mt-1 mr-1'>- $</span> <input class='filter-input-tag w-25' type="number" id="price-to" name="price-to" />
        <button class='filter-btn'><i class="fa fa-search" aria-hidden="true"></i></button>
      </div>
    </div>
  </div>
  <div id='rating-div' class='white-div'>
    <div class='div-header'>🟤 Rating</div>
    <div class='filtering-links'>
      <li
        v-for="(link, index) in ratingLinks"
        :key="index"
      >
        <a v-if="index === 0" @click="handleClickRating(link)">
          {{ link }} 
          <span style="color: gray" v-if="type === 'Search'">({{ searchedBooks.length }})</span>
          <span style="color: gray" v-else>({{ relevantBooks.length }})</span>
          <router-link></router-link>
        </a>
        <a v-else @click="handleClickRating(link)">
          {{ link }} <span style="color: gray">(0)</span><router-link></router-link>
        </a>
      </li>
      <div class='d-flex w-100 mt-1' id='price-input-div'>
        <span class='mt-1 mr-1'>*</span> <input class='filter-input-tag w-25' type="number" id="rating-from" name="rating-from" />
        <span class='ml-1 mt-1 mr-1'>- *</span> <input class='filter-input-tag w-25' type="number" id="rating-to" name="rating-to" />
        <button class='filter-btn'><i class="fa fa-search" aria-hidden="true"></i></button>
      </div>
    </div>
  </div>
  <div id='status-div' class='white-div'>
    <div class='div-header'>🟤 Book Status</div>
    <div class='filtering-links'>
      <li
        v-for="(link, index) in statusLinks"
        :key="index"
      >
        <a @click="handleClickStatus(link)">
          {{ link }} <span style="color: gray">({{ countStatus(link) }})</span><router-link></router-link>
        </a>
      </li>
    </div>
  </div>
  <div id='main-div'>
    <div id='books-content' class='white-div'>
    <div class='div-header d-flex flex-row'>
      🟤 {{ mainHeader }} ({{ mainHeaderSort }} 
      <span class='ml-1' v-if="this.sortingInverter">
        - Descending)
      </span> 
      <span v-else>)</span>
      <b-navbar-nav class='d-flex flex-row ml-2'>
        <b-link
          v-for="(sortingOption, index) in sortingOptions"
          :key="index"
          to="#"
          @click='handleClickSort(sortingOption)'
        >
            {{ sortingOption }}<span class='ml-1 mr-1' style="border-right: 1px solid gray"></span>
        </b-link>
      </b-navbar-nav>
    </div>
    <div class='book-rows'>
      <template v-if="type === 'Search'">
        <template
          v-for="(book, index) in searchedBooks.filter(book => {
            if (genreFilters == '' && priceFilters == '' && statusFilters == '') {
              return book
            } else {
              if (handleGenreSearch(book.genres) && handlePriceSearch(book.price) && handleStatusSearch(book.status)) {
                return book
              }
            }
          })"
        >
          <BookRow
            :price="book.price"
            :bookImg="book.image"
            :bookName="book.title"
            cardMinWidth="230px"
            cardHeight="380px"
            cardScale="scale(0.7)"
            :hasShadow="false"
            :hasNoBorder="true"
            :index="(index + 1).toString()"
            :bookDesc="book.sypnosis"
            :bookGenres="book.genres"
            :key="index"
            maxRowWidth="98%"
            :author="getMatchingAuthor(book).name"
            :authorImg="getMatchingAuthor(book).image"
            :authorDesc="getMatchingAuthor(book).description"
            :publishers="book.publishers"
            :hasBlackBackground="false"
            :isLightblue="false"
            :bookAbsoluteUrl="book.get_absolute_url"
          />
        </template>
      </template>
      <template v-else>
        <template
          v-for="(book, index) in relevantBooks.filter(book => {
            if (genreFilters == '' && priceFilters == '' && statusFilters == '') {
              return book
            } else {
              if (handleGenreSearch(book.genres) && handlePriceSearch(book.price) && handleStatusSearch(book.status)) {
                return book
              }
            }
          })"
        >
          <BookRow
            :price="book.price"
            :bookImg="book.image"
            :bookName="book.title"
            cardMinWidth="230px"
            cardHeight="380px"
            cardScale="scale(0.7)"
            :hasShadow="false"
            :hasNoBorder="true"
            :index="(index + 1).toString()"
            :bookDesc="book.sypnosis"
            :bookGenres="book.genres"
            :key="index"
            maxRowWidth="98%"
            :author="getMatchingAuthor(book).name"
            :authorImg="getMatchingAuthor(book).image"
            :authorDesc="getMatchingAuthor(book).description"
            :publishers="book.publishers"
            :hasBlackBackground="false"
            :isLightblue="false"
            :bookAbsoluteUrl="book.get_absolute_url"
          />
        </template>
      </template>
    </div>
    <div class='bottom-spacer' />
  </div>
  </div>
  <div id='right-div'>
    <template v-if="type != 'Bestseller'">
      <template v-if="type === 'Search'">
        <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="mangaGenreLinks" :books='searchedBooks' genreOf="Manga Genres" />
        <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="lightNovelsGenreLinks" :books='searchedBooks' genreOf="Light Novel Genres" />
        <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="westernNovelsGenreLinks" :books='searchedBooks' genreOf="Other Genres" />
      </template>
      <template v-else>
        <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="genresList" :books='relevantBooks' genreOf="Genres" />
      </template>
    </template>
    <template v-else>
      <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="mangaGenreLinks" :books='relevantBooks' genreOf="Manga Genres" />
      <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="lightNovelsGenreLinks" :books='relevantBooks' genreOf="Light Novel Genres" />
      <RightGenres @clickGenre='handleClickGenre' :genreFilters="genreFilters" :genresList="westernNovelsGenreLinks" :books='relevantBooks' genreOf="Other Genres" />
    </template>
  <div class='bottom-spacer' />
  </div>
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.min.css'
// import grayBG from '@/assets/css/grayBG.css'

import '@/assets/css/bestsellers.css'
import { lightNovelsGenreLinks, mangaGenreLinks, westernNovelsGenreLinks } from '@/assets/js/genreLinks.js'

import BookCard from '@/components/BookCard'
import BookRow from '@/components/BookRow'
import RightGenres from '@/components/RightGenres'

export default {
  name: 'swiper-example-centered-slides',
  title: 'Centered slides',
  components: {
    Swiper,
    SwiperSlide,
    BookCard,
    BookRow,
    RightGenres
  },
  props: {
    type: String,
    bookPath: String,
    searchedBooks: Array,
    query: String
  },
  data () {
    return {
      authors: [],
      relevantBooks: [],
      lightNovelsGenreLinks,
      mangaGenreLinks,
      westernNovelsGenreLinks,
      mainHeader: 'Books',
      mainHeaderSort: 'Alphabetical',
      sortingInverter: false,
      genreFilters: '',
      priceFilters: '',
      statusFilters: '',
      ratingFilters: '',
      timeFilters: '',
      bookViews: [
        { name: 'Bestsellers', to: '/books/bestsellers' },
        { name: 'Manga', to: '/books/manga' },
        { name: 'Light Novels', to: '/books/light-novels' },
        { name: 'Western Novels', to: '/books/western-novels' },
        { name: 'Scholarly', to: '/books/scholarly' }
      ],
      timeIntervals: [
        'Daily',
        'Weekly',
        'Monthly',
        'Yearly'
      ],
      sortingOptions: [
        'Alphabetical',
        'Price',
        'Rating',
        'Volumes'
      ],
      priceLinks: [
        '$0.00',
        '$0.01 - $1.00',
        '$1.01 - $5.00',
        '$5.01 - $10.00',
        '$10.00+',
      ],
      ratingLinks: [
        '5*',
        '4* - 4.9*',
        '3* - 3.9*',
        '2* - 2.9*',
        '1* - 1.9*',
        '0* - 0.9*',
      ],
      statusLinks: [
        'Pre-Order',
        'Ongoing',
        'Completed',
        'Discontinued'
      ],
      swiperOption: {
        slidesPerView: 5,
        spaceBetween: -100,
        loop: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      }
    }
  },
  mounted () {
    this.getAuthors()
    this.getRelevantBooks()
  },
  computed: {
    normalizedWesternNovelsGenreLinks () {
      return this.westernNovelsGenreLinks.map(elem => {
        elem = elem.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
        return elem
      })
    },
    genresList () {
      return this.type === 'Light Novel' ? this.lightNovelsGenreLinks : this.type === 'Manga' ? this.mangaGenreLinks : this.type === 'Western Novel' ? this.normalizedWesternNovelsGenreLinks : this.normalizedWesternNovelsGenreLinks
    }
  },
  methods: {
    async getAuthors () {

      this.$store.commit('setIsLoading', true)

      await axios
        .get(`/api/v1/alphabetical-authors/`)
        .then(response => {
            this.authors = response.data
        })
        .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        })

      this.$store.commit('setIsLoading', false)
    },
    async getRelevantBooks () {

      this.$store.commit('setIsLoading', true)

      if (this.type === 'Bestseller') {
        await axios
          .get('/api/v1/alphabetical-books/')
          .then(response => {
            for (let book in response.data) {
              if (response.data[book].is_bestseller) {
                this.relevantBooks.push(response.data[book])
              }
            }
          })
          .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
          })
      }
      else {
        await axios
        .get(`/api/v1/alphabetical-book-types/`)
        .then(response => {
          for (let data in response.data) {
            if (this.type === response.data[data].name) {
              this.relevantBooks = response.data[data].books
            }
          }
        })
        .catch(error => {
            console.log(error)
            toast({
                message: 'Something went wrong. Please try again.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        })
      }
      
      console.log(this.relevantBooks)

      this.$store.commit('setIsLoading', false)
    },
    getMatchingAuthor (matchingBook) {
      for (let author in this.authors) {
        for (let book in this.authors[author].books) {
          if (matchingBook.title === this.authors[author].books[book].title) {
            return this.authors[author]
          }
        }
      }
    },
    handleClickGenre (genre) {
      if (this.genreFilters === genre) {
        this.genreFilters = ''
        this.mainHeader = 'Latest Updates'
      } else {
        this.genreFilters = genre
        this.mainHeader = 'Search Results'
      }
    },
    handleGenreSearch (genres) {
      if (this.genreFilters === '') {
        return true
      }
      return (genres !== undefined && genres.includes(this.genreFilters))
    },
    handleClickTime (time) {
      if (this.timeFilters === time) {
        this.timeFilters = ''
      } else {
        this.timeFilters = time
      }
    },
    handleClickSort (sortingOption) {
      if (this.mainHeaderSort === sortingOption) {
        this.sortingInverter = !this.sortingInverter
      }
      else {
        this.sortingInverter = false
      }
      this.mainHeaderSort = sortingOption
      this.handleSortingOption(this.mainHeaderSort)
    },
    handleSortingOption (sortingOption) {
      console.log(sortingOption)
      if (sortingOption === 'Alphabetical') {
        if (this.type === 'Search') this.searchedBooks.sort((a,b) => {
          let x = a['title']
          let y = b['title']
          if (!this.sortingInverter) {
            return ((x < y) ? -1 : ((x > y) ? 1 : 0))
          } else {
            return ((x < y) ? 1 : ((x > y) ? -1 : 0))
          }
        })
        else this.relevantBooks.sort((a,b) => {
          let x = a['title']
          let y = b['title']
          if (!this.sortingInverter) {
            return ((x < y) ? -1 : ((x > y) ? 1 : 0))
          } else {
            return ((x < y) ? 1 : ((x > y) ? -1 : 0))
          }
        })
      }
      else if (sortingOption === 'Price') {
        if (this.type === 'Search') this.searchedBooks.sort((a,b) => {
          let x = a['price']
          let y = b['price']
          if (!this.sortingInverter) {
            return ((x < y) ? -1 : ((x > y) ? 1 : 0))
          } else {
            return ((x < y) ? 1 : ((x > y) ? -1 : 0))
          }
        })
        else this.relevantBooks.sort((a,b) => {
          let x = a['price']
          let y = b['price']
          if (!this.sortingInverter) {
            return ((x < y) ? -1 : ((x > y) ? 1 : 0))
          } else {
            return ((x < y) ? 1 : ((x > y) ? -1 : 0))
          }
        })
      }
    },
    handleClickPrice (price) {
      if (this.priceFilters === price) {
        this.priceFilters = ''
        this.mainHeader = 'Latest Updates'
      } else {
        this.priceFilters = price
        this.mainHeader = 'Search Results'
      }
    },
    handlePriceSearch (price) {
      if (this.priceFilters === '') {
        return true
      }
      let priceSplit = this.priceFilters.split(' - ')
      let limits = []
      for (let i = 0; i < priceSplit.length; i++) {
        limits[i] = parseFloat(priceSplit[i].substring(1).replace('+','').trim())
      }
      if (limits[0] === 0.00) {
        return (price !== undefined && price == limits[0])
      }
      else if (limits[0] === 10.00) {
        return (price !== undefined && price >= limits[0])
      }
      else return (price !== undefined && price >= limits[0] && price <= limits[1])
    },
    handleClickRating (rating) {
      if (this.ratingFilters === rating) {
        this.ratingFilters = ''
      } else {
        this.ratingFilters = rating
      }
    },
    handleClickStatus (status) {
      if (this.statusFilters === status) {
        this.statusFilters = ''
        this.mainHeader = 'Latest Updates'
      } else {
        this.statusFilters = status
        this.mainHeader = 'Search Results'
      }
    },
    handleStatusSearch (status) {
      if (this.statusFilters === '') {
        return 1
      }
      return (status !== undefined && status === this.statusFilters)
    },
    countPrices (price) {
      let priceSplit = price.split(' - ')
      let limits = []
      for (let i = 0; i < priceSplit.length; i++) {
        limits[i] = parseFloat(priceSplit[i].substring(1).replace('+','').trim())
      }
      let count = 0
      if (this.type === "Search") {
        for (let book in this.searchedBooks) {
          if (limits[0] === 0.00) {
            if (this.searchedBooks[book].price == limits[0]) {
              count++
            }
          }
          else if (limits[0] === 10.00) {
            if (this.searchedBooks[book].price >= limits[0]) {
              console.log('limits[0] ' + limits[0])
              count++
            }
          }
          else {
            if (this.searchedBooks[book].price >= limits[0] && this.searchedBooks[book].price <= limits[1]) {
              count++
            }
          }
        }
      }
      else {
        for (let book in this.relevantBooks) {
        if (limits[0] === 0.00) {
            if (this.relevantBooks[book].price == limits[0]) {
              count++
            }
          }
          else if (limits[0] === 10.00) {
            if (this.relevantBooks[book].price >= limits[0]) {
              console.log('limits[0] ' + limits[0])
              count++
            }
          }
          else {
            if (this.relevantBooks[book].price >= limits[0] && this.relevantBooks[book].price <= limits[1]) {
              count++
            }
          }
        }
      }
      return count
    },
    countStatus (status) {
      let count = 0
      if (this.type === "Search") {
        for (let book in this.searchedBooks) {
          if (this.searchedBooks[book].status === status) {
            count++
          }
        }
      }
      else {
        for (let book in this.relevantBooks) {
          if (this.relevantBooks[book].status === status) {
            count++
          }
        }
      }
      return count
    }
  }
}
</script>

<style>
body {
  background-color: #eeeeee;
}
</style>

<style scoped>
.top-divs {
  position: absolute;
  width: 78%;
  right: 300px;
  border-radius: 5px;
  padding: 10px 0 0 20px;
  text-align: left;
}

#books-toggle {
  top: 75px;
  height: 80px;
  background-color: lightblue;
  border: 2px solid #5bc0de;
}

#nav-view-output {
  top: 165px;
  height: 40px;
  background-color: lightgray;
  border: 2px solid gray;
  padding-top: 8px;
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

#popular-books {
  top: 215px;
  width: 78%;
  height: 40px;
  right: 300px;
  text-align: left;
  padding-top: 10px;
  padding-left: 20px;
  color: rgb(161, 85, 34);
  font-weight: bold;
}

#popular-books:before {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  top: 0px;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
}

#popular-books:after {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  top: 40px;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
}

#top-cards-swiper {
  top: 240px;
  width: 78%;
  position: absolute;
  right: 300px;
  height: 360px;
}

.swiper-slide {
  width: 60%;
  transform: translate(0, -50px);
}

.swiper-slide:nth-child(2n) {
  width: 40%;
}

.swiper-slide:nth-child(3n) {
  width: 20%;
}

#books-content {
  background-color: white;
  width: 60%;
  height: auto;
  position: absolute;
  right: 300px;
  top: 605px;
}

#books-content:before {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
}

.div-header {
  padding-top: 10px;
  padding-left: 20px;
  color: rgb(161, 85, 34);
  font-weight: bold;
  text-align: left;
}

.div-header:after {
  content: "";
  background: rgb(161, 85, 34);
  width: 100%;
  height: 4px;
  border-radius: 5px;
  position: absolute;
  right: 0;
  top: 40px;
}

#price-div {
  top: 605px;
  left: 50px;
  width: 240px;
  height: 220px;
}

.filtering-links {
  text-align: left;
  padding-top: 20px;
  padding-left: 20px;
}

.book-rows {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

.book-rows>* {
  flex: 1 1 240px;
}

.book-rows:nth-child(odd) {
  padding-left: 20px;
}

.filter-input-tag {
  background-color: #eeeeee;
}

.filter-btn {
  position: absolute;
  right: 20px;
}

#rating-div {
  top: 865px;
  left: 50px;
  width: 240px;
  height: 245px;
}

#status-div {
  top: 1150px;
  left: 50px;
  width: 240px;
  height: auto;
  padding-bottom: 10px;
}

#right-div {
  display: flex;
  flex-direction: column;
  top: 75px;
  right: 50px;
  width: 210px;
  height: auto;
  position: absolute;
}

.genres-div {
  position: relative;
  height: auto;
  margin-bottom: 30px;
  padding-bottom: 10px;
}

.bottom-spacer {
  min-height: 120px;
  height: 120px;
  width: 100px;
  position: absolute;
}
</style>

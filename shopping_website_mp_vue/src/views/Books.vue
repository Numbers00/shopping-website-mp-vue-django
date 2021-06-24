<template>
<body>
    <!-- ===============================================-->
    <!--    Main Content-->
    <!-- ===============================================-->
    <main class="main" id="top">
      <section class="py-0" id="home">
        <div
          class="bg-holder d-none d-md-block"
          style="
            background-image: url(https://images.pexels.com/photos/1470162/pexels-photo-1470162.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940);
            background-position: right bottom;
            background-size: contain;
          "
        ></div>
        <!--/.bg-holder-->

        <div
          class="bg-holder d-block d-md-none"
          style="
            background-image: url(assets/img/illustrations/hero-bg.png);
            background-position: right top;
            background-size: contain;
          "
        ></div>
        <!--/.bg-holder-->

        <div class="container">
          <div class="row align-items-center min-vh-md-75">
            <div class="col-md-7 col-lg-6 py-6 text-sm-start text-center">
              <h1
                class="mt-6 mb-sm-4 display-4 fw-semi-bold lh-sm fs-4 fs-lg-6 fs-xxl-7"
              >
                Treat yourself.
                <br class="d-block d-lg-none d-xl-block" />Take a break.
                <br class="d-block d-lg-none d-xl-block" />Have a book.
              </h1>
              <p class="mb-4 fs-1">
                If you're a passionate bibliophile like us (or just want to take a rest and immerse yourself in good reads), Code&Chill got your back! Feel free to browse our selections.
              </p>
              <div class="pt-3">
                <form>
                  <a
                    href="#category_books"
                    class="book-btn"
                    style="box-shadow: 3px 3px 3px gray; text-decoration: none"
                    >Browse Books &#8594;</a
                  >
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============================================-->
      <!-- <section> begin ============================-->
      <section>
        <div class="container" id="category_books">
          <div class="row justify-content-center">
            <div class="col-auto mb-5 mb-md-7" id="category-card">
              <h1 class="fw-semi-bold text-primary">
                Our <span class="text-1100">resources</span>
              </h1>
            </div>
          </div>
          <div class="container">
            <div class="row">
              <div
                class="col-md-3 mb-3 mb-lg-0 text-center"
                style="padding: 10px"
                id="book-category"
              >
                <a
                  style="text-decoration: none; color: inherit"
                  @click="$router.push({ name: 'Scholarly' })"
                >
                  <div class="px-0 px-lg-3">
                    <img
                      class="img-fluid mb-4"
                      src="https://icons.iconarchive.com/icons/ampeross/smooth/128/Apple-Books-icon.png"
                      width="100"
                      alt="..."
                      id="hover-img"
                    />
                    <h3 class="h5 mb-4 font-base">Scholarly</h3>
                    <p class="lh-lg">
                      Our collection of academic books and references are
                      selectively curated for your needs in Computer Science.
                    </p>
                  </div>
                </a>
              </div>
              <div
                class="col-md-3 mb-3 mb-lg-0 text-center"
                style="padding: 10px"
                id="book-category"
              >
                <a
                  style="text-decoration: none; color: inherit"
                  @click="$router.push({ name: 'WesternNovels' })"
                >
                  <div class="px-0 px-lg-3">
                    <img
                      class="img-fluid mb-4"
                      src="https://icons.iconarchive.com/icons/icons8/windows-8/128/Printing-Books-icon.png"
                      width="100"
                      alt="..."
                      id="hover-img"
                    />
                    <h3 class="h5 mb-4 font-base">Western Novels</h3>
                    <p class="lh-lg">
                      Delve into a world that would keep you imagination going
                      with our editors' choice of novels from best-selling
                      authors.
                    </p>
                  </div>
                </a>
              </div>
              <div
                class="col-md-3 mb-3 mb-lg-0 text-center"
                style="padding: 10px"
                id="book-category"
              >
                <a
                  style="text-decoration: none; color: inherit"
                  @click="$router.push({ name: 'LightNovels' })"
                >
                  <div class="px-0 px-lg-3">
                    <img
                      class="img-fluid mb-4"
                      src="https://icons.iconarchive.com/icons/iconsmind/outline/128/Books-2-icon.png"
                      width="100"
                      alt="..."
                      id="hover-img"
                    />
                    <h3 class="h5 mb-4 font-base">Light Novels</h3>
                    <p class="lh-lg">
                      Not only do we offer from your usual academic shelf, but
                      we also reserve a special spot for light novel enthusiasts.
                    </p>
                  </div>
                </a>
              </div>
              <div
                class="col-md-3 mb-3 mb-lg-0 text-center"
                style="padding: 10px"
                id="book-category"
              >
                <a style="text-decoration: none; color: inherit" @click="$router.push({ name: 'Manga' })">
                  <div class="px-0 px-lg-3">
                    <img
                      class="img-fluid mb-4"
                      src="https://icons.iconarchive.com/icons/ncrow/mega-pack-2/256/Manga-Studio-FX-4-icon.png"
                      width="100"
                      alt="..."
                      id="hover-img"
                    />
                    <h3 class="h5 mb-4 font-base">Manga</h3>
                    <p class="lh-lg">
                      And not only that, but we cater to manga enthusiasts as well, manga,
                      manhwa, manhua, we have you covered with our top picks in each category.
                    </p>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>
        <!-- end of .container-->
      </section>
      <!-- <section> close ============================-->
      <!-- ============================================-->

      <section id="libraries">
        <div
          class="bg-holder"
          style="
            background-position: left bottom;
            background-size: contain;
          "
          :style="{'background-image': 'url(' + require('@/assets/img/illustrations/libraries-bg.png') + ')'}"
        ></div>
        <!--/.bg-holder-->

        <div class="container">
          <div class="row g-xl-0 align-items-center">
            <div class="col-md-5 col-lg-7 text-xl-center">
              <img
                class="img-fluid mb-5 mb-md-0"
                src="https://images.pexels.com/photos/768125/pexels-photo-768125.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
                width="620"
                alt=""
                style="border-radius: 10px"
              />
            </div>
            <div
              class="col-md-7 col-lg-4 text-center text-md-start offset-lg-1 offset-xxl-0"
            >
              <h1 class="fw-semi-bold text-primary">
                Our <span class="text-1100">best-sellers</span>
              </h1>
              <p class="pt-3 lh-lg">
                We know you're busy with your personal errands. That is why we
                created this special section that saves you time and easily
                shows you books that have consistently been at the top of the
                list across the world, all in one place for you to choose from!
              </p>
              <div class="py-3">
                <a
                  @click="$router.push({ name: 'Bestsellers' })"
                  style="text-decoration: none; color: inherit"
                >
                  <button
                    class="book-btn"
                    style="box-shadow: 3px 3px 3px gray; text-decoration: none"
                  >
                    Learn More
                  </button>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============================================-->
      <!-- <section> begin ============================-->
      <section class="py-8" id="books">
        <div class="container" id="best-seller">
          <div class="row justify-content-center">
            <div class="col-md-8 col-lg-6 text-center mb-7">
              <h1 class="fw-semi-bold text-primary">
                Best<span class="text-1100"> seller books</span>
              </h1>
            </div>
            <div class="col-lg-9">
              <div class="accordion" id="accordionExample">
                <template v-for="(book, index) in books">
                  <BookAccordion
                    v-if="book.is_bestseller"
                    :isShow="index == 0 ? 'show' : ''"
                    :accNum="index.toString()"
                    :bookName="book.title"
                    :author="getMatchingAuthor(book).name"
                    :price="book.price"
                    :bookImg="book.image"
                    copiesSold=""
                    :bookDesc="book.sypnosis"
                    :key="index"
                    :bookGenres="book.genres"
                    :authorImg="getMatchingAuthor(book).image"
                    :authorDesc="getMatchingAuthor(book).description"
                    :publishers="book.publishers"
                    :bookAbsoluteUrl="book.get_absolute_url"
                  />
                </template>
              </div>
            </div>
            <div class="col-lg-12 d-flex justify-content-center">
              <a @click="$router.push({ name: 'CardBestsellers' })">
                <button class="book-btn" type="submit">Find More</button>
              </a>
            </div>
          </div>
        </div>
        <!-- end of .container-->
      </section>
      <!-- <section> close ============================-->
      <!-- ============================================-->

      <section class="py-6">
        <div
          class="bg-holder"
          style="
            background-position: right bottom;
            background-size: contain;
          "
          :style="{'background-image': 'url(' + require('@/assets/img/illustrations/cta-bg.png') + ')'}"
        ></div>
        <!--/.bg-holder-->
      </section>
    </main>
    <!-- ===============================================-->
    <!--    End of Main Content-->
    <!-- ===============================================-->

    <link
      href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800&amp;display=swap"
      rel="stylesheet"
    />
</body>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

import BookAccordion from '@/components/BookAccordion.vue'

export default {
  components: {
    BookAccordion
  },
  data () {
    return {
      books: [],
      authors: []
    }
  },
  mounted () {
    this.getBooks()
    this.getAuthors()

    document.title = 'Books | Code & Chill'
  },
  methods: {
    async getBooks () {
      await axios
        .get(`/api/v1/alphabetical-books/`)
        .then(response => {
            this.books = response.data
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
    },
    async getAuthors () {
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
    },
    getMatchingAuthor (matchingBook) {
      for (let author in this.authors) {
        for (let book in this.authors[author].books) {
          if (matchingBook.title === this.authors[author].books[book].title) {
          return this.authors[author]
        }
        }
      }
    }
  },
  created () {
    const polyfill = document.createElement('script')
    polyfill.setAttribute('src', '//polyfill.io/v3/polyfill.min.js?features=window.scroll')
    document.head.appendChild(polyfill)
  }
}
</script>

<style scoped src='@/assets/css/books.css'>
body {
  background-color: white !important;
}
</style>

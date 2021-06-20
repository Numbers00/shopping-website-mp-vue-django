<template>
<div class='genres-div white-div'>
  <div class='div-header'>🟤 {{ genreOf }}</div>
  <div class='filtering-links'>
    <ul>
    <template
      v-for="(link, index) in genresList"
    >
    <li :key="index">
      <a @click='clickGenre(link)' :class="{'is-underlined': link === genreFilters}">
        {{ link }} <span style="color: gray">({{ countGenre(link) }})</span><router-link></router-link>
      </a>
    </li>
    </template>
    </ul>
  </div>
</div>
</template>

<script>
export default {
  props: {
    books: [],
    genreOf: String,
    genresList: Array,
    genreFilters: String
  },
  watch: {
    genreFilters () {
      console.log(this.genreFilters)
    }
  },
  methods: {
    clickGenre (genre) {
      this.$emit('clickGenre', genre)
    },
    countGenre (genre) {
      let count = 0
      for (let book in this.books) {
        if (this.books[book].genres.includes(genre)) {
          count++
        }
      }
      return count
    }
  }
}
</script>

<style>
.is-underlined {
  text-decoration: underline;
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

.filtering-links {
  text-align: left;
  padding-top: 20px;
  padding-left: 20px;
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

.genres-div {
  position: relative;
  height: auto;
  margin-bottom: 30px;
  padding-bottom: 10px;
}
</style>

<template>
<div
  class="accordion-item mb-5 border border-x-0 border-bottom-0 border-200"
>
  <div class="accordion-header" id="heading6">
    <div
      class="accordion-button collapsed"
      role="button"
      data-bs-toggle="collapse"
      :data-bs-target="'#collapse' + accNum"
      aria-expanded="true"
      :aria-controls="'collapse' + accNum"
    >
      <div class="row w-100 justify-content-center">
        <div class="col-sm-6 font-base">
          <span class="mb-0 fw-bold text-start text-1200"
            >{{bookName}}</span
          >
          <p class="my-2">{{author}}</p>
        </div>
        <div class="col-8 col-sm-4">
          <div class="rating">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
          </div>
        </div>
        <div class="col-4 col-sm-2 text-end">
          <h5 class="mb-0 font-base fw-bold">${{price}}</h5>
        </div>
      </div>
    </div>
  </div>
  <div
    :class="'accordion-collapse collapse shadow-lg ' + isShown"
    :id="'collapse' + accNum"
    :aria-labelledby="'heading' + accNum"
    data-bs-parent="#accordionExample"
  >
    <div class="accordion-body">
      <div class="row justify-content-center-center">
        <div class="col-12 col-sm-3">
          <img
            class="img-fluid d-block mx-auto mx-sm-0"
            :src="bookImg"
            width="130"
            alt="..."
          />
        </div>
        <div
          class="col-12 col-sm-9 mt-4 mt-sm-0 d-sm-block d-flex flex-column"
        >
          <ul>
            <li class="fw-semi-bold text-black">
              Copies Sold: 240 million
            </li>
          </ul>
          <p style="text-align: justify">
            {{bookDesc}}
          </p>
        </div>
        {{ comments }}
        <a @click="$router.push({ path: '' + bookAbsoluteUrl, append: false})"><button class="buy-btn">Buy</button></a>
      </div>
    </div>
  </div>
</div>
</template>

<script>

export default {
  props: {
    isShown: String,
    accNum: String,
    bookName: String,
    author: String,
    price: String,
    bookImg: String,
    copiesSold: String,
    bookDesc: String,
    bookGenres: String,
    authorImg: String,
    authorDesc: String,
    comments: String,
    publishers: String,
    bookAbsoluteUrl: String
  }
}
</script>

<style scoped src='@/assets/css/books.css'>
</style>

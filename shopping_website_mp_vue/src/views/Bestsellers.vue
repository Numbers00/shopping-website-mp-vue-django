<template>
<div>
<BooksContent type="Bestseller" />
</div>
</template>

<script>
import BooksContent from '@/components/BooksContent'

export default {
  components: {
    BooksContent
  },
  mounted () {
    document.title = 'Bestsellers | Code & Chill'
  }
}
</script>

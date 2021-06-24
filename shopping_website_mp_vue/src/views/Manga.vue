<template>
<BooksContent type="Manga" bookPath="Manga" />
</template>

<script>
import BooksContent from '@/components/BooksContent'

export default {
  components: {
    BooksContent
  },
  mounted () {
    document.title = 'Manga | Code & Chill'
  }
}
</script>

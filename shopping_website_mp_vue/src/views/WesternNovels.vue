<template>
<BooksContent type="Western Novel" bookPath="Western Novels" />
</template>

<script>
import BooksContent from '@/components/BooksContent'

export default {
  components: {
    BooksContent
  },
  mounted () {
    document.title = 'Western Novels | Code & Chill'
  }
}
</script>

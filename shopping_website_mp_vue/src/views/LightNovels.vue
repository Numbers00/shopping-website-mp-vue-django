<template>
<BooksContent type="Light Novel" bookPath="Light Novels" />
</template>

<script>
import BooksContent from '@/components/BooksContent'

export default {
  components: {
    BooksContent
  },
  mounted () {
    document.title = 'Light Novels | Code & Chill'
  }
}
</script>

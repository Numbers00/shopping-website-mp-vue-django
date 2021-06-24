<template>
<BooksContent type="Scholarly" bookPath="Scholarly" />
</template>

<script>
import BooksContent from '@/components/BooksContent'

export default {
  components: {
    BooksContent
  },
  mounted () {
    document.title = 'Scholarly | Code & Chill'
  }
}
</script>

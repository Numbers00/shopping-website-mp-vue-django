<template>
<BooksContent :searchedBooks="books" type="Search" :query="query" bookPath="Scholarly" />
</template>

<script>
import axios from 'axios'
import BooksContent from '@/components/BooksContent.vue'

export default {
    name: 'Search',
    components: {
        BooksContent
    },
    data () {
        return {
            books: [],
            query: ''
        }
    },
    mounted () {
        document.title = 'Search | Code & Chill'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch () {
            this.$store.commit('setIsLoading', true)

            console.log(this.query)

            await axios
                .post('/api/v1/books/search/', {'query': this.query})
                .then(response => {
                    this.books = response.data
                })
                .catch(err => {
                    console.log(err)
                })

            console.log(this.books)
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

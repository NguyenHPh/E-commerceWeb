<template>
    <div id="content" class="pl-5">
        <div>Search for "{{ query }}"</div>
        <span class="result-quantity">displaying {{ displayqtt }} results</span>
        <div v-show = "displayqtt == 0" class="text-center" style="font-size: 25px;">
            No product founded
        </div>
        <div v-show = "displayqtt > 0" class="results mx-auto col-lg-10">
            <ProductBox 
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
            />
        </div>
        
    </div>
</template>


<script>
import axios from 'axios'
import ProductBox from '../components/ProductBox.vue'
export default {
    name: 'Search',
    components:{
        ProductBox
    },
    data() {
        return{
            products: {},
            displayqtt: 0,
            query: ''

        }
    },
    mounted() {
        document.title = 'Search'
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods:{
        async performSearch() {
            this.$store.commit('setIsLoading', true)
            const search_query = this.query
            await axios
                .get(`/api/v1/search/${search_query}`)
                .then(response => {
                    this.products = response.data
                    this.displayqtt = this.products.length
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
    .results{

    }
</style>
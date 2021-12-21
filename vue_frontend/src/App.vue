<template>
<div>
     <AppHeader v-bind:cartTotalLength="cartTotalLength"/>
     <NavBar />
     <Rated />
     <router-view/>
     <AppFooter />
     
</div>
</template>



<style>

@import './assets/styles/rated.css';
@import './assets/styles/header.css';
@import './assets/styles/nav-bar.css';
@import './assets/styles/footer.css';

</style>


<script>
  import axios from 'axios'
  //import '../node_modules/bulma';
  import Rated from "./components/Rated.vue";
  import NavBar from "./components/nav-bar.vue";
  import AppFooter from "./components/AppFooter.vue";
  import AppHeader from './components/AppHeader.vue';
  export default {
    data() {
      return {
        cart: {
          items: [],
          length: 0,
          categories: []
        }
      }
    },
    components:{
          AppHeader,
          AppFooter,
          NavBar, 
          Rated
    },
    beforeCreate() {
      this.$store.commit('initializeStore')
      const token = this.$store.state.token

      if (token) {
          axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
          axios.defaults.headers.common['Authorization'] = ""
      }

    },
    mounted() {
      this.cart = this.$store.state.cart
    },
    methods:{

    },
    computed: {
      cartTotalLength() {
          let totalLength = 0

          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }

          return totalLength
      }
    }
  }
   
</script>

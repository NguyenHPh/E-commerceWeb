<template>
<div>
     <AppHeader v-bind:cartTotalLength="cartTotalLength"/>
     <NavBar />
     <Rated />
    <div class="is-loading-bar" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>
    <router-view/>
     <AppFooter />
     

    

     
</div>
</template>


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




<style>
  @import '../node_modules/bulma';
  @import './assets/styles/rated.css';
  @import './assets/styles/header.css';
  @import './assets/styles/nav-bar.css';
  @import './assets/styles/footer.css';

  .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }
  .lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #2c7328;
    border-color: #2c7328 transparent #2c7328 transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }
  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .is-loading-bar {
    height: 0;
    overflow: hidden;
    text-align: center;

    -webkit-transition: all 0.3s;
    transition: all 0.3s;
  }

  .is-loading {
      height: 80px;
  }
</style>

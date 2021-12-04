<template>
<div>
     <AppHeader />
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
  import Rated from "./components/Rated.vue";
  import NavBar from "./components/nav-bar.vue";
  import AppFooter from "./components/AppFooter.vue";
  import AppHeader from './components/AppHeader.vue';
  export default {
    data() {
      return {
      }
    },
    components:{
        AppHeader,
        AppFooter,
        NavBar, 
        Rated
    }
  }
</script>

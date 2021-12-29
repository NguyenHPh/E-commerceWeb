
<template>
<div>
    <div class="container-fluid mx-auto category-intro text-center pt-5 pb-2">
        <div class="text-center mb-3" v-show="categoryall">
            <h2>All dog food</h2>
        </div>
        <div v-show= "!categoryall">
            <h2>{{ category.name }}</h2>
            <div class="row readmore" >
                <p class="col-9 mx-auto mt-3">{{ category.description }}</p>
                <span class="readmore-link"><i class="icon-up-down fas fa-caret-down mr-2"></i></span>
            </div>
        </div>
    </div>
    <div class="mt-5">
        <div class="container-base d-md-flex align-items-stretch mx-auto">
      <!-- Page Content  -->
            <nav id="sidebar" class="px-4">
                <div class="text-center">
                    <h4>Filter results:</h4>
                    <ul class="list-unstyled components mb-1 mt-3 px-4 py-4 text-left">
                      <li>
                        <a href="#pageSubmenu1" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle pt-2 pb-3 d-block">by type</a>
                        <ul class="collapse list-unstyled" id="pageSubmenu1">
                            <li>
                                <a href="/collections/wet-dog-food" class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterCategory[0] }"></i>wet food
                                </a>
                            </li>
                            <li>
                                <a href="/collections/dry-dog-food" class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterCategory[1] }"></i> dry food
                                </a>
                            </li>
                            <li>
                                <a href="/collections/range-natural-hand-baked-treats" class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterCategory[2] }"></i>dog treats
                                </a>
                            </li>
                        </ul>
                      </li>
                      <li>
                        <a href="#pageSubmenu2" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle py-2 d-block">by lifestage</a>
                        <ul class="collapse list-unstyled" id="pageSubmenu2">
                            <li>
                                <span class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterLifeStage[0] }" @click="loadLifeStage(0)"></i>puppy
                                </span>
                            </li>
                            <li>
                                <span class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterLifeStage[1] }" @click="loadLifeStage(1)"></i> adult
                                </span>
                            </li>
                            <li>
                                <span class="mb-3 d-flex">
                                    <i class="fas mr-2" v-bind:class="{ 'fa-check':filterLifeStage[2] }" @click="loadLifeStage(2)"></i>senior 
                                </span>
                            </li>
                        </ul>
                      </li>
                    </ul>
                </div>
            </nav>

            <div id="content" class="pl-5">
                <span class="result-quantity">displaying {{ displayqtt }} results</span>
                <ProductBox 
                    v-for="product in dproducts"
                    v-bind:key="product.id"
                    v-bind:product="product"
                />
            </div>
        </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'
import ProductBox from '../components/ProductBox.vue'

export default {
    name: 'Product',
    components:{
        ProductBox
    },
    data() {
        return{
            products: {},
            dproducts: {},
            category: '',
            categoryall: true,
            displayqtt: 0,
            filterCategory: [false, false, false],
            filterLifeStage: [false, false, false]
        }
    },
    mounted() {
        document.title = 'Product';
        this.getProduct();
        this.loadMore();
    },
    methods:{

        async getProduct(){
                this.$store.commit('setIsLoading', true)


                const category_slug = this.$route.params.category_slug

                if (category_slug == "all"){
                    axios.get(`/api/v1/collections/all`)
                            .then(response => {
                                this.products = response.data
                                this.dproducts = this.products
                                this.displayqtt = this.products.length
                            })
                            .catch(err =>{
                                console.log(err)
                            })
                }
                else{
                    await axios.get(`/api/v1/collections/${category_slug}/`)
                            .then(response => {
                                this.category = response.data
                                if (this.category.name == "treats"){
                                    this.filterCategory[2] = true
                                }
                                if (this.category.name == "dry food"){
                                    this.filterCategory[1] = true
                                }
                                if (this.category.name == "wet food"){
                                    this.filterCategory[0] = true
                                }
                            })
                            .catch(err =>{
                                console.log(err)
                            })

                    await axios.get(`/api/v1/collections/${category_slug}/all`)
                            .then(response => {
                                this.products = response.data
                                this.categoryall = false
                                this.displayqtt = this.products.length
                            })
                            .catch(err =>{
                                console.log(err)
                            })
                }
                this.dproducts = this.products
                console.log(this.products)
                this.$store.commit('setIsLoading', false)
        },

        loadMore(){
            var fullHeight = function() {

                $('.js-fullheight').css('height', $(window).height());
                $(window).resize(function(){
                    $('.js-fullheight').css('height', $(window).height());
                });

            };
            fullHeight();

            $(".readmore-link").click( function(e) {
              // record if our text is expanded
              var isExpanded =  $(e.target).hasClass("expand");
              
              //close all open paragraphs
              $(".readmore.expand").removeClass("expand");
              $(".readmore-link.expand").removeClass("expand");
              $(".icon-up-down").removeClass("fa-caret-up");


              // if target wasn't expand, then expand it
              if (!isExpanded){
                $( e.target ).parent( ".readmore" ).addClass( "expand" );
                $(e.target).addClass("expand");
                $(".icon-up-down").addClass("fa-caret-up");
              } 
            });

        },
        loadLifeStage(type){
            this.filterLifeStage[type] = !this.filterLifeStage[type]
            let dLifeStage = []
            if (this.filterLifeStage[0]){
                dLifeStage.push("puppy")
            }
            if (this.filterLifeStage[1]){
                dLifeStage.push("adult")
            }
            if (this.filterLifeStage[2]){
                dLifeStage.push("senior")
            }
            console.log(dLifeStage)
            this.dproducts = this.products.filter(product => dLifeStage.includes(product.lifeStage))
            this.displayqtt = this.dproducts.length
        }
    },
    computed:{

    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
</style>
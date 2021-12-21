<template>
<div>
    <div class="container-fluid mx-auto category-intro text-center pt-5 pb-2">
        <div class="text-center mb-3" v-if="categoryall">
            <h2>All dog food</h2>
        </div>
        <div v-else>
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
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas fa-check mr-2"></i>wet food
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i> dry food
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i>dog treats
                                </a>
                            </li>
                        </ul>
                      </li>
                      <li>
                        <a href="#pageSubmenu2" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle py-2 d-block">by lifestage</a>
                        <ul class="collapse list-unstyled" id="pageSubmenu2">
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas fa-check mr-2"></i>puppy
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i> adult
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i>senior 
                                </a>
                            </li>
                        </ul>
                      </li>
                    </ul>
                </div>
            </nav>

            <div id="content" class="pl-5">
                <span class="result-quantity">displaying {{ displayqtt }} results</span>
                <div class="product py-3" v-for="product in products" :key="product.id">
                    <div class="row">
                        <div class="col-10 col-lg-4 mx-auto pt-4">
                            <img v-bind:src="product.get_image" alt="product" class="img-fluid w-100">
                        </div>
                        <div class="col-10 col-lg-8 pt-4 mx-auto">
                            <p class="mb-1">{{ product.special_range }}</p>
                            <h3>
                                <router-link v-bind:to="product.get_absolute_url">{{ product.brief_component }}</router-link>
                            </h3>
                            <p class="age">available in: {{ product.lifeStage }}</p>
                            <p>{{ product.rating }} <span class="review">(based on 13 reviews)</span></p>
                            <div class="row text-center" >
                                <div class="col-4" v-for="tray in product.get_trays">
                                    <div>
                                        <div class="mx-auto product-frame">
                                            <span class="product-size d-block font-weight-bold pt-3">x{{ tray[1] }}</span>
                                            <span class="product-pack-type d-block py-1">Trays</span>
                                            <span class="best-price-label d-block font-italic py-1">best value</span>
                                        </div>
                                        <p class="price-product text-center font-weight-bold mt-2">£{{ tray[0]*tray[1] }}</p>
                                        <p class="price-per-tray text-center font-italic"><span>£{{ tray[0] }}</span> per tray</p>
                                    </div>    
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="buy-detail">
                        <div class="add-to-cart text-right mt-2">
                            <button type="button" class="d-inline-block px-4 py-2">
                                buy now <i class="fas fa-arrow-right pl-2"></i>                
                            </button>
                        </div>
                        <div class="text-right">
                            <span class="d-inline-block view-product-detail mt-2">
                                <router-link v-bind:to="product.get_absolute_url">view full product detail</router-link>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'Product',
    data() {
        return{
            products: {},
            category: '',
            categoryall: true,
            displayqtt: 0
        }
    },
    mounted() {
        document.title = 'Product';

        this.getProduct();

        this.loadMore();
    },
    methods:{

        async getProduct(){
                const category_slug = this.$route.params.category_slug

                if (category_slug == "all"){
                    axios.get(`/api/v1/collections/all`)
                            .then(response => {
                                this.products = response.data
                                this.displayQuantity()
                            })
                            .catch(err =>{
                                console.log(err)
                            })
                }
                else{
                    await axios.get(`/api/v1/collections/${category_slug}/`)
                            .then(response => {
                                this.category = response.data
                                this.categoryall = true
                            })
                            .catch(err =>{
                                console.log(err)
                            })

                    await axios.get(`/api/v1/collections/${category_slug}/all`)
                            .then(response => {
                                this.products = response.data
                                this.categoryall = false
                                this.displayQuantity()
                                console.log(this.products)
                            })
                            .catch(err =>{
                                console.log(err)
                            })
                }
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

        }
    },
    computed:{
        displayQuantity(){
            this.displayqtt = this.products.length
        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
</style>
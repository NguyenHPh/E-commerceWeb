<template>
<div>
    <div class="container-fluid mx-auto category-intro text-center pt-5 pb-2">
        <div class="text-center mb-3" v-if="categoryall">
            <h2>All dog food</h2>
        </div>
        <div v-else>
            <h2>natural wet dog food</h2>
            <div class="row readmore" >
                    <p class="col-9 mx-auto mt-3">Our range of complete and complementary wet dog food has been designed with sensitive tummies in mind, so your canine companion can continue being happy and healthy. Each wet dog food recipe is packed full of natural ingredients gently steamed to retain as much natural flavour and goodness as possible.  <br>

                    Our complete grain free wet dog food range is made using natural ingredients with added vitamins and minerals to support your dog’s overall health and wellbeing. Choose from mouth-watering recipes, each including 75% salmon, lamb, duck, beef or turkey to make mealtimes even more delicious.
                    <br><br>
                    Our complete range of wet dog food with brown rice recipes provides a delicious balanced meal. These are packed with wholesome natural ingredients like ocean fish, chicken, liver, and tripe, along with healthy vegetables and wholegrain brown rice for a satisfying and delicious dish for your dog.
                    <br><br>
                    You can even introduce your new pup to our complete puppy recipes specially designed with puppies from two months and over in mind. Or, for more senior dogs our range of senior complete wet meals are perfect to help give your dog the support they need.
                    <br><br>
                    Fancy making dinner times extra-special? Our range of National Trust wet dog food gourmet recipes is here to help. Ingredients like venison, wild boar, green beans, and apricot all feature and are sure to be a hit in the bowl. When you buy from the range, you’ll also be helping to support the work done by the National Trust to care for many of the places we love to explore with our four-legged friends.
                    <br><br>
                    If you prefer to tailor mealtimes, our range of just complementary recipes is the answer! Use as a tasty topper, or as part of a balanced diet for your dog. Our complementary recipes are available in a whole host of scrumptious ingredients including beef, duck, and chicken.
                    <br><br>
                    Made in Devon, our natural, good quality wet dog food is available from as little as £1.24 per tray for our complementary recipes and from only £1.90 per tray for our complete wet dog food range.
                    <br><br>
                    Not sure which recipe to try? Our starter packs contain a selection of recipes to help mix up mealtimes for your canine companion.</p>
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
                <span class="result-quantity">displaying 50 results</span>
                <div class="product py-3" v-for="product in products" :key="product.id">
                    <div class="row">
                        <div class="col-10 col-lg-4 mx-auto pt-4">
                            <img v-bind:src="product.get_image" alt="product" class="img-fluid w-100">
                        </div>
                        <div class="col-10 col-lg-8 pt-4 mx-auto">
                            <p>{{ product.special_range }}</p>
                            <h3>
                                <router-link v-bind:to="product.get_absolute_url">personalised birthday box for dogs</router-link>
                            </h3>
                            <p class="age">available in: {{ product.lifeStage }}</p>
                            <p>{{ product.rating }} <span class="review">(based on 13 reviews)</span></p>
                            <div class="row text-center">
                                <div class="col-4">
                                    <div class="mx-auto product-frame">
                                        <span class="product-size d-block font-weight-bold pt-3">x36</span>
                                        <span class="product-pack-type d-block py-1">Trays</span>
                                        <span class="best-price-label d-block font-italic py-1">best value</span>
                                    </div>
                                    <p class="price-product text-center font-weight-bold mt-2">£51.25</p>
                                    <p class="price-per-tray text-center font-italic"><span>£1.42</span> per tray</p>
                                </div>
                                <div class="col-4">
                                    <div class="mx-auto product-frame">
                                        <span class="product-size d-block font-weight-bold pt-3">x18</span>
                                        <span class="product-pack-type d-block py-1">Trays</span>
                                    </div>
                                    <p class="price-product text-center font-weight-bold mt-2">£26.30</p>
                                    <p class="price-per-tray text-center font-italic"><span>£1.46</span> per tray</p>
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
            categoryall: true
        }
    },
    mounted() {
        document.title = 'Product';

        this.getProduct();

        (function($) {
            "use strict";
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

        })(jQuery);  
    },
    methods:{
        categoryCheck(category){
            if (category != "all"){
                this.categoryall = false
            }
        },
        getProduct(){
            const category_slug = this.$route.params.category_slug

            axios
                .get(`/api/v1/collections/${category_slug}`)
                .then(response =>{
                    this.products = response.data
                    this.category = response.category_slug
                    console.log(this.products[0].get_image)
                    if (category_slug != "all"){
                        this.categoryall = false
                    }

                })
                .catch(err =>{
                    console.log(err)
                })
        }
    },
    counted:{
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
</style>
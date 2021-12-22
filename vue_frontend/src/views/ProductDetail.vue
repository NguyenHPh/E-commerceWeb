<template>
    <div id ="app">        
        <div class="head-intro mt-5 container-base mx-auto" >
            <h3 class="text-center">{{product.special_range}}</h3>
            <h1 class="text-center col-10 mx-auto">{{product.brief_component}}</h1>
            <span class="d-block text-center mt-3">from £ {{ minprice }}</span>
            <div class="head-intro-review text-center mt-2">
                <span class="stars-assess"></span>
                <span class="review-qtt">(based on 50 reviews)</span>
            </div>
        </div>

        <div class="container-base mx-auto">
            <hr>
        </div>


        <div class="product-display container-base mt-5 mx-auto pb-1">
            <div class="row pb-5">
                <div class="product-images col-12 col-lg-6 mb-5">
                    <div class="top-content">
                        <img id=featured class="img-fluid w-100 pt-2 px-5" v-bind:src="images[0]">
                        <div id="slide-wrapper" >
                            <img id="slideLeft" class="arrow" src="../assets/image/arrow-left.png">

                            <div id="slider">
                                <img class="thumbnail active img-fuid w-100" v-bind:src="images[0]">
                                <img class="thumbnail img-fuid w-100" v-bind:src="images[1]">
                                <img class="thumbnail img-fuid w-100" v-bind:src="images[2]">
                                <img class="thumbnail img-fuid w-100" v-bind:src="images[3]">
                                <img class="thumbnail img-fuid w-100" v-bind:src="images[4]">
                            </div>

                        <img id="slideRight" class="arrow" src="../assets/image/arrow-right.png">
                    </div>
                </div>
                </div>





                <div class="product-selection col-12 col-lg-6">
                    <table class="w-100">
                        <tr>
                            <td class="left-col">1</td>
                            <td class="right-col px-5 py-4">
                                <p>select your dog's age</p>
                                <span class="selection-box d-inline-block fas fa-check text-center"></span>
                                <span class="ml-3 month-birth">{{ product.lifeStage }} +</span>
                            </td>
                        </tr>
                        <tr>
                            <td class="left-col">2</td>
                            <td class="right-col px-5 py-4">
                                <p>select your pack size</p>
                                <div class="row text-center">
                                    <div class="col-4" v-for="(tray, index) in product.get_trays" :key="index">
                                        <div class="mx-auto product-frame">
                                            <span class="product-size d-block font-weight-bold pt-3">x{{tray[1]}}</span>
                                            <span class="product-pack-type d-block py-1">Trays</span>
                                            <span class="best-price-label d-block font-italic py-1">best value</span>
                                        </div>
                                        <p class="price-product text-center font-weight-bold mt-2">£{{ tray[1]*tray[0] }}</p>
                                        <p class="price-per-tray text-center font-italic"><span>£{{tray[0]}}</span> per tray</p>
                                        <span v-if="traySelected[index]"  class="selection-box d-inline-block fas fa-check text-center tray" @click = "selectTray(index)"></span>
                                        <span v-else class="selection-box d-inline-block text-center tray" @click = "selectTray(index)"></span>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="left-col">3</td>
                            <td class="right-col px-5 py-4">
                                <span style="font-size: 1.25rem; color: #000">quantity</span>
                                <div class="minus d-inline-block ml-4">
                                    <button type="button" v-on:click = "decrease()">
                                        <i class="fa fa-minus"></i>
                                    </button>
                                </div>

                                <div class ="quantity d-inline-block">
                                    <input type="number" id = "quantity" v-model="quantity" min ="1" mm-min="1" step ="1" mm-step="1">
                                </div>

                                <div class="plus d-inline-block ml-2" v-on:click = "increase()">
                                    <button type="button">
                                        <i class="fa fa-plus"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </table>
                    <div class="add-to-cart text-center mt-5">
                        <button type="button" class="d-inline-block px-5 py-3" @click="addToCart()">
                            add to basket
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="container-base mx-auto">
            <hr>
        </div>

        <div class="container-base mx-auto further-info my-5" >
            <div class="label row">
                <div class="label-selection border-right" 
                :class="{ 'selected-part': isSelected[0] }" v-on:click = "changeContent(0)">
                    description
                </div>

                <div class="label-selection border-right"
                :class="{ 'selected-part': isSelected[1] }" v-on:click = "changeContent(1)">
                    nutritional info
                </div>
                <div class="label-selection border-right"
                :class="{ 'selected-part': isSelected[2] }" v-on:click = "changeContent(2)">
                    feeding guide
                </div>
                <div class="label-selection border-right"
                :class="{ 'selected-part': isSelected[3] }" v-on:click = "changeContent(3)">
                    delivery info
                </div>
                <div class="label-selection"
                :class="{ 'selected-part': isSelected[4] }" v-on:click = "changeContent(4)">reviews
                    <span class="stars-assess">{{ product.rating }}</span>
                </div>
            </div>
            <div class="content mt-3 row">
                <div id ="description" class="col-9 col-lg-8 mx-auto py-5 mx-0" 
                :class="{ 'hide': !isSelected[0] }">
                    {{ product.description }}
                </div>
                <div id = "nutrition" class="col-9 col-lg-8 mx-auto py-5" 
                :class="{ 'hide': !isSelected[1] }">
                   {{ product.nutrition_info }}
                </div>
                <div id="feeding-guide" class="col-9 col-lg-8 mx-auto py-5" 
                :class="{ 'hide':  !isSelected[2] }">
                    {{ product.feeding_guide }}
                </div>
                <div id="deliver" class="col-9 col-lg-8 mx-auto py-5" 
                :class="{ 'hide':  !isSelected[3] }">
                    {{ product.deliver_info }}
                </div>
                <div id ="review" class="col-9 col-lg-8 mx-auto py-5" 
                :class="{ 'hide': !isSelected[4] }">
                    review revieww
                </div>
            </div>
        </div>
    </div> 
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'Product Detail',
    data() {
        return{
            product: {},
            isSelected: [true, false, false, false, false],
            traySelected: [true, false, false],
            quantity: 1,
            trayqtt: 0,
            priceper: 0,
            minprice: 0,
            images: []
        }
    },
    mounted() {
        this.getProduct()
        this.carousel()
        document.title = 'Product Detail'
    },
    methods:{

        async getProduct(){
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug
            await axios.get(`/api/v1/collections/${category_slug}/${product_slug}/`)
                    .then(response => {
                        this.product = response.data
                            this.minprice = this.product.get_trays[2][0]*this.product.get_trays[2][1]
                            this.product.get_images_detail.forEach(image => this.images.push(image))
                            console.log(this.images)

                    })
                    .catch(err =>{
                        console.log(err)
                    })
            this.$store.commit('setIsLoading', false)
        },

        selectTray(index){
            for (var i = 0; i < 3; i++){
                if (i == index){
                    this.traySelected[i] = true
                }
                else{
                    this.traySelected[i] = false

                }
            } 
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            for (var i = 0; i < 3; i++){
                if (this.traySelected[i] == true){
                    this.trayqtt = this.product.get_trays[i][1]
                    this.priceper = this.product.get_trays[i][0]
                    break;
                }
            } 
            
            const item = {
                product: this.product,
                quantity: this.quantity,
                trayqtt: this.trayqtt,
                priceper: this.priceper
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        },


        changeContent(id) {
            for (var i = 0; i < 5; i++){
                if (i == id){
                    this.isSelected[i] = true
                }
                else{
                    this.isSelected[i] = false

                }
            }
        },

        increase(){
            this.quantity++;
        },

        decrease(){
            if (this.quantity>1){
                this.quantity--;
            }
        },

        carousel(){
            let thumbnails = document.getElementsByClassName('thumbnail')

            let activeImages = document.getElementsByClassName('active')

            for (var i=0; i < thumbnails.length; i++){

                thumbnails[i].addEventListener('mouseover', function(){
                    console.log(activeImages)
                    
                    if (activeImages.length > 0){
                        activeImages[0].classList.remove('active')
                    }
                    

                    this.classList.add('active')
                    document.getElementById('featured').src = this.src
                })
            }


            let buttonRight = document.getElementById('slideRight');
            let buttonLeft = document.getElementById('slideLeft');

            buttonLeft.addEventListener('click', function(){
                document.getElementById('slider').scrollLeft -= 180
            })

            buttonRight.addEventListener('click', function(){
                document.getElementById('slider').scrollLeft += 180
            })
        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product-detail.css">
</style>
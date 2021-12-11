<template>
<div id="our-ranges">
    <div class="container-base mx-auto">
        <!-- <div class="row py-5">
            <div class="col-lg-4 text-center px-2 category mt-5">
                <h2>{{ categories[0].name }}</h2>
                <img src="../assets/image/our-range-category-01.png" alt="product" class="img-fluid w-100">
                <div>
                    <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                </div>
            </div>
            <div class="col-lg-4 text-center px-2 category mt-5">
                <h2>{{ categories[1].name }}</h2>
                <img src="../assets/image/our-range-category-02.png" alt="product" class="img-fluid w-100">
                <div>
                    <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                </div>
            </div>
            <div class="col-lg-4 text-center px-2 category mt-5">
                <h2>{{ categories[2].name }}</h2>
                <img src="../assets/image/our-range-category-03.png" alt="product" class="img-fluid w-100">
                <div>
                    <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                </div>
            </div>
        </div> -->

        <div class="row py-5">
            <div class="col-lg-4 text-center px-2 category mt-5" 
                v-for="category in categories"
                :key="category.id"
            >
                <h2>{{category.name}}</h2>
                <img v-bind:src="category.get_image" alt="product" class="img-fluid w-100">
                <div>
                    <router-link v-bind:to="category.get_absolute_url" class="py-2 px-3 mt-3">Learn more</router-link>
                </div>
            </div>
        </div>

        <div class="wet-range mt-5 container-fluid pb-5">
            <h1 class="pt-5 d-block">our <em >wet food</em > ranges</h1>
            <div class="row">
                <div>
                     <p class="col-10 col-lg-8 mx-auto text-center py-3">We've a wide selection of tail-waggingly tasty complete and complementary wet foods for dogs with even the most sensitive of tummies.</p>
                </div>
                <div class="row px-4 sub-cat">
                    <div class="col-lg-3 text-center pb-5">
                        <img src="../assets/image/our-range-wet-food-01.png" alt="food" class="img-fluid w-100">
                        <span>complete grain free range</span>
                        <div>
                            <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                        </div>
                    </div>
                    <div class="col-lg-3 text-center pb-5">
                        <img src="../assets/image/our-range-wet-food-02.png" alt="food" class="img-fluid w-100">
                        <span>National Trust gourmet range</span>
                        <div>
                            <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                        </div>
                    </div>
                    <div class="col-lg-3 text-center pb-5">
                        <img src="../assets/image/our-range-wet-food-03.png" alt="food" class="img-fluid w-100">
                        <span>complete with brown rice</span>
                        <div>
                            <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                        </div>
                    </div>
                    <div class="col-lg-3 text-center pb-5">
                        <img src="../assets/image/our-range-wet-food-04.png" alt="food" class="img-fluid w-100">
                        <span>complementary wet food range</span>
                        <div>
                            <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <div class="dry-range mt-5 container-fluid py-5">
            <div class="row px-4">
                <div class="col-lg-6">
                    <h1 class="pt-5 d-block">complete <em >dry foods</em></h1>
                    <p>Our cold pressed dry food is made using natural ingredients with added vitamins & minerals to ensure it contains everything your dog needs to stay happy & healthy. You don't need to mix our dry food with anything else, but if you prefer to mix up mealtimes, it's the perfect companion to our complete wet food ranges.</p>
                    <div>
                        <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                    </div>
                    <img src="../assets/image/our-range-dog-decorate.png" alt="dog" class="img-fluid w-100">
                </div>
                <div class="col-lg-6">
                    <img src="../assets/image/our-range-dry-food.png" alt="food" class="img-fluid w-100">
                </div>
            </div>
            
        </div>

         <div class="treat-range mt-5 container-fluid py-5">
            <div class="row px-4">
                <div class="col-lg-6">
                    <img src="../assets/image/our-range-treat.png" alt="food" class="img-fluid w-100">
                </div>
                <div class="col-lg-6">
                    <h1 class="pt-5 d-block">hand-baked <em >dry foods</em></h1>
                    <p>Our tail-waggingly tasty range of grain free hand-baked treats are packed with irresistible, natural ingredients to help nourish the relationship between you and your four-legged friend in between mealtimes.</p>
                    <div>
                        <a href="#" class="py-2 px-3 mt-3">Learn more</a>
                    </div>
                    <img src="../assets/image/our-range-dog-decorate2.png" alt="dog" class="img-fluid w-100">
                </div>

            </div>
            
        </div>
    </div>

    <div class="container-fluid bg-near-bottom">
        <div class="col-lg-6 mx-auto text-center py-5">
            <h2>who are we?</h2>
            <p>We’re a bunch of Devonian dog lovers and experts in pet nutrition who’ve been developing and producing natural pet food for over 45 years</p>
            <div>
                <a href="#" class="py-2 px-3 mt-3">learn more our history</a>
            </div>
        </div>
    </div>

    <div class="container-fluid py-5 about-learn-more mx-auto">
        <div class="col-lg-5 mx-auto py-4 text-center">
            <h2>need some help?</h2>
            <h4 class="mt-4 pb-3">find the right range for you</h4>
            <div class="mx-auto py-2 my-3">
                <a href="#">learn more</a>
            </div>
        </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'
export default {
    name: 'Category',
    data() {
        return{
            categories: {}
        }
    },
    mounted() {
        document.title = 'Collections'
        this.getCategories()
    },
    methods:{
        getCategories(){
            axios
                .get('/api/v1/collections')
                .then(response =>{
                    this.categories = response.data
                })
                .catch(err =>{
                    console.log(err)
                })
        } 
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/our-ranges.css">
</style>

<template>
        <div class="main-content">
        <div class="main-content__banner">
            <div class="banner__box">
                <img src="../assets/image/banner-box.png" alt="">
                <div class="banner__box__content">
                    <p class = "box__content--title">natural & nutritious</p>
                    <p class = "box__content--small-title">dogs dinner from Devon</p>
                    <p class = "box__content--pagraraph">Ignite your dogs taste buds with our natural range of dog food. With over 50 years experience, our simple and wholesome food is tail-waggingly tasty. </p>
                    <button class = "box__content--button-learn"><a href = "">learn more</a></button>
                    <button class = "box__content--button-buy"><a href="">shop now <i class="fas fa-arrow-right"></i></a></button>
                </div>
            </div>
        </div>
        <div class="main-content__tag">
            <p class="tag--natural"><span>Natural</span> ingredients</p>
            <p class="tag--devon">made in <span>Devon</span></p>
            <p class="tag--junk">free from <span>Junk</span></p>
            <p class="tag--est">Est. in <span>1971</span></p>
        </div>

        <div class="main-content__product">
            <div class="product__product1">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/GF_395_Lamb_Butternut_430x330_crop_center.jpg?v=1601903750" alt=""/>
                <p class = "product1--category">our range</p>
                <p class="product1--title">wet food</p>
                <p class="product1--content">A wide selection of tail-waggingly tasty complete and complementary wet foods</p>
                <button class = "product1__button-learn"><a href="">learn more</a></button>
                <button class = "product1__button-buy"><a href="">shop now <i class="fas fa-arrow-right"></i></a></button>
            </div>

            <div class="product__product2">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/Cold_Press_1kg_chicken_close_up_430x330_crop_center.jpg?v=1601905003" alt=""/>
                <p class = "product2--category">our range</p>
                <p class="product2--title">dry food</p>
                <p class="product2--content">Our cold pressed dry food contains everything your dog needs to stay happy & healthy

                </p>
                <button class = "product2__button-learn"><a href="">learn more</a></button>
                <button class = "product2__button-buy"><a href="">shop now <i class="fas fa-arrow-right"></i></a></button>
            </div>

            <div class="product__product3">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/Natural_Soft_Bites_Full_Range_Lifestyle_July_2020_2_430x330_crop_center.jpg?v=1602595750" alt=""/>
                <p class = "product3--category">our range</p>
                <p class="product3--title">treat</p>
                <p class="product3--content">Our range of lovingly hand-baked treats made using a mix of irresistible natural ingredients
                </p>
                <button class = "product3__button-learn"><a href="">learn more</a></button>
                <button class = "product3__button-buy"><a href="">shop now <i class="fas fa-arrow-right"></i></a></button>
            </div>
        </div>
        <div class="main-content__service-rate">
            <div class="service-rate--img1">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/Feefo21_HPBanner_400x.jpg?v=1617980799" alt="rate">
            </div>
            <div class="service-rate--img2">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/Feefo_Rating_V5_400x.progressive.jpg?v=1600258327" alt="rate">
            </div>
            <div class="service-rate__content">
                <p class = "service-rate__content--title">"Waggy tail of approval"</p>
                <p class="service-rate__content--pagraraph">"My dog is loving his tasty food choices. Sniffing around looking forward to it with very waggy tail"</p>
            </div>
        </div>
        <div class="main-content__project-and-month">
            <div class="project-and-month__project">
                <div class="project--wrapper">
                    <p class="project--title">dogs welcome project</p>
                    <p class = "project--content">an initiative to improve access for our four-legged friends</p>
                    <div class="project--button-learn">
                        <button><a href="">learn more</a></button>
                    </div>
                </div>
            </div>
            <div class="project-and-month__month">
                <div class="month--wrapper">
                    <p class="month--title">dogs welcome project</p>
                    <p class = "month--content">an initiative to improve access for our four-legged friends</p>
                    <div class="month--button-learn">
                        <button><a href="">learn more</a></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
}

<script>

export default {
    name: 'Home',
    data() {
        return{

        }
    },
    mounted() {
        document.title = 'Home'
    }
}
</script>

<style scoped src="../assets/styles/index.css">
</style>
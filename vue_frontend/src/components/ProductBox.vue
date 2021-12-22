
<template>
    <div class="product py-3">
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
</template>


                        

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
</style>
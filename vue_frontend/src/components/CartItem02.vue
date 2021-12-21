<template>
    <div class="order__product">
        <div class="product__main">
            <div class="product__main--img">
                <img v-bind:src="item.product.get_image">
                <div class="product__main--quantity">
                    <p> {{ item.quantity }}</p>
                </div>
            </div>
        </div>
        <div class="product__name">
            <p class = "name--main-name">{{ item.product.brief_component }}</p>
            <p class = "name--advice">{{ item.product.lifeStage }} + / {{ item.trayqtt }} trays</p>
        </div>
        <div class="order__price">
            <p class = "price--product-price" style="font-size: 16px">£{{getItemTotal(item)}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CartItem02',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.trayqtt*item.priceper*item.quantity
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>

<style>
    .order__product{
        padding: 10px 0;
        border-bottom: 1px solid #3a9e3f;

    }
</style>
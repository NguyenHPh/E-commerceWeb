<template>
   <div>
          <div class="shopping-cart">
            <div class="shopping-cart--title">
                <h1>Shopping basket</h1>
            </div>
            <div class="shopping-cart--subtitle">
                <img  src="../assets/image/delivery-van.png" alt="deliver">
                <p>You have qualified for free shipping!</p>
            </div>
            <div class="shopping-car__progess-bar">
                <div class="progess-bar__wrapper">
                    <div class="progess-bar__wrapper--progess">
                        
                    </div>
                </div>
            </div>
            <div class="shopping-cart__main">
                <div class="cart__container">
                    <div class="main__cart">
                        <div class="cart__table__title" style="text-align: center;">
                            <div class="title--item">
                                <p>Item</p>
                            </div>
                            <div class="title--price">
                                <p>Price</p>
                            </div>
                            <div class="title--qty">
                                <p>Qty.</p>
                            </div>
                            <div class="title--subtotal">
                                <p>Subtotal</p>
                            </div>
                            <div class="title--delete">
                                
                            </div>
                        </div>
                        <CartItem
                            v-for="item in this.$store.state.cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </div>
                </div>
                <div class="main__check-out">
                    <div class="check-out-wrapper">
                        <div class="check-out__content">
                            <div class="check-out__content--subtotal">
                                <p>Subtotal: £ {{ cartTotalPrice.toFixed(2) }}</p>
                            </div>
                            <div class="check-out__content--got-discount">
                                <p>Got a discount code? Checkout using ShopPay, PayPal or the standard checkout to apply your discount.</p>
                            </div>
                        </div>
                        <div class="check-out__button">
                            <div class="button__shoppay">
                                <a href=""><button>Shop Pay</button></a>
                            </div>
                            <div class="button__paypal">
                                <a href=""><button><i class="fab fa-paypal"></i><span class = "character-pay">Pay</span><span class = "character-pal">Pal</span></button></a>
                            </div>
                            <div class="button__gpay">
                                <a href=""><button><i class="fab fa-google"></i><span>Pay</span></button></a>
                            </div>
                            <div class="button__divider">
                                <p>- or -</p>
                            </div>
                            <div class="button__check-out">
                                <a href=""><button><span>Checkout</span></button></a>
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
import CartItem from '../components/CartItem.vue'

export default {
    name: 'Cart',
    components:{
        CartItem
    },
    data() {
        cart: {
            items: []
        }
    },
    mounted(){
        document.title = "Cart"
        this.cart = this.$store.state.cart.items
        //console.log(this.$store.state.cart.items[0].quantity)
    },
    methods:{
        removeFromCart(item) {
            this.$store.state.cart.items = this.$store.state.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed:{
        cartTotalLength() {
            return this.$store.state.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.$store.state.cart.items.reduce((acc, curVal) => {
                return acc += (curVal.product.get_trays[0][0]*curVal.product.get_trays[0][1]) * curVal.quantity
            }, 0)
        },
    }
}
</script>
<style>
    @import "../assets/styles/cart.css";
</style>
<template>
   <div class = "big-container">
        <div class="shopping-cart">
            <div class="shopping-cart--title">
                <h1>Shopping basket</h1>
            </div>
            <div class="shopping-cart--subtitle">
                <img  src="../assets/image/delivery-van.png" alt="deliver">
                <p v-if="$store.state.cart.items.length > 0">You have qualified for free shipping!</p>
                <p v-else>Buy at least one product for free shipping</p>

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
                            <div class="button__divider" v-if="$store.state.cart.items.length > 0">
                                <p>- or -</p>
                            </div>
                            <div class="button__check-out">
                                <button v-if="$store.state.cart.items.length > 0" class = "btn-check-out"><span>Checkout</span></button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="check-out__wrapper" style="display:none">
            <div class="check-out__page">
                <div class="check-out__page__information">
                    <div class="check-out__page--logo">
                        <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/logo_forthglade.png?28877" alt="logo">
                    </div>
                    <div class="page__form-information">
                        <div class="form-information__after-login">
                            <div class="after-login--avatar">
                                
                            </div>
                            <div class="after-login__info">
                                <div class="after-login__info--email">
                                    <p>Nguyen Hoang Phuong (phuongnhgcs200104@fpt.edu.vn)</p>
                                    <a href="">Login</a>
                                </div>
                            </div>
                        </div>
                          <form @submit.prevent="proceedOrder">
                            <div class="form-information--email">
                                <label for="input">Email</label>
                                <input type="text" name="email" v-model="user.email" disabled>
                            </div>
                            <div class="form-information__address">
                                <div class="address--title">
                                    <p>Delivery address</p>
                                </div>
                                <div class="address__name">
                                    <div class="name--firstname">
                                        <label for="input">First name</label>
                                        <input type="text" v-model = "userinfo.firstName" required>
                                    </div>
                                    <div class="name--lastname">
                                        <label for="">Last name</label>
                                        <input type="text" v-model = "userinfo.lastName" required>
                                    </div>
                                </div>
                                <div class="address--delivery-address" required>
                                    <label for="">Address</label>
                                    <input type="text" v-model = "userinfo.address">
                                </div>
                            </div>
                            <div class="form--information--phone">
                                <label for="">Phone number</label>
                                <input type="text" v-model = "userinfo.phone" required>
                            </div>
                        
                        <div class="page__button">
                            <div class="button--back"><i class="fas fa-chevron-left"></i> Return to basket</div>
                            <input type="submit" value="Order">
                        </div>
                    </form>
                    </div>
                   
                </div>
                <div class="check-out__order">
                    <div class="order--wrapper">
                        <div class="order__hide-show">
                            <div class="hide-show__bar">
                                <div class="hide-show__bar--title">
                                    <p><i class="fas fa-shopping-cart"></i><span> Show order summary</span> <i class="fas fa-chevron-down"></i></p>
                                </div>
                                <div class="hide-show__bar--price">
                                    <p>£86.99</p>
                                </div>
                            </div>
                        </div>
                        <div class="order__product-and-price--wrapper">
                            <div class="order__product-and-price">
                                <CartItem02
                                    v-for="item in this.$store.state.cart.items"
                                    v-bind:key="item.product.id"
                                    v-bind:initialItem="item" />
                            </div>
                            <div class="order__discount">
                                <div class="discount--code">
                                    <label for="input">Discount code</label>
                                    <input type="text" name="discount-code">
                                </div>
                                <div class="discount--button">
                                    <button>Apply</button>
                                </div>
                            </div>
                            <div class="order__subtotal">
                                <div class="subtotal--title">
                                    <p>Subtotal</p>
                                </div>
                                <div class="subtotal--price">
                                    <p>£{{ cartTotalPrice }}</p>
                                </div>
                            </div>
                            <div class="order__discount-money">
                                <div class="discount__money--title">
                                    <p>Discount</p>
                                </div>
                                <div class="discount__money--price">
                                    <p>£0</p>
                                </div>
                            </div>
                            <div class="order__total">
                                <div class="total--title">
                                    <p>Total</p>
                                </div>
                                <div class="total--price">
                                    <p>£{{ cartTotalPrice }}</p>
                                </div>
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
import CartItem02 from '../components/CartItem02.vue'
import { toast } from 'bulma-toast'
import $ from 'jquery'

export default {
    name: 'Cart',
    components:{
        CartItem,
        CartItem02
    },
    data() {
        return {
            user: '',
            userinfo: '',
            cart: {
                item: []
            },
            paid_amount: '',
            error: []
        }
    },
    mounted(){
        document.title = "Cart"
        this.cart = this.$store.state.cart
        this.getUserInfo()
        this.loadCss()
    },
    methods:{
        async getUserInfo(){
            this.$store.commit('setIsLoading', true)
            await axios.get('/api/v1/userinfo')
                .then(response =>{
                    this.user = response.data
                    console.log(this.user)
                })
                .catch(err =>{
                    console.log(err)
                })

            await axios.get('/api/v1/userorderinfo')
                .then(response =>{
                    this.userinfo = response.data
                })
                .catch(err =>{
                    this.userinfo = {
                        firstName: "",
                        lastName: "",
                        phone: "",
                        address: ""
                    }
                })
            this.$store.commit('setIsLoading', false)

        },

        async proceedOrder(){
            this.$store.commit('setIsLoading', true)
            let items = []

            for (let i = 0; i < this.$store.state.cart.items.length; i++) {
                let item = this.$store.state.cart.items[i]
                let obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    trayQuantity: item.trayqtt,
                    trayPricePer: item.priceper,
                    price: item.trayqtt * item.priceper * item.quantity
                }

                items.push(obj)
            }

            const paid_amount = this.$store.state.cart.items.reduce((acc, curVal) => {
                                    return acc += (curVal.priceper*curVal.trayqtt) * curVal.quantity
                                }, 0)
            let data = {
                'first_name': this.firstname,
                'last_name': this.lastname,
                'address': this.address,
                'phone': this.phone,
                'paid_amount': paid_amount,
                'items': items
            }

            console.log(data)


            await axios
                .post('/api/v1/', data)
                .then(response => {
                    console.log("ok")
                    this.$store.commit('clearCart')
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log("failed")

                    console.log(error)
                })
                localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
                this.$store.commit('setIsLoading', false)
        },

        removeFromCart(item) {
            this.$store.state.cart.items = this.$store.state.cart.items.filter(i => i.product.id !== item.product.id)
        },

        loadCss(){
             if(this.user.email != ""){
                $(".form-information--email label").css({"top":"15%"});
                $(".form-information--email input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            }
             if(this.userinfo.firstName != ""){
                    $(".name--firstname label").css({"top":"15%"});
                    $(".name--firstname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
                }
                if(this.userinfo.lastName != ""){
                    $(".name--lastname label").css({"top":"15%"});
                    $(".name--lastname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
                }
              if(this.userinfo.address!= ""){
                    $(".address--delivery-address label").css({"top":"15%"});
                    $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"1.9rem"});
                }
             if(this.userinfo.phone != ""){
                    $(".form--information--phone label").css({"top":"15%"});
                    $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"1.9rem"});
                }
              if($(".discount--code input").val() != ""){
                    $(".discount--code label").css({"top":"15%"});
                    $(".discount--code input").css({"padding-top":"1.1rem", "height":"1.9rem"});
                }
            $(".form-information--email input").focusin(function(){
                $(".form-information--email label").css({"top":"15%"});
                $(".form-information--email input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".form-information--email input").focusout(function(){
                if($(".form-information--email input").val() == ""){
                    $(".form-information--email label").css({"top":"35%"});
                    $(".form-information--email input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".name--firstname input").focusin(function(){
                $(".name--firstname label").css({"top":"15%"});
                $(".name--firstname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".name--firstname input").focusout(function(){
                if($(".name--firstname input").val() == ""){
                    $(".name--firstname label").css({"top":"35%"});
                    $(".name--firstname input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".name--lastname input").focusin(function(){
                $(".name--lastname label").css({"top":"15%"});
                $(".name--lastname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".name--lastname input").focusout(function(){
                if($(".name--lastname input").val() == ""){
                    $(".name--lastname label").css({"top":"35%"});
                    $(".name--lastname input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".address--delivery-address input").focusin(function(){
                $(".address--delivery-address label").css({"top":"15%"});
                $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".address--delivery-address input").focusout(function(){
                if($(".address--delivery-address input").val() == ""){
                    $(".address--delivery-address label").css({"top":"35%"});
                    $(".address--delivery-address input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".form--information--phone input").focusin(function(){
                $(".form--information--phone label").css({"top":"15%"});
                $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".form--information--phone input").focusout(function(){
                if($(".form--information--phone input").val() == ""){
                    $(".form--information--phone label").css({"top":"35%"});
                    $(".form--information--phone input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".discount--code input").focusin(function(){
                $(".discount--code label").css({"top":"15%"});
                $(".discount--code input").css({"padding-top":"1.1rem", "height":"1.9rem"});
            })

            $(".discount--code input").focusout(function(){
                if($(".discount--code input").val() == ""){
                    $(".discount--code label").css({"top":"35%"});
                    $(".discount--code input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".discount--code input").keyup(function(){
                if($(".discount--code input").val() == ""){
                    $(".discount--button button").css({"background-color":"#cccccc", "pointer-events":"none"});
                }else{
                    $(".discount--button button").css({"background-color":"#2c732f", "pointer-events":"all"});
                }
            })

            $(".hide-show__bar--title p").click(function(){
                $(".order__product-and-price--wrapper").slideToggle();
            })
            $(window).resize(function(){
                if($(window).width() > 740){
                    $(".order__product-and-price--wrapper").css("display","block");
                }
            })

            $('.btn-check-out').click(function(){
                $('.check-out__wrapper').show();
                $('.shopping-cart').hide();
            })

            $('.button--back').click(function(){
                $('.check-out__wrapper').hide();
                $('.shopping-cart').show();
            })
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
                return acc += (curVal.priceper*curVal.trayqtt) * curVal.quantity
            }, 0)
        }
    }
    
}
</script>
<style>
    @import "../assets/styles/cart.css";
     @import "../assets/styles/check-out-page.css";
     
</style>
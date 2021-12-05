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
                        <div class="cart__table__title">
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
                        <div class="cart__table">
                            <div class="table__item">
                                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/products/OI_6kg_CP_Chicken_FRONT_120x120.jpg?v=1634656280" alt="">
                                <div class="item__info">
                                    <a href="" class = "info--name">Chicken Grain Free Cold Pressed Natural Dry Dog Food</a>
                                    <p class = "info--age">Age 2 month+ / 18kg</p>
                                </div>
                            </div>
                            <div class="table__price">
                                <div class="price__product">
                                    <p class = "price__product--total">£86.99</p>
                                    <p class = "price__product--per-kg">£4.83 per kg</p>
                                </div>
                            </div>
                            <div class="table__qty">
                                <form action="" method="post">
                                    <input type="number" name = "product-quantity">
                                </form>
                            </div>
                            <div class="table__subtotal">
                                <p class = "subtotal--content">£86.99</p>
                            </div>
                            <div class="table__delete">
                                <a href="" class = "delete--x"><i class="fas fa-times"></i></a>
                                <a href="" class = "delete--remove">Remove</a>
                            </div>
                        </div>
                        <div class="cart__table">
                            <div class="table__item">
                                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/products/OI_6kg_CP_Chicken_FRONT_120x120.jpg?v=1634656280" alt="">
                                <div class="item__info">
                                    <a href="" class = "info--name">Chicken Grain Free Cold Pressed Natural Dry Dog Food</a>
                                    <p class = "info--age">Age 2 month+ / 18kg</p>
                                </div>
                            </div>
                            <div class="table__price">
                                <div class="price__product">
                                    <p class = "price__product--total">£86.99</p>
                                    <p class = "price__product--per-kg">£4.83 per kg</p>
                                </div>
                            </div>
                            <div class="table__qty">
                                <form action="" method="post">
                                    <input type="number" name = "product-quantity">
                                </form>
                            </div>
                            <div class="table__subtotal">
                                <p class = "subtotal--content">£86.99</p>
                            </div>
                            <div class="table__delete">
                                <a href="" class = "delete--x"><i class="fas fa-times"></i></a>
                                <a href="" class = "delete--remove">Remove</a>
                            </div>
                        </div>
                        
                    </div>
                </div>
                <div class="main__check-out">
                    <div class="check-out-wrapper">
                        <div class="check-out__content">
                            <div class="check-out__content--subtotal">
                                <p>Subtotal: £86.99</p>
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

export default {
    name: 'Cart',
    data() {

    },
    methods: {

    },
    mounted(){
        document.title = "Cart";
    }
}
</script>
<style>
    @import "../assets/styles/cart.css";
</style>
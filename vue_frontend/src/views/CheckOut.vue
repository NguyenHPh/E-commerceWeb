<template>
        <div class="check-out__wrapper">
            <div class="check-out__page">
                <div class="check-out__page__information">
                    <div class="check-out__page--logo">
                        <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/logo_forthglade.png?28877" alt="logo">
                    </div>
                    <div class="page__contact-info">
                        <div class="contact-info--title">
                            <p>Contact information</p>
                        </div>
                        <div class="contact-info--login">
                            <p>Already have an account? <a href="">Login</a></p>
                        </div>
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
                        <form action="" method="post">
                            <div class="form-information--email">
                                <label for="input">Email</label>
                                <input type="text" name="email">
                            </div>
                            <div class="form-information__address">
                                <div class="address--title">
                                    <p>Delivery address</p>
                                </div>
                                <div class="address__name">
                                    <div class="name--firstname">
                                        <label for="input">First name</label>
                                        <input type="text" name = "firstname">
                                    </div>
                                    <div class="name--lastname">
                                        <label for="">Last name</label>
                                        <input type="text" name = "lastname">
                                    </div>
                                </div>
                                <div class="address--delivery-address">
                                    <label for="">Address</label>
                                    <input type="text" name = "address">
                                </div>
                            </div>
                            <div class="form--information--phone">
                                <label for="">Phone number</label>
                                <input type="text" name = "phone-number">
                            </div>
                        </form>
                    </div>
                    <div class="page__button">
                        <div class="button--back"><a href=""><i class="fas fa-chevron-left"></i> Return to basket</a></div>
                        <a href="" class = "button--continue-to-delivery"><button >Continue to delivery</button></a>
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
                                <div class="order__product">
                                    <div class="product__main">
                                        <div class="product__main--img">
                                            <img src="../image/product-img-01.jpg" alt="">
                                            <div class="product__main--quantity">
                                                <p>1</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="product__name">
                                        <p class = "name--main-name">Chicken Grain Free Cold Pressed Natural Dry Dog Food</p>
                                        <p class = "name--advice">Age 2 months + / 18kg</p>
                                    </div>
                                </div>
                                <div class="order__price">
                                        <p class = "price--product-price">£86.99</p>
                                </div>
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
                                    <p>£86.99</p>
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
                                    <p>£86.99</p>
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
    name: 'check out',
    data() {

    },
    methods: {

    },
    mounted(){
            document.title = "Check Out";
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

        }
}
</script>
<style>
    @import "../assets/styles/check-out-page.css";
</style>
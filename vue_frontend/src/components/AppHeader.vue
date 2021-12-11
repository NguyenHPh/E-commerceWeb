<template>
<header>
<div class="blur-glass">
            
</div>
<div class="small-nav-bar">
    <div class="small-nav-bar__title">
        <span class = "title--icon"><i class="fas fa-chevron-left"></i></span> <div class="small-nav-bar__title--content"><p>Forth glade</p></div>
    </div>
    <div class="small-nav-bar__menu">
        <ul class = "main-ul-1">
            <li><a href="">wet food {{ getCategories }} </a></li>
            <li><a href="">dry food</a></li>
            <li><a href="">dog treats</a></li>
            <li><div class="ul-header-2"><span>our range</span><i class="fas fa-chevron-right"></i></div>
                <ul class = "main-ul-1-2">
                    <li><a href="">limited edition recipes</a></li>
                    <li><a href="">grain free complete meals</a></li>
                    <li><a href="">brown rice complete meals</a></li>
                </ul>
            </li>
            <li><div class="ul-header-3"><span>discover forthglade</span><i class="fas fa-chevron-right"></i></div>
                <ul class = "main-ul-1-3">
                    <li><div class="ul-header-3-1"><span>About forthglade</span><i class="fas fa-chevron-right"></i></div>
                        <ul>
                            <li><a href="">limited edition recipes</a></li>
                            <li><a href="">grain free complete meals</a></li>
                            <li><a href="">brown rice complete meals</a></li>
                        </ul>
                    </li>
                    <li><div class="ul-header-3-2"><span>Latest news</span><i class="fas fa-chevron-right"></i></div>
                        <ul>
                            <li><a href="">limited edition recipes</a></li>
                            <li><a href="">limited edition recipes</a></li>
                            <li><a href="">limited edition recipes</a></li>
                        </ul>
                    </li>
                    <li><div class="ul-header-3-3"><span>Join the team</span><i class="fas fa-chevron-right"></i></div>
                        <ul>
                            <li><a href="">limited edition recipes</a></li>
                            <li><a href="">limited edition recipes</a></li>
                            <li><a href="">limited edition recipes</a></li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li><div class="ul-header-5"><i class="fas fa-user-circle"></i><a href="">log in</a></div></li>
            <li><div class="ul-header-4"><i class="fas fa-question-circle"></i><span>help</span><i class="fas fa-chevron-right"></i></div>
                <ul class = "ul-header-4-1">
                    <li><a href="">Join the team</a></li>
                    <li><a href="">Delivery and returns</a></li>
                    <li><a href="">feeding advice</a></li>
                </ul>
            </li>
        </ul>
    </div>
</div>
<div class="header">
    <div class="header__top">
        <div class="header__top--top1">
        </div>
        <div class="header__top--top2">  
        </div>
        <div class="header__top--top1">
        </div>
    </div>
    <div class="header__main-header">
        <div class="header__main-header__icon">
            <div class="header__main-header--bar">
                <i class = "fas fa-bars"></i>
                <p class="header--bar-title">Menu</p>
            </div>
            <div class="header__main-header--phone">
                <i class="fas fa-phone-alt"></i>
                <p class = "phone-number">0394 712 245</p>
            </div>
            <div class="header__main-header--login">
                <template v-if="$store.state.isAuthenticated">
                    <a style="text-decoration: none; color: black" @click = "logout()"> logout </a>
                </template>
                <template v-else>
                    <router-link :to="{ path: '/log-in'}" style="text-decoration: none; color: black"> login </router-link>
              </template>
            </div>
            <div class="header__main-header--divider">
                <span style="margin-left: 0.5rem;">|</span>
            </div>
            <div class="header__main-header--help">
                <p>help
                    <ul class = "list-help">
                        <li><a href="">find a stockit</a></li>
                        <li><a href="">get in touch</a></li>
                        <li><a href="">subcribe and save</a></li>
                        <li><a href="">delivery and return</a></li>
                        <li><a href="">join the team</a></li>
                    </ul>
                </p>
                <div class="sort-down-icon">
                    <i class="fas fa-sort-down"></i>
                </div>
            </div>
        </div>
        <div class="header__main-header__search-and-cart">
            <div class="header__main-header--search">
                <form action="" method="post">
                    <input type="text" name = "product_name" placeholder="product search">
                    <button class = "search--button" type="submit"><i class="fas fa-search"></i></button>
                    <div class="search--button-disable">

                    </div>
                </form>
            <p class="search--title">Search</p>
            </div>
            <div class="header__main-header__cart">
                <a href="">
                    <i class="fas fa-shopping-basket"></i>
                    <p class = "cart--content" v-if = "cartTotalLength < 1"> your basket is empty!</p>
                    <p class = "cart--content" v-else> ({{ cartTotalLength }})   checkout <i class="fas fa-arrow-right"></i></p>
                    <p class="cart--title">Basket</p>
                </a>
            </div>
        </div>
    </div>
    <div class="small-search">
            <form action="">
                <input type="text" placeholder="product search" name = "product_name">
                <button type="submit"><i class="fas fa-search"></i></button>
            </form>
    </div>
    <div class="header--logo">
        <img src="//cdn.shopify.com/s/files/1/0402/7685/2896/t/2/assets/logo_forthglade.svg?v=8815871955478593558"  alt="logo">
    </div>
    <div class="header--divider">
    </div>
</div>
</header>
</template>
<script>
    import axios from 'axios'
    import $ from "jquery";
    export default{
        name: "AppHeader",
        props: {
            cartTotalLength: Number,
            getCategories: Array,

        },
        data(){
            return{
                
            }       
        },
        mounted(){
            $(".header__main-header--bar").click(function(){
                $("body").css("overflow","hidden");
                $(".small-nav-bar").removeClass('transform-disappear');
                $(".small-nav-bar").addClass("transform-appear");
                $(".blur-glass").css("display", "block");
            });

            $(".title--icon").click(function(){
                $("body").css("overflow","scroll");
                $(".blur-glass").css("display", "none");
                $(".small-nav-bar").addClass("transform-disappear").one('animationend',   
                    function(e) {
                        $(".small-nav-bar").removeClass('transform-appear');
                    });
            });
            $(".ul-header-1").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1").slideToggle();
            })

            $(".main-ul-1-1 .ul-header-1-1").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:first-child ul").slideToggle();
            })

            $(".main-ul-1-1 .ul-header-1-2").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:nth-child(2) ul").slideToggle();
            })
            $(".main-ul-1-1 .ul-header-1-3").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:nth-child(3) ul").slideToggle();
            })
            $(".ul-header-2").click(function(){
                $(".small-nav-bar ul li:nth-child(4) .main-ul-1-2").slideToggle();
            });

            $(".ul-header-3").click(function(){
                $(".small-nav-bar ul li:nth-child(5) .main-ul-1-3").slideToggle();
            });

            $(".main-ul-1-3 ul-header-3-1").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:first-child ul").slideToggle();
            })
            $(".main-ul-1-3 ul-header-3-2").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:nth-child(2) ul").slideToggle();
            })
            $(".main-ul-1-3 ul-header-3-3").click(function(){
                $(".small-nav-bar ul li:first-child .main-ul-1-1 li:nth-child(3) ul").slideToggle();
            });
            $(".ul-header-4").click(function(){
                $(".ul-header-4-1").slideToggle();
            })

            $(".search--button-disable").click(function(){
                $(".small-search").slideToggle(0);
            });

        },
        methods: {
            logout() {
                axios.defaults.headers.common["Authorization"] = ""

                localStorage.removeItem("token")
                localStorage.removeItem("username")
                localStorage.removeItem("userid")
                this.$store.commit('removeToken')
                this.$router.push('/')
            }
        }
        
    }
</script>


<style>
    .header__main-header--login a{
        cursor: pointer;
    }
</style>   
<template>
    <footer>
        <div class="footer">
    <h2 class = "footer--title">Stay updated with Forthglade</h2>
    <div class="form-email">
        <form action="">
            <input type="text" name = "customer-email" placeholder="your-email address">
            <button type="submit">Submit</button>
        </form>
    </div>
    <div class="footer__social">
        <div class="footer__social--facebook">
            <a href=""><img src="../assets/image/facebook-logo.png" width="45rem" alt="facebook"></a>
        </div>
        <div class="footer__social--twiter">
            <a href=""><img src="../assets/image/twitter.png" width="45rem" alt="twitter"></a>
        </div>
        <div class="footer__social--instagram">
            <a href=""><img src="../assets/image/instagram.png" width="45rem" alt=""></a>
        </div>
    </div>
    <div class="footer__decor">
        <div class="footer__image">
            <div class="footer__image--dog">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/forthglade_footer_walkingdog_400x_8762e2e5-0b0b-4760-8426-ebd0f4848657_400x.png?v=1618919449" alt="dog">
            </div>
            <div class="footer__image--flag">
                <img src="https://cdn.shopify.com/s/files/1/0402/7685/2896/files/forthglade_footer_feefo_400x_2x_2021_400x.png?v=1618919396" alt="flag">
            </div>
        </div>
    </div>
</div>
<div class="footer__info">
    <div class="footer__info__account">
        <p class = "footer__info__account--title">account</p>
        <ul>
            <li>
                <a href="/log-in">login</a>
            </li>
        </ul>
    </div>
    <div class="footer__info__help">
        <p class = "footer__info__help--title">help</p>
        <ul>
            <li><a href="/about">discover forthglade</a></li>
            <li><a href="/get-in-touch">get in touch</a></li>
            <li><a href="">find a stockist</a></li>
            <li><a href="/advices">advices</a></li>
            <li><a href="">deliver and return</a></li>
            <li><a href="">join a team</a></li>
        </ul>

    </div>
    <div class="footer__info__legal">
        <p class = "footer__info__legal--title">legal</p>
        <ul>
            <li><a href="/privacy">privacy and security</a></li>
            <li><a href="/term">terms and condition</a></li>
        </ul>
    </div>
    <div class="footer__info__stockist">
        <p class = "footer__info__stockist--title">become a stockist</p>
        <p class = "footer__info__stockist--content">get in touch with our team to find out more</p>
        <button><a href="/get-in-touch">get in touch</a></button>
    </div>
</div>
<div class="small-footer">
    <ul>
        <li><div><span>account</span><i class="fas fa-sort-down"></i></div>
            <ul>
                <li><a href="/log-in">log in</a></li>
            </ul>
        </li>
        <li><div><span>help</span><i class="fas fa-sort-down"></i></div>
            <ul>
                <li><a href="/about">discover forthglade</a></li>
                <li><a href="/get-in-touch">get in touch</a></li>
                <li><a href="">find a stockist</a></li>
                <li><a href="/advices">dvices</a></li>
                <li><a href="">join a team</a></li>
            </ul>
        </li>
        <li><div><span>legal</span><i class="fas fa-sort-down"></i></div>
            <ul>
                <li><a href="/about">privacy and security</a></li>
                <li><a href="/term">terms and condition</a></li>
            </ul>
        </li>
        <li><a href="">become a stockist</a></li>
    </ul>
</div>
    </footer>
</template>
<script>
    import $ from "jquery";
    export default{
        name: "AppFooter",
        mounted(){
            $(".small-footer ul li:first-child").click(function(){
                $(".small-footer ul li:first-child ul").slideToggle();
            });

            $(".small-footer ul li:nth-child(2)").click(function(){
                $(".small-footer ul li:nth-child(2) ul").slideToggle();
            });

            $(".small-footer ul li:nth-child(3)").click(function(){
                $(".small-footer ul li:nth-child(3) ul").slideToggle();
            });


        }
    }
</script>
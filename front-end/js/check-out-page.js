// $(".form-information--email input").focusin(function(){
//     $(".form-information--email label").css({"top":"15%"});
//     $(".form-information--email input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".form-information--email input").focusout(function(){
//     if($(".form-information--email input").val() == ""){
//         $(".form-information--email label").css({"top":"35%"});
//         $(".form-information--email input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".name--firstname input").focusin(function(){
//     $(".name--firstname label").css({"top":"15%"});
//     $(".name--firstname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".name--firstname input").focusout(function(){
//     if($(".name--firstname input").val() == ""){
//         $(".name--firstname label").css({"top":"35%"});
//         $(".name--firstname input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".name--lastname input").focusin(function(){
//     $(".name--lastname label").css({"top":"15%"});
//     $(".name--lastname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".name--lastname input").focusout(function(){
//     if($(".name--lastname input").val() == ""){
//         $(".name--lastname label").css({"top":"35%"});
//         $(".name--lastname input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".address--delivery-address input").focusin(function(){
//     $(".address--delivery-address label").css({"top":"15%"});
//     $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".address--delivery-address input").focusout(function(){
//     if($(".address--delivery-address input").val() == ""){
//         $(".address--delivery-address label").css({"top":"35%"});
//         $(".address--delivery-address input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".form--information--phone input").focusin(function(){
//     $(".form--information--phone label").css({"top":"15%"});
//     $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".form--information--phone input").focusout(function(){
//     if($(".form--information--phone input").val() == ""){
//         $(".form--information--phone label").css({"top":"35%"});
//         $(".form--information--phone input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".discount--code input").focusin(function(){
//     $(".discount--code label").css({"top":"15%"});
//     $(".discount--code input").css({"padding-top":"1.1rem", "height":"1.9rem"});
// })

// $(".discount--code input").focusout(function(){
//     if($(".discount--code input").val() == ""){
//         $(".discount--code label").css({"top":"35%"});
//         $(".discount--code input").css({"padding-top":"0rem", "height":"3rem"});
//     }
// })

// $(".discount--code input").keyup(function(){
//     if($(".discount--code input").val() == ""){
//         $(".discount--button button").css({"background-color":"#cccccc", "pointer-events":"none"});
//     }else{
//         $(".discount--button button").css({"background-color":"#2c732f", "pointer-events":"all"});
//     }
// })

// $(".hide-show__bar--title p").click(function(){
//     $(".order__product-and-price--wrapper").slideToggle();
// })
$(window).resize(function(){
    if($(window).width() > 740){
        $(".order__product-and-price--wrapper").css("display","block");
    }
})

if($(".form-information--email input").val() != ""){
    $(".form-information--email label").css({"top":"15%"});
    $(".form-information--email input").css({"padding-top":"1.1rem", "height":"1.9rem"});
}
 if($(".name--firstname input").val() != ""){
        $(".name--firstname label").css({"top":"15%"});
        $(".name--firstname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
    }
    if($(".name--lastname input").val() != ""){
        $(".name--lastname label").css({"top":"15%"});
        $(".name--lastname input").css({"padding-top":"1.1rem", "height":"1.9rem"});
    }
  if($(".address--delivery-address input").val() != ""){
        $(".address--delivery-address label").css({"top":"15%"});
        $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"1.9rem"});
    }
 if($(".form--information--phone input").val() != ""){
        $(".form--information--phone label").css({"top":"15%"});
        $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"1.9rem"});
    }
  if($(".discount--code input").val() != ""){
        $(".discount--code label").css({"top":"15%"});
        $(".discount--code input").css({"padding-top":"1.1rem", "height":"1.9rem"});
    }
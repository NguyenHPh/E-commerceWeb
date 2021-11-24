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

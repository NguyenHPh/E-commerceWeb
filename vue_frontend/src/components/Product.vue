<template>
    <div class="mt-5">
        <div class="container-base d-md-flex align-items-stretch mx-auto">
      <!-- Page Content  -->
            <nav id="sidebar" class="px-4">
                <div class="text-center">
                    <h4>Filter results:</h4>
                    <ul class="list-unstyled components mb-1 mt-3 px-4 py-4 text-left">
                      <li>
                        <a href="#pageSubmenu1" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle pt-2 pb-3 d-block">by type</a>
                        <ul class="collapse list-unstyled" id="pageSubmenu1">
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas fa-check mr-2"></i>wet food
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i> dry food
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i>dog treats
                                </a>
                            </li>
                        </ul>
                      </li>
                      <li>
                        <a href="#pageSubmenu2" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle py-2 d-block">by lifestage</a>
                        <ul class="collapse list-unstyled" id="pageSubmenu2">
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas fa-check mr-2"></i>puppy
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i> adult
                                </a>
                            </li>
                            <li>
                                <a href="#" class="mb-3 d-flex">
                                    <i class="fas mr-2"></i>senior 
                                </a>
                            </li>
                        </ul>
                      </li>
                    </ul>
                </div>
            </nav>

            <div id="content" class="pl-5">
                <span class="result-quantity">displaying 50 results</span>
                <div class="product py-3">
                    <div class="row">
                        <div class="col-10 col-lg-4 mx-auto pt-4">
                            <img src="../assets/image/product-display-01.jpg" alt="product" class="img-fluid w-100">
                        </div>
                        <div class="col-10 col-lg-8 pt-4 mx-auto">
                            <h3><a href="#">personalised birthday box for dogs</a></h3>
                            <p class="age">available in: adult 1+ years</p>
                            <p>******** <span class="review">(based on 13 reviews)</span></p>
                            <div class="row text-center">
                                <div class="col-4">
                                    <div class="mx-auto product-frame">
                                        <span class="product-size d-block font-weight-bold pt-3">x36</span>
                                        <span class="product-pack-type d-block py-1">Trays</span>
                                        <span class="best-price-label d-block font-italic py-1">best value</span>
                                    </div>
                                    <p class="price-product text-center font-weight-bold mt-2">£51.25</p>
                                    <p class="price-per-tray text-center font-italic"><span>£1.42</span> per tray</p>
                                </div>
                                <div class="col-4">
                                    <div class="mx-auto product-frame">
                                        <span class="product-size d-block font-weight-bold pt-3">x18</span>
                                        <span class="product-pack-type d-block py-1">Trays</span>
                                    </div>
                                    <p class="price-product text-center font-weight-bold mt-2">£26.30</p>
                                    <p class="price-per-tray text-center font-italic"><span>£1.46</span> per tray</p>
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
                                <a href="#">view full product detail</a>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>



export default {
    name: 'Product',
    props: {
        product: Object
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/product.css">
</style>
<template>
    <div id = "advices">
        <div class="container-fluid mx-5 mx-auto pt-5">
            <div class="row">
                <div class="col-lg-4">
                    <p class="text-center my-3">Our feeding advice is here to help you, but no one knows your four-legged friend better than you do - so you should tailor the amount you feed based on your dogs' individual lifestyle.</p>
                    <p class="text-center my-3">As a general rule, if your dog is very active you may want to consider feeding more and likewise if your pup isn't very active you may want to consider feeding less.</p>
                </div>
                <div class="col-lg-4">
                    <img src="../assets/image/advice-one-dog-head.png" alt="dog eating" class="w-100 img-fluid">
                </div>
                <div class="col-lg-4">
                    <p class="text-center my-3">If you're using Forthglade for the first time, as with all new foods it's important that you gradually introduce it over a period of around 5 days to avoid any unnecessary tummy upset.</p>
                    <p class="text-center my-3">As always, please make sure your canine companion always has access to fresh drinking water.</p>
                </div>
            </div>
        </div>

        <div class="container-base mx-auto further-info mt-5" >
            <div class="label row">
                <div class="col-lg-6 mx-auto">
                    <div class="row">
                        <div class="label-selection border-right col-12  col-lg-4" 
                        :class="{ 'selected-part': isSelected[0] }" v-on:click = "changeContent(0)">
                            wet food
                        </div>

                        <div class="label-selection border-right col-12  col-lg-4"
                        :class="{ 'selected-part': isSelected[1] }" v-on:click = "changeContent(1)">
                            dry food
                        </div>
                        <div class="label-selection  col-12 col-lg-4"
                        :class="{ 'selected-part': isSelected[2] }" v-on:click = "changeContent(2)">
                            treats
                        </div>
                    </div>
                </div>
            </div>
            <div class="content mt-3 row">
                <div id ="wet-food" class="col-11 mx-auto py-5 mx-0" 
                :class="{ 'hide': !isSelected[0] }">
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal grain free (puppy 2-12 months)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-01.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                                <p class="px-5 py-3">Your puppy needs more food in it's younger months to support its growth & development, so as it reaches 6 months the amount you feed should reduce slightly and this is reflected in our feeding advice above.</p>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal grain free (adult 1 year+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-02.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete gourmet meal grain free (adult 1 year+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-03.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal grain free (senior 7 years+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                               <div>
                                    <img src="../assets/image/advice-wet-food-04.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal with brown rice (puppy 2-12 months)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-05.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                                <p class="px-5 py-3">Your puppy needs more food in it's younger months to support its growth & development, so as it reaches 6 months the amount you feed should reduce slightly and this is reflected in our feeding advice above.</p>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal with brown rice (adult 1 year+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-06.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete meal with brown rice (senior 7 years+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-07.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>small dog complete meal grain free</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-wet-food-08.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>complete gourmet meal grain free (adult 1 year+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <p class="px-5 py-3">Our Just 90% range is designed to help you tailor mealtimes and can be used alongside a good quality mixer, as a treat or alongside your own choice of healthy vegetables to create a balanced meal. The amount you should feed will depend on how you choose to use our Just range because the calorie content of what you choose to add will vary. Our feeding advice below gives you a rough idea on how much to use, but you, of course, know your dog better than we do - so keep an eye on their weight and adjust the quantities as needed.</p>
                                <div>
                                    <img src="../assets/image/advice-wet-food-09.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <div id = "dry-food" class="col-11 mx-auto py-5" 
                :class="{ 'hide': !isSelected[1] }">
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>cold pressed grain free dry food (puppy 2-12 months)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-dry-food-01.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>cold pressed grain free dry food (Adults 1 year+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-dry-food-02.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>cold pressed grain free dry food (senior 7 years+)</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <div>
                                    <img src="../assets/image/advice-dry-food-03.png" alt="table plan" class="d-block col-12 mx-auto">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="treats" class="col-11 mx-auto py-5" 
                :class="{ 'hide':  !isSelected[2] }">
                    <div class="info-plan-meal">
                        <div class="front-show py-4">
                            <i class="fas fa-arrow-right mx-4"></i>
                            <span>grain free hand-baked treats</span>
                            <i class="fas fa-caret-down ml-auto mr-4"></i>
                        </div>
                        <div class="content-inner">
                            <div class="group">
                                <p class="px-5 py-3">Treats are for special occasions and should only play a small part in your dogs' balanced diet. If you're likely to use treats often, you may want to consider feeding less at mealtimes to make sure you don't accidentally over-feed your pup.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <div class="container-base py-5 about-learn-more mb-5 mx-auto">
            <div class="col-lg-4 mx-auto py-4 text-center">
                <h2>still not sure?</h2>
                <h4 class="mt-4 pb-3">tailoring how much you feed based on your dogs lifestyle</h4>
                <div class="mx-auto py-2 my-3">
                    <a href="#">learn more</a>
                </div>
            </div>
        </div>
    </div>
</template>
}

<script>

export default {
    name: 'Advices',
    data() {
        return{
            isSelected: [true, false, false],
            quantity: 1
        }
    },
    mounted() {
        document.title = 'Advices'
        var groups = document.getElementsByClassName("front-show");
        for (var i = 0; i<groups.length; i++){
            groups[i].onclick = function(){
                if (this.nextElementSibling.style.display == "block"){
                    this.nextElementSibling.style.display = "none";
                }
                else{
                    this.nextElementSibling.style.display = "block";
                }
            }
        }

    },
    methods: {
        changeContent: function(id) {
                for (var i = 0; i < 3; i++){
                    if (i == id){
                        this.isSelected[i] = true
                    }
                    else{
                       this.isSelected[i] = false
                    }
                }
            },

        increase: function(){
            this.quantity++;
        },

        decrease: function(){

            if (this.quantity>1){
                this.quantity--;
            }
        }
    }
}

</script>


<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/advices.css">
</style>

<template>
    <div class="user-info-page">
            <div class="wrappers">
                <div class = "user-info">
                    <div class = "user-info-detail">
                        <div class = "user-image">
                        </div>
                        <div class = "info">
                            <h1 id = "user-name">Nguyễn Hoàng Phương</h1>
                        </div>
                    </div>
                </div>
                    <div class="edit-user-info">
                        <div class="check-out__page__information">
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
                                <form  @submit.prevent="submitForm" enctype="multipart/form-data">
                                    <div class="form-information__address">
                                        <div class="address--title">
                                            <p>User Information</p>
                                        </div>
                                        <div class="address__name">
                                            <div class="name--firstname">
                                                <label for="input">First name</label>
                                                <input type="text" name = "firstname" v-model="first_name">
                                            </div>
                                            <div class="name--lastname">
                                                <label for="">Last name</label>
                                                <input type="text" name = "lastname" v-model="last_name">
                                            </div>
                                        </div>
                                    <div class="form-information--email">
                                        <label for="input">Email</label>
                                        <input type="text" name="email" v-model = "email">
                                    </div>
                                        <div class="address--delivery-address">
                                            <label for="">Address</label>
                                            <input type="text" name = "address" v-model="address">
                                        </div>
                                    </div>
                                    <div class="form--information--phone">
                                        <label for="">Phone number</label>
                                        <input type="text" name = "phone-number" v-model="phone">
                                    </div>
                                    <div class="form-information--image">
                                        <label for="">Image: </label>
                                        <input type ="file" name = "user-image" @change="processFile($event)">
                                    </div>
                                    <div class="form-submit--button">
                                        <input type="submit" name = "submit" value="Update info">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
</template>

<script>
    export default{
        name: "Info",
        data(){
            return{
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                address: '',
                image: ''
            }
        },
        mounted(){
            document.title = "User Info";
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
            },
        methods:{
            async submitForm(){
                const data = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'address': this.address,
                    'phone': this.phone,
                    'image': this.image
                }

                await axios
                    .post('/api/v1/checkout/', data)
                    .then(response => {
                        console.log("ok")
                    })
                    .catch(error => {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(error)
                    })
            },

            processFile(event) {
                this.image = event.target.files[0]
            }

        }
    }
</script>
<style>
 @import "../assets/styles/user-info.css";
 .user-image{
     background: url(../assets/image/user-avatar.png);
     background-size: cover;
     background-repeat: no-repeat;
 }
</style>
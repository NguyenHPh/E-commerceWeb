<template>
<div class="user-info-page">
    <div class="wrappers">
        <div class = "user-info">
            <div class = "user-info-detail">
                <div class = "info" v-if="userinfo">
                    <h1 id = "user-name">{{ userinfo.firstName + " " + userinfo.lastName }}</h1>
                </div>
            </div>
        </div>
            <div class="edit-user-info">
                <div class="check-out__page__information">
                    <div class="page__contact-info">
                        <div class="contact-info--title">
                            <p>Contact information</p>
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
                        <form @submit.prevent = "submitForm">
                            <div class="form-information--email">
                                <label for="input">Email</label>
                                <input type="text" v-model="user.email" disabled>
                            </div>
                            <div class="form-information__address">
                                <div class="address--title">
                                    <p>User Information</p>
                                </div>
                                <div class="address__name">
                                    <div class="name--firstname">
                                        <label for="input">First name</label>
                                        <input type="text" v-model="userinfo.firstName" required>
                                    </div>
                                    <div class="name--lastname">
                                        <label for="">Last name</label>
                                        <input type="text" v-model="userinfo.lastName" required>
                                    </div>
                                </div>
                                <div class="address--delivery-address">
                                    <label for="">Address</label>
                                    <input type="text" v-model="userinfo.address" required>
                                </div>
                            </div>
                            <div class="form--information--phone">
                                <label for="">Phone number</label>
                                <input type="text" v-model="userinfo.phone" required>
                            </div>
                            <div class="form-submit--button">
                                <input type="submit" name = "submit" value="Update">
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import { toast } from 'bulma-toast'
import axios from 'axios'
import $ from 'jquery'
export default {
    name: 'UserInfo',
    data() {
        return{
            user: '',
            userinfo: ''
        }
    },
    mounted() {
        document.title = 'User Info'
        this.getUserInfo()
        this.loadCss()
    },
    methods: {
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
        async submitForm(){
            this.$store.commit('setIsLoading', true)

            let data = {
                firstName: this.userinfo.firstName,
                lastName: this.userinfo.lastName,
                phone: this.userinfo.phone,
                address: this.userinfo.address
            }
            console.log(data)
            await axios.post('/api/v1/updateinfo', data)
                .then(response =>{
                    console.log("ok")
                    this.$store.commit('setIsLoading', false)
                    toast({
                        message: 'Update successfully',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })
                .catch(err =>{
                    console.log(err)
                })
            this.$store.commit('setIsLoading', false)

        },
        loadCss(){
            if(this.user.email != ""){
                $(".form-information--email label").css({"top":"15%"});
                $(".form-information--email input").css({"padding-top":"1.1rem", "height":"3rem"});
            }
            if(this.userinfo.firstName != ""){
                    $(".name--firstname label").css({"top":"15%"});
                    $(".name--firstname input").css({"padding-top":"1.1rem", "height":"3rem"});
                }
            if(this.userinfo.lastName != ""){
                    $(".name--lastname label").css({"top":"15%"});
                    $(".name--lastname input").css({"padding-top":"1.1rem", "height":"3rem"});
                }
            if(this.userinfo.address!= ""){
                    $(".address--delivery-address label").css({"top":"15%"});
                    $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"3rem"});
                }
            if(this.userinfo.phone != ""){
                    $(".form--information--phone label").css({"top":"15%"});
                    $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"3rem"});
                }
            $(".form-information--email input").focusin(function(){
                $(".form-information--email label").css({"top":"15%"});
                $(".form-information--email input").css({"padding-top":"1.1rem", "height":"3rem"});
            })

            $(".form-information--email input").focusout(function(){
                if($(".form-information--email input").val().trim() == ""){
                    $(".form-information--email label").css({"top":"35%"});
                    $(".form-information--email input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".name--firstname input").focusin(function(){
                $(".name--firstname label").css({"top":"15%"});
                $(".name--firstname input").css({"padding-top":"1.1rem", "height":"3rem"});
            })

            $(".name--firstname input").focusout(function(){
                if($(".name--firstname input").val().trim() == ""){
                    $(".name--firstname label").css({"top":"35%"});
                    $(".name--firstname input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".name--lastname input").focusin(function(){
                $(".name--lastname label").css({"top":"15%"});
                $(".name--lastname input").css({"padding-top":"1.1rem", "height":"3rem"});
            })

            $(".name--lastname input").focusout(function(){
                if($(".name--lastname input").val().trim() == ""){
                    $(".name--lastname label").css({"top":"35%"});
                    $(".name--lastname input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".address--delivery-address input").focusin(function(){
                $(".address--delivery-address label").css({"top":"15%"});
                $(".address--delivery-address input").css({"padding-top":"1.1rem", "height":"3rem"});
            })

            $(".address--delivery-address input").focusout(function(){
                if($(".address--delivery-address input").val().trim() == ""){
                    $(".address--delivery-address label").css({"top":"35%"});
                    $(".address--delivery-address input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })

            $(".form--information--phone input").focusin(function(){
                $(".form--information--phone label").css({"top":"15%"});
                $(".form--information--phone input").css({"padding-top":"1.1rem", "height":"3rem"});
            })

            $(".form--information--phone input").focusout(function(){
                if($(".form--information--phone input").val().trim() == ""){
                    $(".form--information--phone label").css({"top":"35%"});
                    $(".form--information--phone input").css({"padding-top":"0rem", "height":"3rem"});
                }
            })
        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/user-info.css">
</style>
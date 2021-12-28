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

        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/user-info.css">
</style>
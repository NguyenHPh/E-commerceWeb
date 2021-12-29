<template>
     <div class="sign-up-wrapper">
            <div class="sign-up">
                <div class="sign-up--title">
                    <h1 style="text-align: center;">Change Password</h1>
                </div>
                <div class="sign-up-form">
                    <form @submit.prevent="submitForm">
                        <div class="form--last-name">
                            <p class = "last-name-label">Your username*</p>
                            <input type="text" v-model="username" required>
                        </div>
                        <div class="form--username">
                            <p class = "user-name-label">Your email address*</p>
                            <input type="email" v-model="email" required>
                        </div>
                        <div class="form--password">
                            <p class = "password-label">Your new password*</p>
                            <input type="password" v-model="password" required>
                        </div>

                        <div class="form--password">
                            <p class = "password-label">Repeat password*</p>
                            <input type="password" v-model="repassword" required>
                         </div>
                    
                        <div class="form-btn">
                            <button type="submit" name = "login-btn" class = "login-btn">Change Password</button>
                            <button type="submit" name = "sign-up-btn" class = "sign-up-btn">Cancel</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
</template>
<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: "ChangePassword",
    data(){
        return {
            username: "",
            email: "",
            password: "",
            repassword: ""
        }
    },
    mounted(){
        document.title = "Change Password"
    },
    methods:{
        validate(){
            this.errors = []
            if (this.username.length < 8) {
                this.errors.push('The username must be over 7 keywords')
            }
            if (this.password.length < 8) {
                this.errors.push('The password is too short')
            }
            if (this.password !== this.repassword) {
                this.errors.push('The passwords doesn\'t match')
            }
        },
        async submitForm(){
            this.$store.commit('setIsLoading', true)
            this.validate()
            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    email: this.email,
                    password: this.password
                }
                
                await axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                             console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }                    
                        })

                this.$store.commit('setIsLoading', false)
                
            }
            else{
                console.log(this.errors);
                toast({
                    message: 'failed',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })
            }
        }
    }
}
</script>
<style>
    @import "../assets/styles/sign-up-page.css";
</style>
<template>
     <div class="sign-up-wrapper">
            <div class="sign-up">
                <div class="sign-up--title">
                    <h1 style="text-align: center;">Sign up your account</h1>
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
                            <p class = "password-label">Your password*</p>
                            <input type="password" v-model="password" required>
                        </div>

                        <div class="form--password">
                            <p class = "password-label">Your password*</p>
                            <input type="password" v-model="repassword" required>
                         </div>
                        <div class="form--subcribe">
                            <input type="checkbox" v-model="subcribe">
                            <p class = "subcribe-label">Subcribe for our newsletter</p>
                        </div>
                        

                        <div class="form-btn">
                            <button type="submit" name = "login-btn" class = "login-btn">Sign up account</button>
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
    name: 'SignUp',
    data() {
        return{
            username:'',
            email: '',
            password: '',
            repassword: '',
            errors: [],
            passed: false



        }
    },
    methods: {
        validate(){
            this.errors = []
            if (this.username.length < 8) {
                this.errors.push('The username must be over 7 keywords')
            }
            if (this.password.length < 8) {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
        },
        async submitForm(){
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
            }
            else{
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
    },
    mounted(){
        document.title = "Sign Up";
    }
}
</script>
<style>
    @import "../assets/styles/sign-up-page.css";
</style>
<template>
     <div class="sign-up-wrapper">
            <div class="sign-up">
                <div class="sign-up--title">
                    <h1>Reactivate your account</h1>
                </div>
                <div class="sign-up--content">
                    <p>Please note we have recently made some changes to our website and as a result you will need to re-enter your details to access your account, it will only take a minute. You will receive a confirmation email.</p>
                </div>
                <div class="sign-up-form">
                    <form @submit.prevent="submitForm">
                        <div class="form--first-name">
                            <p class = "first-name-label">Your first name*</p>
                            <input type="text" v-model="firstName" required>
                        </div>
                        <div class="form--last-name">
                            <p class = "last-name-label">Your last name*</p>
                            <input type="text" v-model="lastName" required>
                        </div>
                        <div class="form--username">
                            <p class = "user-name-label">Your email address*</p>
                            <input type="text" v-model="email" required>
                        </div>
                        <div class="form--password">
                            <p class = "password-label">Your password*</p>
                            <input type="password" v-model="password" required>
                        </div>
                        <div class="form--subcribe">
                            <input type="checkbox" v-model="subcribe">
                            <p class = "subcribe-label">Subcribe for our newsletter</p>
                        </div>
                        

                        <div class="form-btn">
                            <button type="submit" name = "login-btn" class = "login-btn">Reactivate account</button>
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
            firstName:'',
            lastName: '',
            email: '',
            password: '',
            subcribe: false

        }
    },
    methods: {
        submitForm(){
            const formData = {
                firstName: this.firstName,
                lastName: this.lastName,
                email: this.email,
                password: this.password,
                subcribe: this.subcribe
            }
            axios
                .post('api/v1/users/', formData)
                .then(response => {
                    toast({
                        message: 'Account created please login',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/log-in')
                })
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
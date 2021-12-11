<template>
     <div class="login-wrapper">
            <div class="login">
                <div class="login--title">
                    <h1>Sign In</h1>
                </div>
                <div class="login--content">
                    <p>Please note we have recently made some changes to our website and as a result you will need to re-enter your details to access your account, it will only take a minute. Simply click the 'create account' button below, enter your details and we will email you with a reactivation link</p>
                </div>
                <div class="login-form">
                    <form @submit.prevent="submitForm">
                        <div class="form--username">
                            <p class = "user-name-label">Your username*</p>
                            <input type="text" name = "user-name" required v-model="username">
                        </div>
                        <div class="form--password">
                            <p class = "password-label">Your password*</p>
                            <input type="password" name = "user-password" required v-model="password">
                        </div>
                        <p class = "forgot-password"><a href="">forgot your password?</a></p>

                        <div class="form-btn">
                            <button type="submit" name = "login-btn" class = "login-btn">Log in</button>
                            <button type="submit" name = "sign-up-btn" class = "sign-up-btn">Create account</button>
                            
                        </div>
                    </form>
                </div>
            </div>
        </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                password: this.password,
                username: this.username
                
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    this.$router.push('/cart')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        console.log("wrong")
                    }
                })
        }
    }
}
</script>
<style>
    @import "../assets/styles/login-page.css";
</style>
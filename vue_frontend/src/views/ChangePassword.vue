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

        }
    },
    mounted(){
        document.title = "Change Password"
    }
}
</script>
<style>
    @import "../assets/styles/sign-up-page.css";
</style>
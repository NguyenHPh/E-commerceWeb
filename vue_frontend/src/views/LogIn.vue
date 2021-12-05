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
                    <form action="" method="post">
                        <div class="form--username">
                            <p class = "user-name-label">Your email address*</p>
                            <input type="text" name = "user-name" required>
                        </div>
                        <div class="form--password">
                            <p class = "password-label">Your password*</p>
                            <input type="password" name = "user-password" required>
                        </div>
                        <p class = "forgot-password"><a href="">forgot your password?</a></p>

                        <div class="form-btn">
                            <button type="submit" name = "login-btn" class = "login-btn">Sign in</button>
                            <button type="submit" name = "sign-up-btn" class = "sign-up-btn">Create account</button>
                            
                        </div>
                    </form>
                </div>
            </div>
        </div>
</template>

<script>

export default {
    name: 'LogIn',
    data() {

    },
    methods: {

    },
    mounted(){
        document.title = "Log In";
    }
}
</script>
<style>
    @import "../assets/styles/login-page.css";
</style>
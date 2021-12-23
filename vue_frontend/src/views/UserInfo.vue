<template>
<div class="user-info-page">
    <div class="wrappers">
        <div class = "user-info">
            <div class = "user-info-detail">
                <div class = "info">
                    <h1 id = "user-name">Nguyễn Hoàng Phương</h1>
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
                        <form action="" method="post">
                            <div class="form-information--email">
                                <label for="input">Email</label>
                                <input type="text" name="email">
                            </div>
                            <div class="form-information__address">
                                <div class="address--title">
                                    <p>User Information</p>
                                </div>
                                <div class="address__name">
                                    <div class="name--firstname">
                                        <label for="input">First name</label>
                                        <input type="text" v-model="user.firstName">
                                    </div>
                                    <div class="name--lastname">
                                        <label for="">Last name</label>
                                        <input type="text" v-model="user.lastName">
                                    </div>
                                </div>
                                <div class="address--delivery-address">
                                    <label for="">Address</label>
                                    <input type="text" v-model="user.address">
                                </div>
                            </div>
                            <div class="form--information--phone">
                                <label for="">Phone number</label>
                                <input type="text" v-model="user.phone">
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
import axios from 'axios'
export default {
    name: 'UserInfo',
    data() {
        return{
            user: ''
        }
    },
    mounted() {
        document.title = 'User Info'
        this.getUserInfo()
    },
    methods: {
        async getUserInfo(){
            await axios.get('/api/v1/userinfo')
                .then(response =>{
                    this.user = response.data
                })
                .catch(err =>{
                    console.log(err)
                })
        }
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/user-info.css">
</style>
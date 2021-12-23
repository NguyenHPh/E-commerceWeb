<template>
    <div class="profile">
            <div class="profile--wrapper">
                <div class="profile__my-account">
                    <div class="my-account--title">
                        <h1>My Account</h1>
                    </div>
                    <div class="my-account__button">
                        <div class="button--subcription">
                            <a href="">Manage Your Information</a>
                        </div>
                        <div class="button--log-out">
                            <a @click="logout()" class="log-out">log out</a>
                        </div>
                        <div class="button--change-password">
                            <a href="">change password</a>
                        </div>
                    </div>
                </div>
                <div class="profile__billing-detail">
                    <div class="billing-detail--title">
                        <p>Billing Details</p>
                    </div>
                    <div class="billing-detail__main">
                        <div class="billing-detail__main--content">
                            <p>You currently have no address saved</p>
                        </div>
                        <div class="billing-detail__main--button">
                            <a href="">Create address</a>
                        </div>
                    </div>
                </div>
                <div class="profile__order-history">
                    <div class="order-history--title">
                        <p>Order History</p>
                    </div>
                    <div class="order-history__main" v-if="orders.length == 0">
                        <div class="order-history__main--content">
                            <p>There are currently no orders in your order history.</p>
                        </div>
                        <div class="order-history__main--button">
                            <a href="">Shop now</a>
                        </div>
                    </div>
                    <div class="order-history__main" v-else>
                        <div class="order-history__main--content">
                            <div v-for="(order, index) in orders" :key="index" style="border: 1px solid blue;">
                                <p>First Name: {{ order.first_name }}</p>
                                <p>Last Name: {{ order.last_name }}</p>
                                <p>Address: {{ order.address }}</p>
                                <p>Order date: {{ order.created_at }}</p>
                                <p>Phone: {{ order.phone }}</p>
                                <p>Paid amount: {{ order.paid_amount }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="profile__refer-a-friend">
                    <div class="refer-a-friend--title">
                        <p>Refer a Friend</p>
                    </div>
                    <div class="refer-a-friend__banner">
                        <div class="refer-a-friend__banner-left">
                            <div class="banner-left--title">
                                <p>nguyen, give a friend 20% off their first order at forthglade.</p>
                            </div>
                            <div class="banner-left--small-tag">
                                <p>Our refer-a-friend programme is managed by Mention Me who will process your data and send you referral service emails. More info and your privacy rights.</p>
                            </div>
                            <div class="banner-left--button">
                                <a href="">give 20% off</a>
                            </div>
                            <div class="banner-left--small-tag-2">
                                <p>by accepting this offer you agree to the terms and conditions</p>
                            </div>
                        </div>
                        <div class="refer-a-friend__banner-right">

                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
import axios from 'axios'
    export default {
        name: "Profile",
        data(){
            return {
                orders: []
            }
        },
        mounted(){
            document.title = "Profile"
            this.getMyOrders()

        },
        methods: {
            logout() {
                axios.defaults.headers.common["Authorization"] = ""

                localStorage.removeItem("token")
                localStorage.removeItem("username")
                localStorage.removeItem("userid")
                this.$store.commit('removeToken')
                this.$router.push('/')
            },
            async getMyOrders() {
                this.$store.commit('setIsLoading', true)
                await axios
                    .get('/api/v1/orders/')
                    .then(response => {
                        this.orders = response.data
                        console.log(this.orders)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>
<style>
    @import "../assets/styles/Profile.css";
    .log-out:hover{
        cursor: pointer
    }
</style>
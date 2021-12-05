import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'


import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Cart from '../views/Cart.vue'
import About from '../views/About.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  // {
  //   path: '/my-account',
  //   name: 'MyAccount',
  //   component: MyAccount,
  //   meta: {
  //       requireLogin: true
  //   }
  // },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  // {
  //   path: '/cart/success',
  //   name: 'Success',
  //   component: Success
  // },
  // {
  //   path: '/cart/checkout',
  //   name: 'Checkout',
  //   component: Checkout,
  //   meta: {
  //       requireLogin: true
  //   }
  // }
]


//product/all
//product/:category

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router





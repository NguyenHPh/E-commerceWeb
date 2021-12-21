import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Cart from '../views/Cart.vue'
import About from '../views/About.vue'
import Advices from '../views/Advices.vue'
import Contact from '../views/Contact.vue'
import Category from '../views/Category.vue'
import Privacy from '../views/Privacy.vue'
import Term from '../views/Term.vue'
import Profile from '../views/Profile.vue'
import Product from '../views/Product.vue'
import ProductDetail from '../views/ProductDetail.vue'
import CheckOut from '../views/CheckOut.vue'





const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requireLogin: true
    }
  }
  ,
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
  {
    path: '/advices',
    name: 'Advices',
    component: Advices
  },
  {
    path: '/get-in-touch',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/collections',
    name: 'Category',
    component: Category
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: Privacy
  },
  {
    path: '/term',
    name: 'Term',
    component: Term
  },
  {
    path: '/collections/:category_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'ProductDetail',
    component: ProductDetail
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
  {
    path: '/cart/checkout',
    name: 'CheckOut',
    component: CheckOut,
    meta: {
        requireLogin: true
    }
  }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router





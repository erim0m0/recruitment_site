import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Signup from '../views/Sign_up.vue'
import Signin from '../views/Sign_in.vue'
import Verify from '../views/Verify.vue'
import ProfileUpdate from '../views/ProfileUpdate.vue'
import CoProfileUpdate from '../views/company/CoProfileUpdate.vue'
impo

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-in',
    name: 'Signin',
    component: Signin,
    meta: { loginRedirect: true }
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup,
    meta: { loginRedirect: true }
  },
  {
    path: '/verify',
    name: 'Verify',
    component: Verify,
  },
  {
    path: '/profile/update',
    name: 'ProfileUpdate',
    component: ProfileUpdate,
    meta: { loginRequired: true }
  },
  {
    path: '/company/profile/update',
    name: 'CoProfileUpdate',
    component: CoProfileUpdate,
    meta: { loginRequired: true }
  },
  {
    path: '/company/advertisement/new/',
    name: 'AdCreate',
    component: AdCreate,
    meta: { loginRequired: true }
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.loginRequired)) {
//     if (store.state.isAuthenticated) {
//       next()
//     } else {
//       next("/sign-in")
//     }
//   } else if (to.matched.some(record => record.meta.loginRedirect)) {
//     if (!store.state.isAuthenticated) {
//       next()
//     } else {
//       next("/")
//     }
//   } else {
//     next()
//   }
// })

export default router

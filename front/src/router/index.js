import { createRouter, createWebHistory } from 'vue-router'
import Home          from '../views/Home.vue'
import Signup        from '../views/Sign_up.vue'
import Signin        from '../views/Sign_in.vue'
import Verify        from '../views/Verify.vue'
import ProfileUpdate from '../views/ProfileUpdate.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-in',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup,
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
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Algorithm from '../views/Algorithm'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/algorithm',
    name: 'algorithm',
    component: Algorithm
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

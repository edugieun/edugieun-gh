import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Index'
import Algorithm from '../views/Algorithm'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
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
  routes
})

export default router

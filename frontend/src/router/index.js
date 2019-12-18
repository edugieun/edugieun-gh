import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Algorithm from '../views/Algorithm'
import AlgoDetail from '../views/AlgoDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  // Alogorithm
  {
    path: '/algorithm',
    name: 'algorithm',
    component: Algorithm
  },
  {
    path: '/algorithm/:id',
    name: 'detail',
    component: AlgoDetail,
    props: true
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

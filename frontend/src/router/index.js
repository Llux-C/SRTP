import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import( '../views/Home.vue')
  },
  {
    path: '/calculate',
    name: 'Calculate',
    component: () => import( '../views/Calculate.vue')
  },
  {
    path: '/check',
    name: 'Check',
    component: () => import( '../views/Check.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router

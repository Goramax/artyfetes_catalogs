import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    name: 'Catalog',
    path: '/catalogue/:catalogid',
    component: () => import('@/pages/Catalog.vue'),
  },
  {
    name: 'Universe',
    path: '/catalogue/:catalogid/univers/:universeid',
    component: () => import('@/pages/Universe.vue'),
  },
  {
    name: 'Login',
    path: '/connexion',
    component: () => import('@/pages/Login.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

export default router

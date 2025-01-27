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
    path: '/catalogue/:catalogid/universe/:universeid',
    component: () => import('@/pages/Universe.vue'),
  },
  {
    name: 'Item',
    path: '/catalogue/:catalogid/universe/:universeid/item/:itemid',
    component: () => import('@/pages/Item.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router

import { createRouter, createWebHistory } from 'vue-router'
import UserRegistration from '@/components/UserRegistration.vue'
import ChatApp from '@/components/ChatApp.vue'

const routes = [
  {
    path: '/',
    component: UserRegistration
  },
  {
    path: '/chat',
    component: ChatApp,
    props: route => ({ token: route.query.token })
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
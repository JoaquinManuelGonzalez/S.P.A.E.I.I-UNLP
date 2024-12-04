import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StudentPortalView from '@/views/StudentPortalView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'inicio',
      component: HomeView,
    },
    {
      path: '/portal-de-alumnos',
      name: 'portal-de-alumnos',
      component: StudentPortalView,
    }
  ],
})

export default router

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
      path: '/primer-formulario',
      name: 'primer-formulario',
      component: () => import('../components/PrimerFormulario.vue'),
    },
    {
      path: '/portal-de-alumnos',
      name: 'portal-de-alumnos',
      component: StudentPortalView,
    }
  ],
})

export default router

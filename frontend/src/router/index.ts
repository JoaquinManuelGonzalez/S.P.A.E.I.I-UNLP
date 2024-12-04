import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/primer-formulario',
      name: 'primer-formulario',
      component: () => import('../components/PrimerFormulario.vue'),
    },
    {
      path: '/segundo-formulario',
      name: 'segundo-formulario',
      component: () => import('../components/PrimerFormularioDos.vue'),
    }
  ],
})

export default router

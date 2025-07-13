import { createRouter, createWebHistory } from 'vue-router'
import RegisterPatient from '@/views/RegisterPatient.vue'
// import CreateOrder from '@/views/CreateOrder.vue'
import OrderHistory from '@/views/OrderHistory.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'RegisterPatient',
      component: RegisterPatient
    }, 
    {
      path: '/orden',
      name: 'CreateOrder',
      component: () => import('@/views/CreateOrder.vue')
    },
    {
      path: '/historial',
      name: 'OrderHistory',
      component: OrderHistory
    },
  ],
})

export default router

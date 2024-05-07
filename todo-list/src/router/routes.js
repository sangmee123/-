const routes = [
  { path: '/', component: () => import('pages/Login.vue') },
  { path: '/login', component: () => import('pages/TodoApp.vue') },
  { path: '/login/naver', component: () => import('pages/NaverAccess.vue') },
  { path: '/register', component: () => import('pages/Membership.vue') },
]

export default routes

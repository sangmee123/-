const routes = [
  {
    path: '/',
    component: () => import('layouts/index.vue'),
    children: [
      { path: '', component: () => import('pages/LoginNaver.vue') },
      { path: 'login', component: () => import('pages/Todo.vue')},
      { path: 'login/naver', component: () => import('pages/LoginAccess.vue')}
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes

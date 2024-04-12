const Login = () => import('pages/Login.vue');
const SignUp = () => import('pages/SignUp.vue');
const TodoList = () => import('pages/TodoList.vue');
const GoogleSheet = () => import('pages/GoogleSheet.vue');
const DataQueryingKEPCO = () => import('pages/DataQueryingKEPCO.vue');
const BackgroundTask = () => import('pages/BackgroundTask.vue');
const ScrollTest1 = () => import('pages/ScrollTest1.vue');
const ScrollTest2 = () => import('pages/ScrollTest2.vue');

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: '', path: '', component: Login },
      { name: 'signup', path: 'signup', component: SignUp },
      { name: 'todolist', path: 'todolist', component: TodoList },
      { name: 'googlesheet', path: 'googlesheet', component: GoogleSheet },
      { name: 'dataqueryingkepco', path: 'dataqueryingkepco', component: DataQueryingKEPCO },
      { name: 'backgroundtask', path: 'backgroundtask', component: BackgroundTask },
      { name: 'scrolltest1', path: 'scrolltest1', component: ScrollTest1 },
      { name: 'scrolltest2', path: 'scrolltest2', component: ScrollTest2 },
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes

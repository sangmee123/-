import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: (to, from) => {
      // name이 scrolltest인 경로이면서 query.page를 요청할 때만
      if (to.name === "scrolltest" && to.query.page) { 
          let yOffset;
          if (window.innerWidth < 767) {
              yOffset = 200; // 모바일
          } else if (window.innerWidth < 1200) {
              yOffset = 240; // 태블릿 
          } else {
              yOffset = 280; // 데스크톱 
          }
          return { x: 0, y: yOffset };
      }
      return { x: 0, y: 0 }; // 다음페이지는 항상 TOP-LEFT 로
  },
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  return Router
}

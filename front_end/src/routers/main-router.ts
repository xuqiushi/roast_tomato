/** @format */
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
const SigninPage = () => import(/* webpackChunkName: "signin" */ '@/views/SigninPage.vue')
const RegisterPage = () => import(/* webpackChunkName: "register" */ '@/views/RegisterPage.vue')
const BlogViewPage = () => import(/* webpackChunkName: "blog-view" */ '@/views/BlogViewPage.vue')
const BlogDetailPage = () => import(/* webpackChunkName: "blog-detail" */ '@/views/BlogDetailPage.vue')
export default new VueRouter({
  mode: 'history',
  // base: '/',
  routes: [
    {
      path: '/',
      name: 'index',
      redirect: '/blog/view'
    },
    {
      path: '/signin',
      name: 'SigninPage',
      component: SigninPage
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterPage
    },
    {
      path: '/blog/view',
      name: 'BlogViewPage',
      component: BlogViewPage
    },
    {
      path: '/blog/detail/:blogId',
      name: 'BlogDetailPage',
      component: BlogDetailPage
    }
  ]
})

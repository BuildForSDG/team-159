import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
  },
  {
    path: '/services',
    name: 'Service',
    component: () => import('../views/Services.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/SignIn.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/SignUp.vue'),
  },
  {
    path: '/support',
    name: 'Support',
    component: () => import('../views/Support.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;

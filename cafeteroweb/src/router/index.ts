import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router';

import Main from '@/modules/main/main.vue';
import Login from '@/modules/login/login.vue';
import Register from '@/modules/register/register.vue';

import Dashboard from '@/pages/dashboard/dashboard.vue';
import Profile from '@/pages/profile/profile.vue';
import Batch from '@/pages/batch/batch.vue';
import BatchAdd from '@/pages/batch/add/add.vue';
import Notify from '@/pages/notify/notify.vue';
import ForgotPassword from '@/modules/forgot-password/forgot-password.vue';
import RecoverPassword from '@/modules/recover-password/recover-password.vue';
import PrivacyPolicy from '@/modules/privacy-policy/privacy-policy.vue';
import store from '@/store/index';

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'Main',
        component: Main,
        meta: {
            requiresAuth: true
        },
        children: [
            {
                path: '',
                name: 'Dashboard',
                component: Dashboard,
                meta: {
                    requiresAuth: true
                }
            },
            {
                path: 'profile',
                name: 'Profile',
                component: Profile,
                meta: {
                    requiresAuth: true
                }
            },
            {
                path: 'batch',
                name: 'batch',
                component: Batch,
                meta: {
                    requiresAuth: true
                }
            },
            {
                path: 'batch-add',
                name: 'batch add',
                component: BatchAdd,
                meta: {
                    requiresAuth: true
                }
            },
            {
                path: 'notify',
                name: 'notify',
                component: Notify,
                meta: {
                    requiresAuth: true
                }
            }
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            requiresUnauth: true
        }
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: {
            requiresUnauth: true
        }
    },
    {
        path: '/forgot-password',
        name: 'ForgotPassword',
        component: ForgotPassword,
        meta: {
            requiresUnauth: true
        }
    },
    {
        path: '/recover-password',
        name: 'RecoverPassword',
        component: RecoverPassword,
        meta: {
            requiresUnauth: true
        }
    },
    {
        path: '/privacy-policy',
        name: 'RecoverPassword',
        component: PrivacyPolicy
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !store.getters.token) {
        next('/login');
    } else if (to.meta.requiresUnauth && !!store.getters.token) {
        next('/');
    } else {
        next();
    }
});

export default router;
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
import {library} from '@fortawesome/fontawesome-svg-core';
import {faLock, faEnvelope} from '@fortawesome/free-solid-svg-icons';
import {faFacebook, faGooglePlus} from '@fortawesome/free-brands-svg-icons';
import Toast, {PluginOptions} from 'vue-toastification';

import './index.scss';
import 'vue-toastification/dist/index.css';

library.add(faLock, faEnvelope, faFacebook, faGooglePlus);


const options: PluginOptions = {};

createApp(App)
    .component('font-awesome-icon', FontAwesomeIcon)
    .use(store)
    .use(router)
    .use(Toast, options)
    .mount('#app');

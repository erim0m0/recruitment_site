import { createApp } from 'vue'
import axios  from 'axios'
import App    from './App.vue'
import router from './router'
import store  from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js';
import 'popper.js/dist/popper.min.js';
import 'bootstrap/dist/js/bootstrap.min.js'


const data = JSON.parse(localStorage.getItem("user_auth"));
axios.defaults.headers.common['Authorization'] = "Bearer " + data.access
axios.defaults.baseURL = 'http://127.0.0.1:8000';
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

createApp(App).use(store).use(router).mount('#app')

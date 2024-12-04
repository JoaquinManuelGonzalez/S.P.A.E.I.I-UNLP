import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './index.css'
import 'flowbite';
import { i18n } from './plugins/i18n'

const app = createApp(App)

app.use(router)
app.use(i18n)
app.mount('#app')

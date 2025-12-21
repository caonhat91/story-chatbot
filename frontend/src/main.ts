import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { focusSlash } from './directives/v-focus-slash'

const app = createApp(App)

app.use(router)
app.directive("focus-slash", focusSlash)

app.mount('#app')

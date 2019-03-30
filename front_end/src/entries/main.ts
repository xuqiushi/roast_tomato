/** @format */

import Vue from 'vue'
import index from '../index/Index.vue'
import store from '../stores/main-store'
import axios from 'axios'
import router from '../routers/main-router'

import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faTimes,
  faPencilAlt,
  faTimesCircle,
  faCheck,
  faPlusCircle,
} from '@fortawesome/free-solid-svg-icons'
import { faHtml5 } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faTimes, faPencilAlt, faTimesCircle, faCheck, faPlusCircle, faHtml5)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.prototype.$http = axios
// import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import '../scss/custom.scss'
import '../scss/custom-code-mirror.scss'
// import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css'
import 'bootstrap/js/dist/util'
import 'bootstrap/js/dist/scrollspy';
import 'codemirror/mode/markdown/markdown';
// import { start_mock } from '../mock/main-mock'
// start_mock()
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(index)
}).$mount('#roast_tomato')

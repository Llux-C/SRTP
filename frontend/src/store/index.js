import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    chosenSensor:"1000A",
    chosenCity:"",
    chosenDate:"",
    chosenWaste:"",
    fill:0,
    time:0,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})

import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    user: '',
  },
  getters: {
  },
  mutations: {
    login(state, user) {
      state.isAuthenticated = true
      state.user = user
      localStorage.setItem('user_auth', JSON.stringify(user));
      axios.defaults.headers.common['Authorization'] = "Bearer " + user.access
    },
    logout(state) {
      state.isAuthenticated = false
      state.user = ''
      localStorage.removeItem("user_auth")
      // localStorage.removeItem("userPhone")
      axios.defaults.headers.common['Authorization'] = ""
    },
  },
  actions: {
    onStart(context) {
      let getUser = localStorage.getItem("user_auth")
      const userData = JSON.parse(getUser)

      if (getUser) {
        axios
          .post('/account/api/token/verify/', {
            token: userData.access
          })
          .then(response => {
            context.commit('login', userData)
            console.log(response.status);
          })
          .catch(error => {
            console.log(error.response);
            axios
              .post('/account/api/token/refresh/', {
                refresh: userData.refresh
              })
              .then(response => {
                userData.access = response.data.access
                context.commit('login', userData)
              })
              .catch(error => {
                context.commit('logout')  
              })
          })
      } else {
        context.commit('logout')
      }
    }
  }
})

const state = {
    isLoading: false, // 全局 Loading 状态
  };
  
  const mutations = {
    setLoading(state, status) {
      state.isLoading = status; // 更新状态
    },
  };
  
  const actions = {
    startLoading({ commit }) {
      commit('setLoading', true);
    },
    stopLoading({ commit }) {
      commit('setLoading', false);
    },
  };
  
  export default {
    namespaced: true,
    state,
    mutations,
    actions,
  };
  
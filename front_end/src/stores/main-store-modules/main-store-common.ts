interface State {
    warningMessages: string[]
}
const state: State = {
    warningMessages: []
};

const mutations = {
    updateWarningMessages: (state: State, value: string[]) => {
        state.warningMessages = value
    },
    addWarningMessage: (state: State, message: string) => {
        state.warningMessages.push(message)
    },
    deleteWarningMessage: (state: State, index: number) => {
        // console.log(state.warningMessages)
        state.warningMessages.splice(index, 1)
        // console.log(state.warningMessages)
    },
    deleteAllWarningMessages: (state: State) => {
        state.warningMessages.splice(0, state.warningMessages.length)
    }
};

const common = {
    namespaced: true,
    state(){
        return state},
    mutations: mutations
};

export default common
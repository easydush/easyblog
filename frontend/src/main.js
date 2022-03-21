import {createApp} from 'vue'
import App from './App.vue'
import Vuex from "vuex";
import axios from "axios";
import {getFakeComment, getFakePost} from "@/utils";


const store = new Vuex.Store({
    state: {
        posts: [],
        style: '',
    },
    actions: {
        loadPosts: function ({commit}) {
            axios.get(`http://localhost:8000/posts`).then((response) => {
                commit('SET_POSTS_LIST', {posts: response.data})
            }, (err) => {
                console.log(err)
            })
        },
        addPost: function () {
            axios.post(`http://localhost:8000/posts/`, getFakePost()).then(
                () => store.dispatch('loadPosts', this.state.style)
                , (err) => {
                    console.log(err)
                })
        },
        /* eslint-disable */
        addComment: function ({commit}, {id, isPost}) {
            console.log(id, isPost)
            axios.post(`http://localhost:8000/comments/`, getFakeComment(id, isPost)).then(
                () => store.dispatch('loadPosts', this.state.style)
                , (err) => {
                    console.log(err)
                })
        },
        deletePost: function ({commit}, id) {
            console.log(id)
            axios.delete(`http://localhost:8000/posts/${id}`).then(
                () => store.dispatch('loadPosts', this.state.style)
                , (err) => {
                    console.log(err)
                })
        },
        deleteComment: function ({commit}, id) {
            axios.delete(`http://localhost:8000/comments/${id}`).then(
                () => store.dispatch('loadPosts', this.state.style)
                , (err) => {
                    console.log(err)
                })
        }
    },
    mutations: {
        SET_POSTS_LIST: (state, {posts}) => {
            state.posts = posts
        },
    },
    getters: {
        posts: (state) => {
            return state.posts
        }
    }
})

createApp(App).use(store).mount('#app')
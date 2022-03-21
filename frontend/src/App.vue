<template>
  <div id="app">
    <header>
      <h1>Blog</h1>
    </header>
    <main>
      <div class="content">
        <div v-for="post in posts" v-bind:key="post.name">
          <div class="post">
            <span class="name">{{ post.title }}</span>
            <button class="button" @click="deleteP(post.id)">X</button>
            <button class="button" @click="addCom({id: post.id, isPost: true})">+ comment</button>
            <br/>
            <span>{{ post.description }}</span>
            <br/>
            <div class="comments" v-for="comment in post.comments" v-bind:key="comment.id">
              --> {{ comment.text }}
              <button class="button" @click="deleteCom(comment.id)">X</button>
              <button class="button" @click="addCom({id: post.id, isPost: false})">+ comment</button>
              <div class="comments" v-for="child in comment.children" v-bind:key="child.id">
                --> {{ child.text }}
                <button class="button" @click="deleteCom(comment.id)">X</button>
              </div>
            </div>
          </div>
        </div>
        <div v-if="posts.length < 1">
          <span>No posts</span>
        </div>
        <div class="controls">
          <button class="add" @click="add">Add post</button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  computed: {
    ...mapGetters(["posts"])
  },
  methods: {
    ...mapActions({
      addPost: 'addPost',
      deletePost: 'deletePost',
      addComment: 'addComment',
      deleteComment: 'deleteComment',
      loadPosts: 'loadPosts',
    }),
    add() {
      this.addPost()
    },
    deleteP(id) {
      this.deletePost(id)
    },
    addCom(data) {
      this.addComment(data)
    },
    deleteCom(id) {
      this.deleteComment(id)
    },
  },
  created() {
    this.loadPosts()
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: sans-serif;
  background: lightcyan;
  background: radial-gradient(circle, darkcyan, cadetblue);
}

header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background-color: #212121;
  color: #FFF;
}

main {
  width: 100%;
  max-width: 768px;
  margin: 0 auto;
  padding: 25px;
}

button {
  appearance: none;
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}

button:hover {
  opacity: 0.8;
}

.post {
  margin-bottom: 20px;
}

.button {
  margin-left: 20px;
}

.name {
  color: lightcyan;
  padding-right: 5px;
}

.controls {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px 15px;
}

.comments {
  margin-left: 10px;
}

.add {
  font-size: 16px;
  font-weight: 700;
  padding: 10px 20px;
  margin: 0 15px;
  border-radius: 6px;
  color: #FFF;
  background-color: lightseagreen;
}
</style>
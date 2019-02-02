<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <BlogCodeMirror></BlogCodeMirror>
    </div>
    <footer></footer>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import MainNavBar from "@/components/MainNavBar.vue";
import Footer from "@/components/Footer.vue";
import BlogCodeMirror from "@/components/BlogCodeMirror.vue";

@Component({
  components: { MainNavBar, Footer, BlogCodeMirror }
})
export default class BlogCreatePage extends Vue {}
</script>

<style scoped></style>

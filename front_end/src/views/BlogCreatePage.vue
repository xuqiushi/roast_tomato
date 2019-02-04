<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <BlogCodeMirror @send-blog-structure="setBlogStructure"></BlogCodeMirror>
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
import { BlogCodeMirrorStructure } from "../../typings/blogInterfaces";
@Component({
  components: { MainNavBar, Footer, BlogCodeMirror }
})
export default class BlogCreatePage extends Vue {
  blogTitle = "";
  blogSummary = "";
  blogContent = "";
  setBlogStructure(blogStructure: BlogCodeMirrorStructure) {
    this.blogTitle = blogStructure.codeTitle;
    this.blogSummary = blogStructure.codeSummary;
    this.blogContent = blogStructure.codeContent;
  }
}
</script>

<style scoped></style>

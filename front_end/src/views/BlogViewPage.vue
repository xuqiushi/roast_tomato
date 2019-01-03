<template>
  <div>
    <MainNavBar />
    <div class="container">
      <div class="row mt-5">
        <div class="col">
          <BlogPreviewList :preview-blog-list="previewBlogList" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import MainNavBar from "@/components/MainNavBar.vue";
import BlogPreviewList from "@/components/BlogPreviewList.vue";
import Vue from "vue";
import { Component } from "vue-property-decorator";
import { PreviewBlogContent } from "../../typings/blogInterfaces";
@Component({
  components: { MainNavBar, BlogPreviewList }
})
export default class BlogViewPage extends Vue {
  previewBlogList: PreviewBlogContent[] = [
    {
      id: "4215342",
      name: "test",
      summary: "test",
      createAt: 1454502
    },
    {
      id: "4215342",
      name: "test",
      summary: "test",
      createAt: 1454502
    }
  ];
}
</script>

<style scoped></style>

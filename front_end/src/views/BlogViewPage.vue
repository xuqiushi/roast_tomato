<template>
  <div>
    <MainNavBar />
    <div class="container-fluid">
      <div class="row d-flex flex-xl-nowrap mt-5 ml-5">
        <div class="d-flex justify-content-center col-12 col-md-9 col-xl-10 py-md-3 pl-md-5">
          <BlogPreviewList :preview-blog-list="previewBlogList" />
        </div>
        <div class="col-12 col-md-3 col-xl-2">
          <BlogPreviewListIndex :preview-blog-list="previewBlogList" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import MainNavBar from "@/components/MainNavBar.vue";
import BlogPreviewList from "@/components/BlogPreviewList.vue";
import BlogPreviewListIndex from "@/components/BlogPreviewListIndex.vue";
import Vue from "vue";
import { Component } from "vue-property-decorator";
import { PreviewBlogContent } from "../../typings/blogInterfaces";
@Component({
  components: { MainNavBar, BlogPreviewList, BlogPreviewListIndex }
})
export default class BlogViewPage extends Vue {
  previewBlogList: PreviewBlogContent[] = [];
  testData = {};
  created(){
    let body = $('body')
    body.addClass('scrolling')
    body.scrollspy({
      target: '#blog-list',
      offset: 100
    })
  }
  mounted() {
    this.$http({
      method: "post",
      url: "/api/blog_list"
    }).then(response => {
      this.previewBlogList = response.data.previewBlogList;
    });
  }
}
</script>

<style scoped>

</style>

<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <div class="row d-flex flex-xl-nowrap mt-5 ml-5">
        <div
          class="d-flex justify-content-center col-12 col-md-9 col-xl-10 py-md-3 pl-md-5"
        >
          <div>
            <BlogPreviewList
              :preview-blog-list="previewBlogList"
            ></BlogPreviewList>
            <Pagination
              :pagination-structure="paginationPara"
              @emit-blog-pagination="changeCurrentPage"
            ></Pagination>
          </div>
        </div>
        <div class="col-12 col-md-3 col-xl-2">
          <BlogPreviewListIndex
            :preview-blog-list="previewBlogList"
          ></BlogPreviewListIndex>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script lang="ts">
import MainNavBar from "@/components/MainNavBar.vue";
import BlogPreviewList from "@/components/BlogPreviewList.vue";
import BlogPreviewListIndex from "@/components/BlogPreviewListIndex.vue";
import Pagination from "@/components/Pagination.vue";
import Footer from "@/components/Footer.vue";
import Vue from "vue";
import { Component } from "vue-property-decorator";
import { PreviewBlogContent } from "../../typings/blogInterfaces";
@Component({
  components: {
    MainNavBar,
    BlogPreviewList,
    BlogPreviewListIndex,
    Pagination,
    Footer
  }
})
export default class BlogViewPage extends Vue {
  previewBlogList: PreviewBlogContent[] = [];
  paginationPara = {
    countAll: 1,
    selectNow: 1
  };
  created() {
    let body = $("body");
    body.addClass("scrolling");
    body.scrollspy({
      target: "#blog-list",
      offset: 100
    });
  }
  mounted() {
    this.$http({
      method: "post",
      url: "/api/blog_list",
      data: this.paginationPara.selectNow
    }).then(response => {
      this.previewBlogList = response.data.previewBlogList;
    });
    this.$http({
      method: "post",
      url: "api/get_blog_pagination_count"
    }).then(response => {
      this.paginationPara.countAll = response.data.countAll;
    });
  }
  changeCurrentPage(pageNumber: number) {
    this.paginationPara.selectNow = pageNumber;
  }
}
</script>

<style scoped></style>

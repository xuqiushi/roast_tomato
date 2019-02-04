<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-sm-12 col-md-12 col-lg-12 mt-5">
          <BlogManageList
            :blog-manage-records="blogManageRecords"
          ></BlogManageList>
          <Pagination
            class="mt-2"
            :pagination-structure="paginationPara"
            @emit-blog-pagination="changeCurrentPage"
          ></Pagination>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import MainNavBar from "@/components/MainNavBar.vue";
import Footer from "@/components/Footer.vue";
import BlogManageList from "@/components/BlogManageList.vue";
import Pagination from "@/components/Pagination.vue";
import { BlogManageRecord } from "../../typings/blogInterfaces";
@Component({
  components: {
    MainNavBar,
    Footer,
    BlogManageList,
    Pagination
  }
})
export default class BlogManagePage extends Vue {
  blogManageRecords: BlogManageRecord[] = [];
  paginationPara = {
    countAll: 1,
    selectNow: 1
  };
  mounted() {
    this.$http({
      method: "post",
      url: "api/blog/manage/get_list"
    }).then(response => {
      this.blogManageRecords = response.data["blogManageRecords"];
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

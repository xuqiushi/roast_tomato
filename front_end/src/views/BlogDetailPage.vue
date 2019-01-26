<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <div class="row d-flex flex-xl-nowrap mt-5 ml-5">
        <div
          class="d-flex justify-content-center col-12 col-md-8 col-xl-9 py-md-3 pl-md-5"
        >
          <div>
            <BlogDetailCard :blog-detail="blogDetail"></BlogDetailCard>
            <hr>
            <BlogCommentInput :user-info="currentUserInfo"></BlogCommentInput>
            <hr>
            <BlogCommentList
              :blog-comment-list="blogCommentList"
            ></BlogCommentList>
          </div>
        </div>
        <div class="col-12 col-md-4 col-xl-3">
          <div
            class="card"
            style="width: 18rem;"
          >
            <img
              class="card-img-top rounded-circle"
              :src="userInfo.userMainImage"
              alt="Card image cap"
            >
            <div class="card-body">
              <h5
                class="card-title text-center"
                v-text="userInfo.userName"
              ></h5>
            </div>
          </div>
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
import BlogDetailCard from "@/components/BlogDetailCard.vue";
import BlogCommentInput from "@/components/BlogCommentInput.vue";
import BlogCommentList from "@/components/BlogCommentList.vue";
import { User } from "../../typings/userInterfaces";
import { BlogComment } from "../../typings/blogInterfaces";
@Component({
  components: {
    BlogDetailCard,
    MainNavBar,
    Footer,
    BlogCommentInput,
    BlogCommentList
  }
})
export default class BlogDetailPage extends Vue {
  blogDetail = {
    id: "",
    name: "",
    content: "",
    userId: "",
    createAt: 0
  };
  userInfo: User = {
    id: "",
    userName: "",
    userMainImage: ""
  };
  currentUserInfo: User = {
    id: "",
    userName: "",
    userMainImage: ""
  };
  blogCommentList: BlogComment[] = [
    {
      id: "",
      content: "",
      userId: "",
      userName: "",
      userMainImage: "",
      creatAt: 0
    }
  ];
  mounted() {
    this.$http({
      method: "post",
      url: "/api/blog/" + this.$route.params.blogId
    })
      .then(response => {
        this.blogDetail = response.data;
      })
      .then(() => {
        this.$http({
          method: "post",
          url: "/api/users/" + this.blogDetail.userId
        }).then(response => {
          this.userInfo = response.data;
        });
      });
    this.$http({
      method: "post",
      url: "/api/users/current_user"
    }).then(response => {
      this.currentUserInfo = response.data;
    });
    this.$http({
      method: "post",
      url: "/api/blog_comment/" + this.blogDetail.id
    }).then(response => {
      this.blogCommentList = response.data;
    });
  }
}
</script>

<style scoped></style>

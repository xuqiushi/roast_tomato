<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <div class="row d-flex flex-xl-nowrap mt-5 ml-5">
        <div
          class="d-flex justify-content-center col-12 col-md-8 col-xl-9 py-md-3 pl-md-5"
        >
          <div><BlogDetailCard :blog-detail="blogDetail"></BlogDetailCard></div>
        </div>
        <div class="col-12 col-md-4 col-xl-3">
          <div
            class="card"
            style="width: 18rem;"
          >
            <img
              class="card-img-top"
              :src="userInfo.userMainImage"
              alt="Card image cap"
            >
            <div class="card-body">
              <h5
                class="card-title"
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
import { User } from "../../typings/userInterfaces";
@Component({
  components: { BlogDetailCard, MainNavBar, Footer }
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
  }
}
</script>

<style scoped></style>

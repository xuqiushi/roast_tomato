<template>
  <BlogDetailCard :blog-detail="blogDetail"></BlogDetailCard>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import BlogDetailCard from "@/components/BlogDetailCard.vue";
@Component({
  components: { BlogDetailCard }
})
export default class BlogDetailPage extends Vue {
  blogDetail = {
    id: "",
    name: "",
    content: "",
    createAt: 0
  };
  mounted() {
    this.$http({
      method: "post",
      url: "/api/blog/" + this.$route.params.blogId
    }).then(response => {
      this.blogDetail = response.data;
    });
  }
}
</script>

<style scoped></style>

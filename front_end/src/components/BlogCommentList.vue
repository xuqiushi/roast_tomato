<template>
  <div>
    <h3>最新评论</h3>
    <ul class="list-group list-group-flush">
      <li
        v-for="blogComment in blogCommentList"
        :key="blogComment.id"
        class="list-group-item d-flex align-items-center"
      >
        <div class="img-thumbnail mr-1">
          <img
            class="rounded-circle"
            alt="用户头像"
            width="50"
            height="50"
            :src="blogComment.userMainImage"
          >
        </div>
        <div>
          <div
            class="d-flex align-items-center user-name"
            v-text="blogComment.userName"
          ></div>
        </div>
        <div class="d-flex align-items-center">
          <div
            class="ml-1"
            v-text="blogComment.createAt"
          ></div>
          <div
            class="ml-1"
            v-text="blogComment.content"
          ></div>
        </div>
      </li>
      <li class="list-group-item d-flex align-items-center">
        <p
          v-if="blogCommentList.length === 0"
          v-text="'还没有人评论...'"
        ></p>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import { BlogComment } from "../../typings/blogInterfaces";

@Component
export default class BlogCommentList extends Vue {
  @Prop({
    default: () => {
      return [
        {
          id: "",
          content: "",
          userId: "",
          userName: "",
          userMainImage: "",
          creatAt: ""
        }
      ];
    },
    required: true,
    type: Array
  })
  blogCommentList!: BlogComment[];
}
</script>

<style scoped>
li {
  border: 0;
}
.user-name {
  font-size: 1.5rem;
}
</style>

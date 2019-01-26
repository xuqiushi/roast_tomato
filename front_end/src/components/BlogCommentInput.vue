<template>
  <div>
    <h3>发表评论</h3>

    <div class="mt-3">
      <div class="card">
        <div class="card-header d-flex align-items-center">
          <div class="img-thumbnail mr-1">
            <img
              class="rounded-circle"
              alt="用户头像"
              width="50"
              height="50"
              :src="userInfo.userMainImage"
            >
          </div>
          <div class="ml-1">
            <h4
              class=""
              v-text="userInfo.userName"
            ></h4>
          </div>
        </div>
      </div>
      <div class="mt-3">
        <form class="ml-3 mr-3">
          <div class="form-group">
            <textarea
              class="form-control"
              rows="6"
              placeholder="说点什么吧"
              style="width:100%;resize:none;"
            ></textarea>
          </div>
          <div>
            <button
              type="submit"
              class="btn btn-primary btn-lg btn3d"
            >
              <i class=""></i> 发表评论
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import { User } from "../../typings/userInterfaces";

@Component
export default class BlogCommentInput extends Vue {
  @Prop({
    default: () => {
      return {
        userName: "",
        userId: "",
        userMainImage: ""
      };
    },
    required: true,
    type: Object
  })
  userInfo!: User;
}
</script>

<style scoped></style>

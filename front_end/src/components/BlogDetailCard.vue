<template>
  <div>
    <h5 v-text="blogDetail.name"></h5>
    <p><small v-text="'发表于' + blogDetail.createAt"></small></p>
    <p v-text="blogDetail.content"></p>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import { BlogDetail } from "../../typings/blogInterfaces";
@Component
export default class BlogDetailCard extends Vue {
  @Prop({
    type: Object,
    default: () => {
      return {};
    },
    required: true
  })
  blogDetail!: BlogDetail;
}
</script>

<style scoped></style>

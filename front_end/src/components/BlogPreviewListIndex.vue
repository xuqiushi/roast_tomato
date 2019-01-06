<template>
  <nav class="bd-toc list-group-flush">
    <div
      id="blog-list"
    >
      <a
        v-for="(value, previewBlogIndex) in previewBlogList"
        :key="value + previewBlogIndex"
        :href="'#blog-list' + previewBlogIndex"
        class="list-group-item list-group-item-action"
        v-text="previewBlogList[previewBlogIndex].name"
      />
    </div>
  </nav>
</template>

<script lang="ts">
import { Component, Prop } from "vue-property-decorator";
import Vue from "vue";
import { PreviewBlogContent } from "../../typings/blogInterfaces";
@Component
export default class BlogPreviewListIndex extends Vue {
  @Prop({
    type: Array,
    required: true,
    default: []
  })
  previewBlogList!: PreviewBlogContent[];
}
</script>

<style scoped>
  .bd-toc {
    position: sticky;
    top: 4rem;
    height: calc(100vh - 4rem);
    overflow-y: auto;
    order: 2;
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    font-size: .875rem;
  }
</style>

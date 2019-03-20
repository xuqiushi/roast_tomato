<template>
  <div class="row">
    <div class="col-12">
      <div
        v-for="(value, previewBlogIndex) in previewBlogList"
        :key="value + previewBlogIndex"
      >
        <div class="card mb-3">
          <h2 class="card-title">
            <RouterLink
              :to="{
                name: 'BlogDetailPage',
                params: { blogId: previewBlogList[previewBlogIndex].id }
              }"
            >
              <a
                :id="'blog-list' + previewBlogIndex"
                v-text="previewBlogList[previewBlogIndex].name"
              ></a>
            </RouterLink>
          </h2>
          <p>
            <small
              v-text="'发表于' + previewBlogList[previewBlogIndex].createAt"
            ></small>
          </p>
          <p
            class="card-text"
            v-text="previewBlogList[previewBlogIndex].summary"
          ></p>
          <p>
            <a
              :href="'/blog/' + previewBlogList[previewBlogIndex].id"
              v-text="'继续阅读'"
            ></a>
            <i class="uk-icon-angle-double-right"></i>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop } from "vue-property-decorator";
import Vue from "vue";
import { PreviewBlogContent } from "../../typings/blogInterfaces";
@Component
export default class BlogPreviewList extends Vue {
  @Prop({
    type: Array,
    required: true,
    default: ()=>{return []}
  })
  previewBlogList!: PreviewBlogContent[];
}
</script>

<style scoped>
.card {
  border: 0;
}
</style>

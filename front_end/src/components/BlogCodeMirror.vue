<template>
  <div class="ml-3 mr-3 mt-3">
    <form>
      <div class="form-group row">
        <label for="code-title">
          标题
        </label>
        <input
          id="code-title"
          v-model="codeTitle"
          class="form-control"
          placeholder="标题"
        >
      </div>
      <div class="form-group row">
        <label for="code-summary">
          摘要
        </label>
        <textarea
          id="code-summary"
          v-model="codeSummary"
          class="form-control"
          rows="3"
        ></textarea>
      </div>
      <CommonEditor
        class="form-group row"
        @send-editor-value="setCodeContent"
      >
      </CommonEditor>
      <div class="form-group row justify-content-center">
        <button
          type="button"
          class="btn btn-primary btn-lg btn3d mr-5"
          @click="createBlog"
        >
          确定
        </button>
        <button
          type="button"
          class="btn btn-danger btn-lg btn3d ml-5"
        >
          取消
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch, Emit } from "vue-property-decorator";
import CommonEditor from "@/components/CommonEditor.vue";

@Component({
  components: {
    CommonEditor
  }
})
export default class BlogCodeMirror extends Vue {
  codeTitle = "";
  codeSummary = "";
  codeContent = "";
  setCodeContent(content: string) {
    this.codeContent = content;
  }
  @Emit("send-blog-structure")
  sendBlogStructure() {
    return {
      codeTitle: this.codeTitle,
      codeSummary: this.codeSummary,
      codeContent: this.codeContent
    };
  }
  @Watch("codeTitle")
  onCodeTitleChange() {
    this.sendBlogStructure();
  }
  @Watch("codeSummary")
  onCodeSummaryChange() {
    this.sendBlogStructure();
  }
  @Watch("codeContent")
  onCodeContentChange() {
    this.sendBlogStructure();
  }
  createBlog() {
    let postData = {
      name: this.codeTitle,
      summary: this.codeSummary,
      content: this.codeContent
    };
    this.$http({
      method: "post",
      url: "/api/blog/create",
      data: postData
    });
  }
}
</script>

<style scoped></style>

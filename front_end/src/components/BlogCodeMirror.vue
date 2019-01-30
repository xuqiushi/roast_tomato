<template>
  <div class="ml-3 mr-3 mt-3">
    <form>
      <div class="form-group row">
        <label for="code-title">
          标题
        </label>
        <input
          id="code-title"
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
          class="form-control"
          rows="3"
        ></textarea>
      </div>
      <div class="form-group row">
        <label for="code-content">
          内容
        </label>
        <textarea
          id="code-content"
          ref="codeContent"
          rows="5"
        ></textarea>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import CodeMirror from "codemirror";

@Component
export default class BlogCodeMirror extends Vue {
  testContent = "";
  mounted() {
    let editor = CodeMirror.fromTextArea(
      this.$refs.codeContent as HTMLTextAreaElement,
      {
        lineNumbers: true,
        mode: "html"
      }
    );
    editor.on("change", () => {
      this.testContent = editor.getValue();
    });
  }
}
</script>

<style scoped></style>

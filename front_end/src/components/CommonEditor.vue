<template>
  <div class="row">
    <div class="col">
      <div class="card">
        <div class="card-body">
          <label for="code-content">
          </label>
          <textarea
            id="code-content"
            ref="textContent"
            rows="5"
          ></textarea>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-body">
          <div class="mt-3 pt-2">
            <p
              ref="codePreview"
              class="card-text"
            ></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import CodeMirror from "codemirror";
import marked from "marked";
@Component
export default class CommonEditor extends Vue {
  testContent = "";
  public $refs!: {
    codePreview: HTMLElement;
    textContent: HTMLTextAreaElement;
  };
  mounted() {
    let editor = CodeMirror.fromTextArea(
      this.$refs.textContent as HTMLTextAreaElement,
      {
        lineNumbers: true,
        theme: "base16-light",
        mode: {
          name: "text/x-markdown",
          highlightFormatting: true,
          allowAtxHeaderWithoutSpace: true
        }
      }
    );
    editor.on("change", () => {
      this.testContent = editor.getValue();
      this.$refs.codePreview.innerHTML = marked(this.testContent);
      this.$emit("send-editor-value", this.testContent);
    });
  }
}
</script>

<style scoped>
.card {
  height: 500px;
  border: 0;
}
.card-body {
  border-radius: 0.25rem;
  border-right: solid gray;
  border-left: solid gray;
}
</style>

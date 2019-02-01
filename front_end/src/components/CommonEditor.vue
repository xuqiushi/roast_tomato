<template>
  <div class="row">
    <div class="col">
      <label for="code-content">
      </label>
      <textarea
        id="code-content"
        ref="textContent"
        rows="5"
      ></textarea>
    </div>
  </div>
</template>

<script lang='ts'>
  import Vue from 'vue'
  import {Component} from 'vue-property-decorator'
  import CodeMirror from "codemirror";
  @Component
  export default class CommonEditor extends Vue {
    testContent = "";
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
      });
    }
  }
</script>

<style scoped>

</style>
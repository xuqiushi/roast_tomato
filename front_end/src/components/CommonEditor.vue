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
    <div class="col">
      <div>
        <p
          ref="codePreview"
        >
        </p>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
  import Vue from 'vue'
  import {Component} from 'vue-property-decorator'
  import CodeMirror from "codemirror";
  import marked from 'marked'
  @Component
  export default class CommonEditor extends Vue {
    testContent = "";
    public $refs!: {
      codePreview: HTMLElement
      textContent: HTMLTextAreaElement
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
        this.$refs.codePreview.innerHTML = marked(this.testContent)
      });
    }
  }
</script>

<style scoped>

</style>
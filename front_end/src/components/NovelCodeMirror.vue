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
      <CommonEditor class="form-group row">
      </CommonEditor>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import CommonEditor from "@/components/CommonEditor.vue";

@Component({
  components: {
    CommonEditor
  }
})
export default class NovelCodeMirror extends Vue {}
</script>

<style scoped></style>

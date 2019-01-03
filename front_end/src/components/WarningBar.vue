<template>
  <div>
    <div
      v-for="(data, index) in warningMessages"
      :key="data + index"
      class="alert alert-warning alert-dismissible fade show"
      role="alert"
    >
      <strong v-text="warningMessages[index]" />
      <button
        type="button"
        class="close"
        @click="closeOneMessage(index)"
      >
        <span> &times; </span>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Watch } from "vue-property-decorator";
@Component
export default class WarningBar extends Vue {
  get warningMessages(): string[] {
    return this.$store.state.common.warningMessages;
  }
  closeOneMessage(index: number) {
    this.warningMessages.splice(index, 1);
  }
  @Watch("warningMessages")
  updateStoreWarning(newVal: string[]) {
    this.$store.commit("common/updateWarningMessages", newVal);
  }
}
</script>

<style scoped></style>

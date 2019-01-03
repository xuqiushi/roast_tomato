<template>
  <div><SigninForm /></div>
</template>

<script lang="ts">
import SigninForm from "@/components/SigninForm.vue";
import Vue from "vue";

import { Component } from "vue-property-decorator";

@Component({
  components: { SigninForm }
})
export default class SigninPage extends Vue {}
</script>

<style scoped>
div {
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}
</style>

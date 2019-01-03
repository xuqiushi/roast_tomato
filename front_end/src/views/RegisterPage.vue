<template>
  <div><RegisterForm /></div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import RegisterForm from "@/components/RegisterForm.vue";
@Component({
  components: { RegisterForm }
})
export default class RegisterPage extends Vue {}
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

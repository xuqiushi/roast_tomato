<template>
  <div class="footer">
    <div>
      <div>
        <p class="text-center">
          Powered by <a href="#">
            Xu Qiushi
          </a>. Copyright &copy; 2019 Xu
          Qiushi.
        </p>
        <p class="text-center">
          <a
            href="#"
            target="_blank"
          ></a> All rights reserved.
        </p>
        <p class="text-center">
          <a
            target="_blank"
            href="http://www.w3.org/TR/html5/"
          >
            <font-awesome-icon
              :icon="['fab', 'html5']"
              class="w3"
            >
            </font-awesome-icon>
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";

@Component
export default class Footer extends Vue {}
</script>

<style scoped>
.footer {
  background-color: #eee;
  border-top: 1px solid #ccc;
}
.w3 {
  font-size: 64px;
  color: #444;
}
</style>

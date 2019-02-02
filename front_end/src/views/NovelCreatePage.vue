<template>
  <div>
    <MainNavBar></MainNavBar>
    <div class="container-fluid">
      <div class="row">
        <div class="col-12 col-sm-12  col-md-12 col-lg-3">
          <CommonTreeSideNav></CommonTreeSideNav>
        </div>
        <div class="col-12  col-sm-12 col-md-12 col-lg-9">
          <NovelCodeMirror class="mr-5 pr-5"></NovelCodeMirror>
        </div>
      </div>
    </div>
    <footer></footer>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import MainNavBar from "@/components/MainNavBar.vue";
import Footer from "@/components/Footer.vue";
import CommonTreeSideNav from "@/components/CommonTreeSideNav.vue";
import NovelCodeMirror from "@/components/NovelCodeMirror.vue";

@Component({
  components: {
    MainNavBar,
    Footer,
    CommonTreeSideNav,
    NovelCodeMirror
  }
})
export default class NovelCreatePage extends Vue {}
</script>

<style scoped></style>

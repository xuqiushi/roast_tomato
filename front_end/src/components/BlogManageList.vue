<template>
  <div class="card">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">
            标题
          </th>
          <th>作者</th>
          <th>创建时间</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(blogRecord, index) in blogManageRecords"
          :key="blogRecord + index"
        >
          <th v-text="blogRecord.name"></th>
          <td v-text="blogRecord.userName"></td>
          <td v-text="blogRecord.createAt"></td>
          <td>操作</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import { BlogManageRecord } from "../../typings/blogInterfaces";

@Component
export default class BlogManageList extends Vue {
  @Prop({
    required: true,
    type: Array,
    default: () => {
      return [];
    }
  })
  blogManageRecords!: BlogManageRecord[];
}
</script>

<style scoped></style>

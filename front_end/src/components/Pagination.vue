<template>
  <nav aria-label="blog-pagination">
    <ul class="pagination justify-content-center">
      <li
        :class="
          'page-item ' + [PaginationStructure.selectNow === 1 ? 'disabled' : '']
        "
      >
        <a
          class="page-link"
          href="#"
          tabindex="-1"
        >
          Previous
        </a>
      </li>
      <li class="page-item">
        <a
          class="page-link"
          href="#"
        >
          1
        </a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 2 > 1"
        class="page-item disabled"
      >
        <a
          class="page-link disabled"
          href="#"
        >
          ...
        </a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 2 > 0"
        class="page-item"
      >
        <a
          class="page-link"
          href="#"
          v-text="PaginationStructure.selectNow - 2"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 1 > 0"
        class="page-item"
      >
        <a
          class="page-link"
          href="#"
          v-text="PaginationStructure.selectNow - 1"
        ></a>
      </li>
      <li class="page-item active">
        <a
          class="page-link"
          href="#"
          v-text="PaginationStructure.selectNow"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 1"
        class="page-item"
      >
        <a
          class="page-link"
          href="#"
          v-text="PaginationStructure.selectNow + 1"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 2"
        class="page-item"
      >
        <a
          class="page-link"
          href="#"
          v-text="PaginationStructure.selectNow + 2"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 3"
        class="page-item disabled"
      >
        <a
          class="page-link disabled"
          href="#"
        >
          ...
        </a>
      </li>
      <li
        :class="
          'page-item ' +
            [
              PaginationStructure.countAll === PaginationStructure.selectNow
                ? 'disabled'
                : ''
            ]
        "
      >
        <a
          class="page-link"
          href="#"
        >
          Next
        </a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import { PaginationPara } from "../../typings/blogInterfaces";
@Component
export default class Pagination extends Vue {
  @Prop({
    type: Object,
    required: true,
    default: {}
  })
  PaginationStructure!: PaginationPara;
}
</script>

<style scoped></style>

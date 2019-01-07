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
          tabindex="-1"
          @click="sendSelectBlogPagination(PaginationStructure.selectNow - 1)"
        >
          Previous
        </a>
      </li>
      <li
        v-if="PaginationStructure.selectNow > 1"
        class="page-item"
      >
        <a
          class="page-link"
          @click="sendSelectBlogPagination(1)"
        >
          1
        </a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 2 > 1"
        class="page-item disabled"
      >
        <a class="page-link disabled">
          ...
        </a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 2 > 1"
        class="page-item"
      >
        <a
          class="page-link"
          @click="sendSelectBlogPagination(PaginationStructure.selectNow - 2)"
          v-text="PaginationStructure.selectNow - 2"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.selectNow - 1 > 1"
        class="page-item"
      >
        <a
          class="page-link"
          @click="sendSelectBlogPagination(PaginationStructure.selectNow - 1)"
          v-text="PaginationStructure.selectNow - 1"
        ></a>
      </li>
      <li class="page-item active">
        <a
          class="page-link"
          v-text="PaginationStructure.selectNow"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 1"
        class="page-item"
        @click="sendSelectBlogPagination(PaginationStructure.selectNow + 1)"
      >
        <a
          class="page-link"
          v-text="PaginationStructure.selectNow + 1"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 2"
        class="page-item"
      >
        <a
          class="page-link"
          @click="sendSelectBlogPagination(PaginationStructure.selectNow + 2)"
          v-text="PaginationStructure.selectNow + 2"
        ></a>
      </li>
      <li
        v-if="PaginationStructure.countAll - PaginationStructure.selectNow > 3"
        class="page-item disabled"
      >
        <a class="page-link disabled">
          ...
        </a>
      </li>
      <li
        v-if="PaginationStructure.countAll > PaginationStructure.selectNow"
        class="page-item"
      >
        <a
          class="page-link"
          @click="sendSelectBlogPagination(PaginationStructure.countAll)"
          v-text="PaginationStructure.countAll"
        ></a>
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
import { Component, Prop, Emit } from "vue-property-decorator";
import { PaginationPara } from "../../typings/blogInterfaces";
@Component
export default class Pagination extends Vue {
  @Prop({
    type: Object,
    required: true,
    default: {}
  })
  PaginationStructure!: PaginationPara;
  @Emit()
  emitBlogPagination(pageNumber: number): number {
    return pageNumber;
  }
  sendSelectBlogPagination(pageNumber: number) {
    this.emitBlogPagination(pageNumber);
  }
}
</script>

<style scoped></style>

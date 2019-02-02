<!-- @format -->
<template>
  <nav class="navbar navbar-expand-md navbar-dark">
    <a
      class="navbar-brand"
      href="#"
    ></a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#tomato-nav-bar"
      aria-controls="tomato-nav-bar"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div
      id="tomato-nav-bar"
      class="collapse navbar-collapse"
    >
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a
            class="nav-link"
            href="#"
          >
            吐槽的番茄 <span class="sr-only">
              (current)
            </span>
          </a>
        </li>
        <li class="nav-item dropdown">
          <a
            id="blog-dropdown"
            class="nav-link dropdown-toggle"
            href="#"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            Blog
          </a>
          <div
            class="dropdown-menu"
            aria-labelledby="blog-dropdown"
          >
            <RouterLink
              class="dropdown-item"
              :to="{
                name: 'BlogCreatePage'
              }"
            >
              创建
            </RouterLink>
            <a
              class="dropdown-item"
              href="#"
            >
              管理
            </a>
          </div>
        </li>
        <li class="nav-item dropdown">
          <a
            id="novel-dropdown"
            class="nav-link dropdown-toggle"
            href="#"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            Novel
          </a>
          <div
            class="dropdown-menu"
            aria-labelledby="novel-dropdown"
          >
            <RouterLink
              class="dropdown-item"
              :to="{
                name: 'NovelCreatePage'
              }"
            >
              创建
            </RouterLink>
            <a
              class="dropdown-item"
              href="#"
            >
              管理
            </a>
          </div>
        </li>
      </ul>
      <ul class="navbar-nav mr-3">
        <li class="nav-item dropdown">
          <a
            id="user-dropdown"
            class="nav-link dropdown-toggle"
            href="#"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
            v-text="userName"
          ></a>
          <div
            id="user-drop-down-li"
            class="dropdown-menu"
            aria-labelledby="user-dropdown"
          >
            <a
              class="dropdown-item"
              href="#"
            >
              登出
            </a>
            <a
              class="dropdown-item"
              href="#"
            >
              修改
            </a>
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
export default {
  name: "MainNavBar",
  data() {
    return {
      userName: "有缘者"
    };
  }
};
</script>

<style scoped>
#user-drop-down-li {
  min-width: 5em;
}
nav {
  background-color: rgba(6, 1, 5, 0.86);
}
</style>

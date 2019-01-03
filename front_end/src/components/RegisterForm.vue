<template>
  <form
    class="form-register"
    @submit.prevent="register()"
  >
    <WarningBar class="sticky-top" />
    <div class="text-center mb-4">
      <img
        class="mb-4"
        src="../assets/tomato.svg"
        alt=""
        width="72"
        height="72"
      >
    </div>

    <div class="form-label-group">
      <input
        id="inputUserName"
        v-model="userName"
        type="text"
        class="form-control"
        placeholder="Name"
        required
        autofocus
      >
      <label for="inputUserName">
        Name
      </label>
    </div>

    <div class="form-label-group">
      <input
        id="inputEmail"
        v-model="email"
        type="email"
        class="form-control"
        placeholder="Email address"
        required
        autofocus
      >
      <label for="inputEmail">
        Email address
      </label>
    </div>

    <div class="form-label-group">
      <input
        id="inputPassword"
        v-model="password"
        type="password"
        class="form-control"
        placeholder="Password"
        required
      >
      <label for="inputPassword">
        Password
      </label>
    </div>

    <div class="form-label-group">
      <input
        id="repeatPassword"
        v-model="repeatPassword"
        type="password"
        class="form-control"
        placeholder="RepeatPassword"
        required
      >
      <label for="repeatPassword">
        RepeatPassword
      </label>
    </div>
    <button
      class="btn btn-lg btn-primary btn-block"
      type="submit"
    >
      Sign in
    </button>
  </form>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import crypto from "crypto";
import WarningBar from "@/components/WarningBar.vue";
@Component({
  components: { WarningBar }
})
export default class RegisterForm extends Vue {
  userName = "";
  email = "";
  password = "";
  repeatPassword = "";
  register() {
    if (this.password !== this.repeatPassword) {
      this.$store.commit("common/addWarningMessage", "两次密码不一致");
    } else {
      let lowCaseEmail = this.email.trim().toLowerCase();
      let user_info = {
        name: this.userName,
        email: lowCaseEmail,
        password:
          this.password === ""
            ? ""
            : (input => {
                return crypto
                  .createHash("sha1")
                  .update(JSON.stringify(input))
                  .digest("hex");
              })(lowCaseEmail + ":" + this.password).toString()
      };
      this.$http({
        method: "post",
        data: user_info,
        url: "/api/users"
      })
        .then(response => {
          if (response.data.error) {
            this.$store.commit("common/addWarningMessage", response.data.error);
          } else {
            this.$store.commit("common/deleteAllWarningMessages");
            location.assign("/");
          }
        })
        .catch(error => {
          this.$store.commit("common/addWarningMessage", error.response.data);
        });
    }
  }
}
</script>

<style scoped>
.form-register {
  width: 100%;
  max-width: 420px;
  padding: 15px;
  margin: auto;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group > input,
.form-label-group > label {
  height: 3.125rem;
  padding: 0.75rem;
}

.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0; /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  pointer-events: none;
  cursor: text; /* Match the input under the label */
  border: 1px solid transparent;
  border-radius: 0.25rem;
  transition: all 0.1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: 1.25rem;
  padding-bottom: 0.25rem;
}

.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  font-size: 12px;
  color: #777;
}

/* Fallback for Edge
    -------------------------------------------------- */
@supports (-ms-ime-align: auto) {
  .form-label-group > label {
    display: none;
  }
  .form-label-group input::-ms-input-placeholder {
    color: #777;
  }
}

/* Fallback for IE
    -------------------------------------------------- */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .form-label-group > label {
    display: none;
  }
  .form-label-group input:-ms-input-placeholder {
    color: #777;
  }
}
</style>

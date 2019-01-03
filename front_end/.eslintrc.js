module.exports = {
  "root": true,
  "parser": "vue-eslint-parser",
  "parserOptions": {
    "parser": "typescript-eslint-parser",
    "sourceType": "module",
    "allowImportExportEverywhere": false,
    "ecmaFeatures": {
      "legacyDecorators": true
    }
  },
  "extends": [
    "eslint:recommended",
    "plugin:vue/recommended",
    "plugin:prettier/recommended",
  ],
  "plugins": [
    'vue',
    "typescript",
    // 此插件用来识别.html 和 .vue文件中的js代码，但是与原生的插件冲突了好像
    // 'html',
    // standard风格的依赖包
    "standard",
    // standard风格的依赖包
    "promise",
  ],
  "env": {
    "browser": true,
    "node": true,
    "es6":true,
    "jquery":true
  },
  "globals": {
    "Vue": true,
    "AMap": true,
    "EXIF": true,
    "j_body": true,
    "native": true,
    "VueRouter": true,
    "pocketPost": true,
    "aliCnCityList": true,
  },
  "rules": {
    // "no-unused-vars": 0,
    "typescript/no-unused-vars": [2],
    // prettier规则
    "no-useless-escape": 0,
    "no-multiple-empty-lines": [
      2,
      {
        "max": 3
      }
    ],
    "prettier/prettier": [
      {"parser": "vue"},
      "error",
      {
        "singleQuote": true,
        "semi": false,
        "trailingComma": "none",
        "bracketSpacing": true,
        "jsxBracketSameLine": true,
        "insertPragma": true,
        "requirePragma": false
      }
    ],
    // eslint规则
    "no-debugger": [1],
    "no-unreachable": [1],
    "no-console": [1],
    "no-extra-semi": [1],
  }
};
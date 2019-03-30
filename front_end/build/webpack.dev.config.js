/** @format */

const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const VueLoaderPlugin = require("vue-loader/lib/plugin");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const HtmlWebpackHardDiskPlugin = require("html-webpack-harddisk-plugin");

let pathsToClean = [
  "favicon.ico",
  "main.*.js",
  "register*.js",
  "signin.*.js",
  "vendor.*.js",
  "common.*.js",
  "main.*.gz",
  "register*.gz",
  "signin.*.gz",
  "vendor.*.gz",
  "common.*.gz"
];

// the clean options to use
let cleanOptions = {
  root: path.resolve(__dirname, "../dist"),
  // exclude: [''],
  verbose: true,
  dry: false
};

module.exports = {
  entry: {
    main: path.resolve(__dirname, "../src/entries/main.ts")
  },
  output: {
    path: path.resolve(__dirname, "../dist"),
    publicPath: "/", // 通过devServer访问路径
    filename: "[name].[hash].js",
    chunkFilename: "[name].[hash].js"
  },
  mode: "development",
  resolve: {
    extensions: ["*", ".js", ".vue", ".ts", ".tsx"],
    alias: {
      "@": path.resolve(__dirname, "../src")
    }
  },
  devtool: "eval-source-map",
  optimization: {
    runtimeChunk: {
      name: "common"
    },
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendor",
          chunks: "all"
        }
      }
    }
  },
  plugins: [
    new CleanWebpackPlugin(pathsToClean, cleanOptions),
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      filename: "../dist/templates/index.html",
      template: path.resolve(__dirname, "../src/assets/index.html"),
      favicon: path.resolve(__dirname, "../src/assets/favicon.ico"),
      inject: true
    }),
    new HtmlWebpackHardDiskPlugin(),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      "window.jQuery": "jquery",
      moment: "moment"
    })
  ],
  module: {
    rules: [
      {
        test: /\.(js|vue)$/,
        loader: "eslint-loader",
        enforce: "pre",
        // include: [path.resolve(__dirname, 'src')], // 指定检查的目录
        include: /src/,
        exclude: /node_modules/,
        options: {
          formatter: require("eslint-friendly-formatter") // 指定错误报告的格式规范
        }
      },
      {
        test: /\.vue$/,
        loader: "vue-loader"
      },
      {
        test: /\.tsx?$/,
        loader: "ts-loader",
        exclude: /node_modules/,
        options: {
          appendTsSuffixTo: [/\.vue$/]
        }
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.(scss)$/,
        use: [
          { loader: "vue-style-loader" },
          {
            loader: "style-loader" // inject CSS to page
          },
          {
            loader: "css-loader" // translates CSS into CommonJS modules
          },
          {
            loader: "postcss-loader", // Run post css actions
            options: {
              plugins: function() {
                // post css plugins, can be exported to postcss.config.js
                return [require("precss"), require("autoprefixer")];
              }
            }
          },
          {
            loader: "sass-loader" // compiles Sass to CSS
          }
        ]
      },
      {
        test: /\.css$/,

        loader: "vue-style-loader!css-loader"
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2|png)\w*/,
        use: [
          {
            loader: "url-loader",
            options: {
              name: "./fonts/[name].[ext]"
            }
          }
        ]
      }
    ]
  },
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:8000/",
        pathRewrite: { "/api": "/api" }
      }
    },
    // contentBase: path.resolve(__dirname, '../dist/'),
    index: "../dist/templates/index.html",
    publicPath: "/", // 通过devServer访问路径
    historyApiFallback: {
      verbose: true,
      index: "/templates/index.html"
    }, //不跳转, //不跳转
    inline: true, //实时刷新，
    host: "127.0.0.1",
    port: 5000, //提供访问的端口
    progress: true
    // clientLogLevel: "warning",
  }
};

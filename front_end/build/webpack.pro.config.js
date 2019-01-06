/** @format */

// nodejs 中的path模块
const path = require('path')
const webpack = require('webpack')
const ParallelUglifyPlugin = require('webpack-parallel-uglify-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const HtmlWebpackHardDiskPlugin = require('html-webpack-harddisk-plugin')
const CompressionWebpackPlugin = require('compression-webpack-plugin');

// the path(s)/files that should be cleaned
let pathsToClean = [
  'favicon.ico',
  'main.*.js',
  'register*.js',
  'signin.*.js',
  'vendor.*.js',
  'common.*.js',
  'main.*.gz',
  'register*.gz',
  'signin.*.gz',
  'vendor.*.gz',
  'common.*.gz',
]

// the clean options to use
let cleanOptions = {
  root: path.resolve(__dirname, '../../back_end/static'),
  // 下边可以添加想要排除的文件
  // exclude: [''],
  verbose: true,
  dry: false
}

module.exports = {
  // 入口文件，path.resolve()方法，可以结合我们给定的两个参数最后生成绝对路径，最终指向的就是我们的index.js文件
  entry: {
    main: path.resolve(__dirname, '../src/entries/main.ts')
  },
  // 输出配置
  output: {
    path: path.resolve(__dirname, '../../back_end/static'),
    publicPath: '/static/', // 通过devServer访问路径
    filename: '[name].[hash].js',
    chunkFilename: '[name].[hash].js'
  },
  mode: 'development',
  resolve: {
    extensions: ['*', '.js', '.vue', '.ts', '.tsx'],
    alias: {
      '@': path.resolve(__dirname, '../src')
    }
  },
  optimization: {
    runtimeChunk: {
      name: 'common'
    },
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all'
        }
      }
    }
  },
  plugins: [
    new CleanWebpackPlugin(pathsToClean, cleanOptions),
    new ParallelUglifyPlugin({
      uglifyJS: {
        output: {
          beautify: false,
          comments: false
        },
        compress: {
          warnings: false,
          drop_console: true,
          collapse_vars: true,
          reduce_vars: true
        }
      }
    }),
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      filename: '../templates/index.html',
      template: path.resolve(__dirname, '../src/assets/index.html'), // 模板文件
      collapseWhitespace: true,
      favicon: path.resolve(__dirname, '../src/assets/favicon.ico'),
      inject: true // js的script注入到body底部
    }),
    new HtmlWebpackHardDiskPlugin(),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      moment: 'moment'
    }),
    new CompressionWebpackPlugin({ //gzip 压缩
      filename: '[path].gz[query]',
      algorithm: 'gzip',
      test: /\.js$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ],
  // 特别注意：webpack v1 和webpack v2 的区别
  module: {
    rules: [
      /* 用来解析vue后缀的文件 */
      {
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        enforce: 'pre',
        // include: [path.resolve(__dirname, 'src')], // 指定检查的目录
        include: /src/,
        exclude: /node_modules/,
        options: {
          // 这里的配置项参数将会被传递到 eslint 的 CLIEngine
          formatter: require('eslint-friendly-formatter') // 指定错误报告的格式规范
        }
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules/,
        options: {
          appendTsSuffixTo: [/\.vue$/]
        }
      },
      /* 用babel来解析js文件并把es6的语法转换成浏览器认识的语法 */
      {
        test: /\.js$/,
        loader: 'babel-loader',
        /* 排除模块安装目录的文件 */
        exclude: /node_modules/
      },
      {
        test: /\.(scss)$/,
        use: [{loader: 'vue-style-loader'
        }, {
          loader: 'style-loader', // inject CSS to page
        }, {
          loader: 'css-loader', // translates CSS into CommonJS modules
        }, {
          loader: 'postcss-loader', // Run post css actions
          options: {
            plugins: function () { // post css plugins, can be exported to postcss.config.js
              return [
                require('precss'),
                require('autoprefixer')
              ];
            }
          }
        }, {
          loader: 'sass-loader' // compiles Sass to CSS
        }]
      },
      {
        test: /\.css$/,

        loader: 'vue-style-loader!css-loader'
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2|png)\w*/,
        use: [
          {
            loader: 'url-loader',
            options: {
              name: './fonts/[name].[ext]',
            }
          }
        ]
      }
    ]
  }
}

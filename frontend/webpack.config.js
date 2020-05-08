var path = require('path')
var nodeExternals = require('webpack-node-externals')
const _MiniCssExtractPlugin = require("mini-css-extract-plugin");

const MiniCssExtractPlugin = new _MiniCssExtractPlugin({
  filename: '[name].bundle.css',
  chunkFilename: '[id].css'
});

const CSSLoader = {
  test: /\.css$/,
  exclude: /node_modules/,
  use: [
    {
      loader: _MiniCssExtractPlugin.loader,
      options: {
        publicPath: __dirname + '/public/css/'
      }
    },
    {
      loader: 'css-loader',
      options: {importLoaders: 1},
    },
    {
      loader: 'postcss-loader',
      options: {
        config: {
          path: __dirname + '/postcss.config.js'
        }
      },
    },
  ],
};
build =  {
    entry: './src/main.js',
    mode: 'production',
    output: {
      path: path.resolve(__dirname, './public'),
      filename: 'bundle.js',
      publicPath: '/'
    },
    resolve: {
      extensions: ['.ts', '.js']
    },
    devtool: 'source-map',
    module: {
      rules: [
        {
          test: /\.(ts|tsx|js|jsx)$/,
          use: ['babel-loader']
        },
        CSSLoader
      ]
    },
    plugins: [
      MiniCssExtractPlugin
    ],
  }

  var server = {
    entry: './src/index.js',
    target: 'node',
    mode: 'production',
    externals: [nodeExternals()],
    output: {
      filename: 'index.prod.js',
      publicPath: '/'
    },
    resolve: {
      extensions: ['.ts', '.js']
    },
    devtool: 'source-map',
    module: {
      rules: [
        {
          test: /\.(ts|tsx|js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        CSSLoader
      ]
    },
    plugins: [
      MiniCssExtractPlugin
    ],
  }
module.exports = [build, server] 
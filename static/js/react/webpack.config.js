// webpack config file to builds react components
// run with command 'webpack' from directory

var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, '../simpris');
var APP_DIR = path.resolve(__dirname, 'src/client/app');

var config = {
  entry: {
    dashboard : APP_DIR + '/dashboard.jsx',
    interaction : APP_DIR + '/crm/interaction.jsx',
    lookup : APP_DIR + '/lookup/lookup.jsx'
  },
  output: {
    path: BUILD_DIR,
    filename: '[name]/bundle_[name].js'
  },
  devtool: 'source-map',
  //watch: true,
  module : {
    loaders : [
      {
        test : /\.jsx?/,
        include : APP_DIR,
        loader : 'babel-loader'
      }
    ]
  }
};

module.exports = config;
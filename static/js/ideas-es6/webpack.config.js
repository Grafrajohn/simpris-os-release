var path = require('path');
var webpack = require('webpack');

var BUILD_DIR = path.resolve(__dirname, '../simpris');

module.exports = {
    entry: './src/ideas_es6.js',
    output: {
        path: BUILD_DIR + '/ideas',
        filename: 'ideas_bundle.js'
    },
    module: {
     loaders: [
         {
             test: /\.js$/,
             loader: 'babel-loader',
             query: {
                 presets: ['es2015']
             }
         }
     ]
    },
    stats: {
     colors: true
    },
    devtool: 'source-map'
};
// gulpfile.js
// concatenates css files
var gulp = require('gulp');
var concat = require('gulp-concat');

gulp.task('default', [], function() {
  console.log("Concating and moving all the css files in styles folder");
  gulp.src("Simpris/simpris/static/web/css/**.css")
      .pipe(concat('web_main.css'))
      .pipe(gulp.dest('build/styles'));
});
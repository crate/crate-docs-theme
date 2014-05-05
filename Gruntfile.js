'use strict';

var mountFolder = function (connect, dir) {
  return connect.static(require('path').resolve(dir));
};

module.exports = function (grunt) {
  // load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  grunt.initConfig({
    pkg: require('./package.json'),
    theme_template_path: 'src/crate/rtd_theme/crate',
    theme_static_path: 'src/crate/rtd_theme/crate/static',
    out_static_path: '_out/docs/web/server/_static',
    watch: {
      options: {
      },
      less: {
        files: ['<%= theme_static_path %>/css/*.less'],
        tasks: ['recess']
      },
      sphinx: {
        files: ['<%= theme_template_path %>/*.html'],
        tasks: ['shell']
      }
    },
    shell: {
      sphinx: {
        command: './bin/sphinx'
      }
    },
    recess: {
      dev: {
        options: {
          compile: true
        },
        files: {
          '<%= out_static_path %>/css/main.css': [
            '<%= theme_static_path %>/css/main.less'
          ]
        }
      },
      dist: {
        options: {
          compile: true
        },
        files: {
          '<%= theme_static_path %>/css/main.css': [
            '<%= theme_static_path %>/css/main.less'
          ]
        }
      }
    }
  });

  grunt.registerTask('build', [
    'recess:dist',
    'shell:sphinx'
  ]);

};

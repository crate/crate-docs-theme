/*!
 * Licensed to Crate (https://crate.io) under one or more contributor
 * license agreements.  See the NOTICE file distributed with this work for
 * additional information regarding copyright ownership.  Crate licenses
 * this file to you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.  You may
 * obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 * However, if you have executed another commercial license agreement
 * with Crate these terms will supersede the license and you may use the
 * software solely pursuant to the terms of the relevant commercial agreement.
 */
'use strict';

var mountFolder = function (connect, dir) {
  return connect.static(require('path').resolve(dir));
};

module.exports = function (grunt) {
  // load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  grunt.initConfig({
    pkg: require('./package.json'),
    theme_template_path: 'src/crate/theme/rtd/crate',
    theme_static_path: 'src/crate/theme/rtd/crate/static',
    out_static_path: 'out/docs/_static',
    watch: {
      options: {
      },
      less: {
        files: ['<%= theme_static_path %>/css/*.less'],
        tasks: ['recess']
      },
      sphinx: {
        files: [
          '<%= theme_template_path %>/*.html',
          '<%= theme_template_path %>/*.conf'
        ],
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

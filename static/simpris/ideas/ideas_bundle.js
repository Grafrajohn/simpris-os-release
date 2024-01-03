/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


// Vue.component('node-idea', {
//     template:
//         '<svg width="50" height="50">\
//             <circle cx="25" cy="25" r="25" fill="purple" />\
//         </svg>'
// });
//
// Vue.component('node-concept', {
//     template:
//         '<svg width="50" height="50">\
//             <rect cx="25" cy="25" r="25" fill="purple" />\
//         </svg>'
// });

// Vue.component('node-link', {
//   // options
// });

// create idea prototype
// var Idea = function() {
//     this.name = "class A";
// }
//
// Idea.prototype.print = function() {
//     console.log(this.name);
// }

new Vue({
    el: '#ideas-root',
    delimiters: ['<%', '%>'],
    components: {},
    data: {
        // linkData: [],
        // projectData: [],
        // noLinkPanelVisible: true,
        // linkPanelVisible: false,
        // lnkURLText: true,
        // lnkURLEdit: true,
        // lnkURLEditText: false,
        ideasMap: [],
        svgContainer: {},
        objCollection: {
            ideas: [],
            concepts: []
        }
    },
    ready: function ready() {},
    mounted: function mounted() {},
    created: function created() {
        var self = this;
        //this.getLinks(simpris.project.project_id_stored, 2);
        this.makeCanvas();
    },
    methods: {
        // create canvas
        makeCanvas: function makeCanvas() {
            var self = this;
            // self.svgContainer = d3.select("#ideas-pane").append("svg")
            //     .id("svgPane")
            //     .attr("width", 600)
            //     .attr("height", 600);
            // d3.select("#ideas-pane").style("background-color", "lightgray");
        },
        // create new idea
        newIdea: function newIdea() {
            var self = this;
            var idea = d3.select("#svgPane").append("circle").attr("cx", 30).attr("cy", 30).attr("r", 20).style("fill", "green");
            //d3.select(idea).style("background-color", "green");
            self.objCollection.ideas.push(idea);
        },
        // create new conecpt
        newConcept: function newConcept() {
            var self = this;
            var concept = d3.select("#svgPane").append("rect").attr("x", 10).attr("y", 10).attr("width", 50).attr("height", 100).style("fill", "blue");
            self.objCollection.concepts.push(concept);
        },
        // add new objects to the ideas map
        mapAddItem: function mapAddItem(obj) {}
        // confirmDeleteLink: function (link_id) {
        //     event.preventDefault();
        //     var result = confirm("Are you sure you want to delete the link?");
        //     if (result == true)
        //         this.deleteLink(link_id);
        //     else
        //         return false;
        // },
        // deleteLink: function (link_id) {
        //     var self = this;
        //     var post_data = {
        //         link_id: link_id,
        //         csrfmiddlewaretoken: simpris.csrf_token
        //     };
        //     $.ajax({
        //         url: '/api/link/delete/' + link_id + '/',
        //         type: 'DELETE',
        //         beforeSend: function(xhr) {
        //             xhr.setRequestHeader("X-CSRFToken", simpris.csrf_token);
        //         }
        //     }).done(function (data) {
        //         window.location.replace("/project/edit/" + simpris.project.project_id_stored + "/");
        //     }).fail(function (response) {
        //         simpris.common.errorNotify(response.statusText);
        //     });
        // },
        // editLink: function (link_id) {
        //     event.preventDefault();
        //     var self = this;
        //     self.lnkURLText = false;
        //     self.lnkURLEdit = true;
        //     self.lnkURLEditText = true;
        //     return false;
        // },
        // // list project links
        // getLinks: function (entity_id, entity_type) {
        //     var self = this;
        //     self.lnkURLText = true;
        //     $.ajax({
        //         url: '/api/link/list/' + entity_id + '/' + entity_type + '/',
        //         type: 'GET'
        //     }).done(function (data) {
        //         self.linkData = data;
        //         if (data.length > 0) {
        //             self.linkPanelVisible = true;
        //             self.noLinkPanelVisible = false;
        //         }
        //         else {
        //             self.linkPanelVisible = false;
        //             self.noLinkPanelVisible = true;
        //         }
        //     }).fail(function (response) {
        //         simpris.common.errorNotify(response.statusText);
        //     });
        // },
        // updateLink: function (link_id) {
        //     var self = this;
        //     var post_data = {
        //         link_id: link_id,
        //         data: $("#frmLinkEdit").serializeArray(),
        //         csrfmiddlewaretoken: simpris.csrf_token
        //     };
        //     $.ajax({
        //         url: '/api/link/update/' + link_id + '/',
        //         type: 'PUT',
        //         data: post_data,
        //         beforeSend: function(xhr) {
        //             xhr.setRequestHeader("X-CSRFToken", simpris.csrf_token);
        //         }
        //     }).done(function (data) {
        //         simpris.common.successNotify("Link has been updated");
        //     }).fail(function (response) {
        //         simpris.common.errorNotify(response.statusText);
        //     });
        // }
    },
    events: {}
});

/***/ })
/******/ ]);
//# sourceMappingURL=ideas_bundle.js.map
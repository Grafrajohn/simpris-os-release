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


var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Base = function Base(createdBy) {
    _classCallCheck(this, Base);

    this.createdBy = createdBy;
};

var Idea = function (_Base) {
    _inherits(Idea, _Base);

    function Idea() {
        _classCallCheck(this, Idea);

        return _possibleConstructorReturn(this, (Idea.__proto__ || Object.getPrototypeOf(Idea)).apply(this, arguments));
    }

    _createClass(Idea, [{
        key: 'doSomething',
        value: function doSomething() {
            //alert("Idea");
        }
    }]);

    return Idea;
}(Base);

new Vue({
    el: '#ideas-root',
    delimiters: ['<%', '%>'],
    components: {},
    data: {
        ideasMap: [],
        svgContainer: {},
        nodes: {
            ideas: [],
            concepts: []
        },
        links: [],
        positionx: 90,
        positiony: 90,
        posX_index: 0,
        posY_index: 0
    },
    ready: function ready() {},
    mounted: function mounted() {},
    created: function created() {
        var self = this;
        self.makeCanvas();
    },
    methods: {
        // create canvas
        makeCanvas: function makeCanvas() {
            var self = this;
        },
        // create new idea
        newIdea: function newIdea() {
            var self = this;
            var idea = d3.select("#svgPane").append("g");
            idea.append("circle").attr("cx", self.positionx + 60).attr("cy", self.positiony).attr("r", 50).style("fill", "green");
            idea.append('text').attr('x', self.positionx - 20).attr('y', self.positiony + 5).attr('dx', 65).style("fill", "white").text('Idea');
            self.nodes.ideas.push(idea);
            self.nodePosition();
            //self.forceLayout();
            self.createIdeasMap();
        },
        // create new conecpt
        newConcept: function newConcept() {
            var self = this;
            var concept = d3.select("#svgPane").append("g");
            concept.append("rect").attr("width", 100).attr("height", 80).attr("x", self.positionx + 10).attr("y", self.positiony - 30).style("fill", "blue");
            concept.append('text').attr('x', self.positionx - 35).attr('y', self.positiony + 15).attr('dx', 65).style("fill", "white").text('Concept');
            self.nodes.concepts.push(concept);
            self.nodePosition();
            //self.forceLayout();
            self.createIdeasMap();
        },
        // add new objects to the ideas map
        mapAddItem: function mapAddItem(obj) {},
        // d3 force layout
        forceLayout: function forceLayout() {
            var self = this;
            var force = d3.layout.force().size([width, height]).nodes(nodes).links(links);
        },
        // set position of node
        nodePosition: function nodePosition() {
            var self = this;
            if (self.positionx > 900) {
                self.positionx = 60;
                self.positiony = self.positiony + 110;
            } else {
                self.positionx = self.positionx + 105;
            }
        },
        // get ideas map
        getIdeasMap: function getIdeasMap() {
            $.ajax({
                method: "GET",
                url: "/api/ideamap/list/",
                data: { proj_id: id }
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function (items) {
                $(items).each(function (index) {
                    var note_content = items[index].description;
                    var note_db_id = items[index].name;
                    $.PostItAll.new({
                        dB_id: note_db_id,
                        content: note_content,
                        position: 'relative',
                        posX: posX_index,
                        posY: posY_index,
                        onChange: function onChange(id) {
                            if (this.content != note_content) {
                                simpris.project.check_typing(id, this);
                            }
                        },
                        onCreated: function onCreated(id, content, obj) {
                            //simpris.project.ideas.notes.push(obj);
                        },
                        onDelete: function onDelete(id) {
                            simpris.project.postit_delete(this.dB_id);
                        }
                    });
                    posX_index += 190;
                    if (posX_index > safe_margin) {
                        posX_index = position.left;
                        posY_index += 230;
                    }
                });
            });
        },
        // create ideas map
        createIdeasMap: function createIdeasMap() {
            var self = this;
            var post_data = {
                id: id,
                content: note.content,
                csrfmiddlewaretoken: simpris.csrf_token,
                parent_id: simpris.project.ideas.project_id
            };
            $.ajax({
                method: "POST",
                url: "/api/ideamap/insert/",
                data: post_data
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function (r) {});
        },
        // update ideas map
        updateIdeasMap: function updateIdeasMap() {
            var self = this;
            var post_data = {
                name: note.dB_id,
                content: note.content,
                csrfmiddlewaretoken: simpris.csrf_token
            };
            $.ajax({
                method: "POST",
                url: "/api/ideamap/update/",
                data: post_data
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function (items) {});
        },
        //delete ideas map
        deleteIdeasMap: function deleteIdeasMap(id) {
            var post_data = {
                id: id,
                csrfmiddlewaretoken: simpris.csrf_token
            };
            var url = "/api/ideamap/delete/";
            $.ajax({
                method: "POST",
                url: url,
                data: post_data
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function (r) {
                id = null;
            });
        }
    },
    events: {}
});

/***/ })
/******/ ]);
//# sourceMappingURL=ideas_bundle.js.map
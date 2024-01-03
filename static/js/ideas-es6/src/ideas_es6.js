'use strict';

class Base {
   constructor(createdBy) {
      this.createdBy = createdBy;
   }
}

class Idea extends Base {
    doSomething() {
        //alert("Idea");
    }
}

new Vue({
  el: '#ideas-root',
    delimiters: ['<%', '%>'],
    components: {
    },
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
    ready: function () {
    },
    mounted: function () {

    },
    created: function () {
        var self = this;
        self.makeCanvas();
    },
    methods: {
        // create canvas
        makeCanvas: function () {
            var self = this;
        },
        // create new idea
        newIdea: function () {
            var self = this;
            var idea = d3.select("#svgPane")
                .append("g");
            idea.append("circle")
                .attr("cx", self.positionx + 60)
                .attr("cy", self.positiony)
                .attr("r", 50)
                .style("fill", "green");
            idea.append('text')
                .attr('x', self.positionx - 20)
                .attr('y', self.positiony + 5)
                .attr('dx', 65)
                .style("fill", "white")
                .text('Idea');
            self.nodes.ideas.push(idea);
            self.nodePosition();
            //self.forceLayout();
            self.createIdeasMap();
        },
        // create new conecpt
        newConcept: function () {
            var self = this;
            var concept = d3.select("#svgPane")
                .append("g");
            concept.append("rect")
                .attr("width", 100)
                .attr("height", 80)
                .attr("x", self.positionx + 10)
                .attr("y", self.positiony - 30)
                .style("fill", "blue");
            concept.append('text')
                .attr('x', self.positionx - 35)
                .attr('y', self.positiony + 15)
                .attr('dx', 65)
                .style("fill", "white")
                .text('Concept');
            self.nodes.concepts.push(concept);
            self.nodePosition();
            //self.forceLayout();
            self.createIdeasMap();
        },
        // add new objects to the ideas map
        mapAddItem: function (obj) {

        },
        // d3 force layout
        forceLayout: function () {
            var self = this;
            var force = d3.layout.force()
                .size([width, height])
                .nodes(nodes)
                .links(links);
        },
        // set position of node
        nodePosition: function () {
            var self = this;
            if (self.positionx > 900) {
                self.positionx = 60;
                self.positiony = self.positiony + 110;
            }
            else {
                self.positionx = self.positionx + 105;
            }
        },
        // get ideas map
        getIdeasMap: function () {
            $.ajax({
                method: "GET",
                url: "/api/ideamap/list/",
                data: {proj_id: id}
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
                        onChange: function (id) {
                            if (this.content != note_content) {
                                simpris.project.check_typing(id, this);
                            }
                        },
                        onCreated: function (id, content, obj) {
                            //simpris.project.ideas.notes.push(obj);
                        },
                        onDelete: function (id) {
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
        createIdeasMap: function () {
            var self = this;
            var post_data = {
                id: id,
                content: note.content,
                csrfmiddlewaretoken: simpris.csrf_token,
                parent_id: simpris.project.ideas.project_id
            }
            $.ajax({
                method: "POST",
                url: "/api/ideamap/insert/",
                data: post_data
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function (r) {
            });
        },
        // update ideas map
        updateIdeasMap: function () {
            var self = this;
            var post_data = {
                name: note.dB_id,
                content: note.content,
                csrfmiddlewaretoken: simpris.csrf_token,
            }
            $.ajax({
                method: "POST",
                url: "/api/ideamap/update/",
                data: post_data
            }).error(function (r) {
                $('#spnError').text("There has been an error: " + r.statusText);
            }).done(function(items) {
            });
        },
        //delete ideas map
        deleteIdeasMap: function (id) {
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
"use strict";

$(function() {

    //Global vars : enable and disable features and change the notes behaviour
    $.fn.postitall.globals = {
        prefix          : '#PIApostit_',//Id note prefixe
        filter          : 'domain',     //Options: domain, page, all
        savable         : false,        //Save postit in storage
        randomColor     : false,        //Random color in new postits
        toolbar         : true,         //Show or hide toolbar
        autoHideToolBar : true,         //Animation efect on hover over postit shoing/hiding toolbar options
        removable       : true,         //Set removable feature on or off
        askOnDelete     : true,         //Confirmation before note remove
        draggable       : true,         //Set draggable feature on or off
        resizable       : true,         //Set resizable feature on or off
        editable        : true,         //Set contenteditable and enable changing note content
        changeoptions   : true,         //Set options feature on or off
        blocked         : true,         //Postit can not be modified
        minimized       : true,         //true = minimized, false = maximixed
        expand          : true,         //Expand note
        fixed           : true,         //Allow to fix the note in page
        addNew          : true,         //Create a new postit
        showInfo        : true,         //Show info icon
        pasteHtml       : true,         //Allow paste html in contenteditor
        htmlEditor      : false,         //Html editor (trumbowyg)
        autoPosition    : true,         //Automatic reposition of the notes when user resize screen
        addArrow        : 'back'        //Add arrow to notes : none, front, back, all
    };

    //Note global vars : Properties, style, features and events of the note
    $.fn.postitall.defaults = {
        //Note properties
        id              : "",                       //Note id
        dB_id           : "",
        created         : Date.now(),               //Creation date
        domain          : window.location.origin,   //Domain in the url
        page            : window.location.pathname, //Page in the url
        osname          : navigator.appVersion,     //Browser informtion & OS name,
        content         : '',                       //Content of the note (text or html)
        position        : 'absolute',               //Position absolute or fixed
        posX            : '100px',                   //x coordinate (from left)
        posY            : '100px',                   //y coordinate (from top)
        right           : '',                       //x coordinate (from right). This property invalidate posX
        height          : 200,                      //Note total height
        width           : 160,                      //Note total width
        minHeight       : 210,                      //Note resizable min-width
        minWidth        : 170,                      //Note resizable min-height
        oldPosition     : {},                       //Position when minimized/collapsed (internal use)
        //Config note style
        style : {
            tresd           : true,                 //General style in 3d format
            backgroundcolor : '#FFFA3C',            //Background color in new postits when randomColor = false
            textcolor       : '#333333',            //Text color
            textshadow      : true,                 //Shadow in the text
            fontfamily      : 'verdana',            //Default font
            fontsize        : 'small',              //Default font size
            arrow           : 'none',               //Default arrow : none, top, right, bottom, left
        },
        //Enable / Disable features
        features : $.fn.postitall.globals,          //By default, copy of global defaults
        //Note flags
        flags : {
            blocked         : false,                //If true, the note cannot be edited
            minimized       : false,                //true = Collapsed note / false = maximixed
            expand          : false,                //true = Expanded note / false = normal
            fixed           : false,                //Set position fixed
            highlight       : false,                //Higlight note
        },
        //Attach the note to al html element
        attachedTo : {
            element         : '',                   //Where to attach
            position        : 'left',              //Position relative to elemente : top, right, bottom or left
            fixed           : true,                 //Fix note to element when resize screen
            arrow           : false,                 //Show an arrow in the inverse position
        },
        // Callbacks / Event Handlers
        onCreated: function(id, options, obj) { return undefined; },    //Triggered after note creation
        onChange: function (id) { return undefined; },                  //Triggered on each change
        onSelect: function (id) { return undefined; },                  //Triggered when note is clicked, dragged or resized
        onDblClick: function (id) { return undefined; },                //Triggered on double click
        onRelease: function (id) { return undefined; },                 //Triggered on the end of dragging and resizing of a note
        onDelete: function (id) { return undefined; }                   //Triggered when a note is deleted
    };

    // set effect from select menu value
    $(".postit_create").click(function () {
       simpris.project.postit_create();
       return false;
    });

    //create postit
    simpris.project.postit_create = function () {
        $.PostItAll.new({
            content: "",
            dB_id: "",
            onChange: function (id) {
                if(this.content != "") {
                    simpris.project.check_typing(id, this);
                }
                 // the this object is available with change post-it name
            },
            onCreated: function (id, note, obj) {
                //simpris.project.ideas.notes.push(obj);
                note.dB_id = id;
                var post_data = {
                    id: id,
                    content: note.content,
                    csrfmiddlewaretoken: simpris.csrf_token,
                    parent_id: simpris.project.ideas.project_id
                }
                $.ajax({
                    method: "POST",
                    url: "/api/idea/insert/",
                    data: post_data
                }).error(function (r) {
                    $('#spnError').text("There has been an error: " + r.statusText);
                }).done(function (r) {
                });
            },
            onDelete: function (id) {
                simpris.project.postit_delete(this.dB_id);
            }
        });
    };

    // load postits
    simpris.project.postit_load = function (id) {
        var p = $("#div_notes");
        var position = p.offset();
        var posX_index = position.left;
        var posY_index = position.top + 30;
        var doc_width = $( document ).width();
        var safe_margin = doc_width - 190;
        $.ajax({
            method: "GET",
            url: "/api/idea/list/",
            data: {proj_id: id}
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
        .done(function(items) {
            $(items).each(function(index) {
                var note_content = items[index].description;
                var note_db_id = items[index].name;
                $.PostItAll.new({
                    dB_id: note_db_id,
                    content : note_content,
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
    };

    //update postit
    simpris.project.postit_update = function (id, note) {
        var post_data = {
            name: note.dB_id,
            content: note.content,
            csrfmiddlewaretoken: simpris.csrf_token,
        }
        $.ajax({
            method: "POST",
            url: "/api/idea/update/",
            data: post_data
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
        .done(function(items) {
        });
    };

    //delete postit
    simpris.project.postit_delete = function (id) {
        var post_data = {
            id: id,
            csrfmiddlewaretoken: simpris.csrf_token
        };
        var url = "/api/idea/delete/";
        $.ajax({
            method: "POST",
            url: url,
            data: post_data
        }).error(function (r) {
            $('#spnError').text("There has been an error: " + r.statusText);
        }).done(function (r) {
            id = null;
        });
    };

    //check for typing
    simpris.project.check_typing = function (id, note) {
        //setup before functions
        var typingTimer;                //timer identifier
        var doneTypingInterval = 3000;  //time in ms, 5 second for example
        var $input = $(id);

        //on keyup, start the countdown
        $input.on('keyup', function () {
            clearTimeout(typingTimer);
            typingTimer = setTimeout(doneTyping, doneTypingInterval);
        });

        //on keydown, clear the countdown
        $input.on('keydown', function () {
            clearTimeout(typingTimer);
        });

        //user is "finished typing," do something
        function doneTyping() {
            simpris.project.postit_update(id, note);
        }
    }
});
'use strict';
    $(function() {

        simpris.project.kanban = {};
        simpris.project.task_find="kan";

        $("ul.kanban-list").sortable({
            connectWith: "ul",
            cursor: "move",
            out: function(event, ui) {
                simpris.project.kanban.item_id = ui.item[0].id.replace("kanban-item-","");
                simpris.project.kanban.ui_item = ui.item[0];
                simpris.project.kanban.item_type = ui.item.find('#item_type').text();
                simpris.project.kanban.source_column = ui.item.attr('data-source-column');
            },
            receive: function(event, ui) {
                simpris.project.kanban.target = $(this).attr('id');
                simpris.project.kanban.target_id = simpris.project.kanban.target.replace("kanban-list-", "");
                simpris.project.kanban.data = {csrfmiddlewaretoken: simpris.csrf_token,
                    item_id: simpris.project.kanban.item_id,
                    item_type: simpris.project.kanban.item_type,
                    column_id: simpris.project.kanban.target_id,
                    source_column: simpris.project.kanban.source_column
                    };
                    if (simpris.project.kanban.source_column === "0") {
                        $.ajax({
                            method: "POST",
                            url: "/api/kanban/insert/",
                            data: simpris.project.kanban.data
                        })
                        .done(function(data) {
                            //alert("moved the bleeder: " + simpris.project.kanban.target_id);
                        });
                    }
                    else {
                        $.ajax({
                            method: "POST",
                            url: "/api/kanban/move/",
                            data: simpris.project.kanban.data
                        })
                        .done(function(data) {
                            //alert("moved the bleeder: " + simpris.project.kanban.target_id);
                        });
                    }
            }
        });
    });
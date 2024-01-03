    $(function() {
        simpris.project.schedule = {};
        simpris.project.task_find="sch";

        $("ul.schedule-list").sortable({
            connectWith: "ul",
            cursor: "move",
            out: function(event, ui) {
                // if move from tasks
                if (ui.item[0].id.substring(0,6) == 'phase-') {
                    simpris.project.schedule.task_id = ui.item[0].id.replace("phase-item-", "");
                }
                // if move from another phase
                else if (ui.item[0].id.substring(0,9) == 'schedule-') {
                    simpris.project.schedule.task_id = ui.item[0].id.replace("schedule-item-", "");
                }
                simpris.project.schedule.ui_item = ui.item[0];
                simpris.project.schedule.item_type = ui.item.find('#item_type').text();
            },
            receive: function(event, ui) {
                simpris.project.schedule.target = $(this).attr('id');
                simpris.project.schedule.phase_id = simpris.project.schedule.target.replace("schedule-list-", "");
                simpris.project.schedule.data = {
                    csrfmiddlewaretoken: simpris.csrf_token,
                    task_id: simpris.project.schedule.task_id,
                    //item_type: simpris.project.schedule.item_type,
                    phase_id: simpris.project.schedule.phase_id
                    };
                    $.ajax({
                        method: "POST",
                        url:"/api/schedule/move/",
                        data: simpris.project.schedule.data
                    })
                    .done(function(data) {
                        //alert("moved the bleeder: " + simpris.project.schedule.phase_id);
                    });
            }
        });
    });
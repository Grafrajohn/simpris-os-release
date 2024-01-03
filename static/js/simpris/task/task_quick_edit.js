/**
 * Created by Graham on 21/02/2017.
 */
'use strict';

$(function () {

    // class click to quick edit task
    $(document).on("click", "a.lnkQuickEditTask", function () {
    	var task_id = this.getAttribute("data-task-id");
        simpris.project.task_quick_edit(task_id);
        return false;
    });

    // button click to update
	$("#btn-task-update").click(function() {
		simpris.project.task_quick_update();
		return false;
	  });

    // button click to update
	$("#btn-task-cancel").click(function() {
		$('#task-quick-edit').trigger("reset");
		//$("#task-quick-edit").hide();
		$("#task-quick-edit").css("display", "none");
		  //return false;
	});

    // button click to retrieve task data
	simpris.project.task_quick_edit = function (taskID) {
	    var data;
        // ajax get task
		  $.ajax({
			  url: "/api/task/detail/",
			  data: { taskid: taskID },
			  type: "GET"
		  })
		  .error(function(err){
			  $("#spnQuickError").show();
			  $("#spnQuickError").text(err.statusText);
			  //console.log("error",err);
		  })
		  .success(function(r){
			  // get data
              data = r;
              simpris.project.task_quick_edit_show(data, taskID);
		  });

		return false;
    };

	// display task edit box
	simpris.project.task_quick_edit_show = function (data, task_id) {
        // display task edit box
        $("#task-quick-edit").css("display", "block");
        window.location = "#task-quick-edit";
        $("#spnTaskName").html(data.taskName);
		$("#frmPercentComplete").val(data.taskPercentageComplete);
		$("#frmDatePicker").val(data.taskStartDate);
		$("#frmDatePicker2").val(data.completionDate);
        $("#hidTaskStatus").val(data.taskStatus);
        $("#hidTaskAssignee").val(data.taskAssignee);
        $("#hidTaskID").val(task_id);

        $("txt_task_start_date").focus();

		simpris.project.get_lookup(21, data.taskStatus);
		simpris.project.get_assignee(task_id, data.taskAssignee);

		$("#frmTaskStatus[value=" + data.taskStatus + "]").attr("selected", true);
		$("#frmTaskAssignee[value" + data.taskAssignee + "]").attr("selected",true);
		//$("#div.frmTaskStatus select").val(data.taskStatus);
		//$("#div.frmTaskAssignee select").val(data.taskAssignee);
		return false;
    };

	// update task
	simpris.project.task_quick_update = function() {
		var $form = $('#frmTaskQuickEdit');

		$('#spnQuickError').empty();

		var valid = simpris.project.validate_task_form("u");

		if (valid == false) {
			return false;
		}

		var data = $('#frmTaskQuickEdit').serializeArray();
		//var ckedited = CKEDITOR.instances.frmTaskDescription.getData();
		//data.push({name: 'ckedited', value: ckedited});

		$.ajax({
			url: '/api/task/update_quick/',
			data: data,
			type: 'POST',
		})
		.error(function(err){
			  $("#spnQuickError").show();
			  $('#spnQuickError').text(err.statusText);
		})
		.success(function(r){
			//console.log(r.task_id);
			// add to page
			window.location.reload(true);
		});
	};

	// get lookups
	simpris.project.get_lookup = function (lookup_id, task_status) {
        // ajax get lookup
		$.ajax({
		  url: "/api/lookup/lookups/21",
		  type: "GET"
		})
		.error(function(err){
		  $("#spnQuickError").show();
		  $("#spnQuickError").text(err.statusText);
		  //console.log("error",err);
		})
		.success(function(r){
		  	// get data
		  	var lookups = r;
		  	// clear select
			$('#frmTaskStatus').empty();
		  	// loop through lookups adding to task status select
			$(lookups).each(function(){
				$('#frmTaskStatus').append('<option value="' + this.lookupvaluenum + '">' + this.lookupvaluechar + '</option>');
				if (this.lookupvaluenum === task_status) {
					$("#frmTaskStatus option[value=" + this.lookupvaluenum + "]").prop('selected', true);
				}

			});
			// set selected status if there is one
		});
	};

	// get assignee
	simpris.project.get_assignee = function (data, task_assignee) {
        // ajax get lookup
		$.ajax({
		  url: "/api/user/projectusers/" + data,
		  type: "GET"
		})
		.error(function(err){
		  $("#spnQuickError").show();
		  $("#spnQuickError").text(err.statusText);
		  //console.log("error",err);
		})
		.success(function(r){
		  	// get data
		  	var assignees = r;
		  	// clear select
			$('#frmTaskAssignee').empty();
		  	// loop through lookups adding to task status select
			$(assignees).each(function(){
				$('#frmTaskAssignee').append('<option value="' + this.user_id + '">' + this.first_name + ' ' + this.last_name + '</option>');
				if (this.user_id === task_assignee) {
					$("#frmTaskAssignee option[value=" + this.user_id + "]").prop('selected', true);
				}
			});
			// set selected status if there is one
		});
	};

	// update task
	simpris.project.validate_task_form = function(action) {

		// action is i for insert or u for update
		// if insert the form is frmUserAdd else frmUserEdit
		var form = null;
		if (action === "i") {
			form = '#frmTaskAdd';
		}
		else {
			form = '#frmTaskQuickEdit';
		}

		var taskStatus = $("#frmTaskStatus", form).val();

		var valid = true;

		//if (taskDescription == "") {
		//	$('#spnError').text("Task description required. " + "<br>");
		//	valid = false;
		//}
		//if (taskType == "") {
		//	$('#spnError').text("Task type required. " + "<br>");
		//	valid = false;
		//}
		//if (taskPriority == "") {
		//	$('#spnError').text("Task priority required. " + "<br>");
		//	valid = false;
		//}
		if (taskStatus === "") {
			$('#spnQuickError').text("Task status required. " + "<br>");
			valid = false;
		}

		return valid;
    };
});
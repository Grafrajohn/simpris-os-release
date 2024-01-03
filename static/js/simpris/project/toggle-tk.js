"use strict";

$(function() {
	// set effect from select menu value
	$(".task-add").click(function() {
	  simpris.project.showAddTaskDiv(this.id);
	  return false;
	});

	$("#btn-task-add").click(function() {
	  simpris.project.perform_task_create();
	  return false;
	});

	$(".task-edit").click(function() {
	  var tableRow = $(this).closest("tr").index();
	  var table = $(this).closest("table").attr('id');
	  simpris.project.showEditTaskDiv(this.id,table,tableRow);
	  return false;
	});

	// $("#frmTaskDependency").click(function() {
	//   var taskID = $('#hidTaskID').val();
	//   simpris.project.get_task_dependencies(taskID);
	//   return false;
	// });

	// delete task
	$(".task-delete").click(function() {
		var confirm_delete = confirm("Are you sure you want to delete?");
		if (confirm_delete == false) {
			return;
		}
		var task_id = $(this).attr('id').replace('link-task-delete-','');
		var tasklist_id = $(this).attr('data-tasklist-delete');
		//var project_id = $(this).attr('data-project-id');
		simpris.project.post_task_delete(task_id,tasklist_id);
		return false;
	});

	simpris.project.delegateTaskEdit = function() {
	  var tableRow = $(this).closest("tr").index();
	  var table = $(this).closest("table").attr('id');
	  simpris.project.showEditTaskDiv(this.id,table,tableRow);
	  return false;
	};
	  
	$("#btn-task-update").click(function() {
	  simpris.project.perform_task_update();
	  return false;
	});

	$("#btn-task-cancel").click(function() {
	  var id = $("#btn-task-cancel").closest("div").attr("id");
	  $('#' + id).toggle();
	  $('#' + id).remove();
	  $("#table-row-placeholder-" + id).remove();
	  $("#table-row-edit-" + id).remove();
	  return false;
	});
		
	// new task button
	simpris.project.showAddTaskDiv = function(buttonid) {
	  // run the effect
	  if (buttonid != "button-tkl") {
		  var div = "#" + buttonid;
		  var divR = buttonid.replace("button","toggle");
		  // check if div already exists if it does delete it as a toggle
		  if ($('#' + divR).length) {
			  $('#' + divR).toggle();
			  $('#' + divR).remove();
			  return;
		  }
		  var divP = div.replace("button","placeholder");
		  $('#toggle-tk-')
		  .clone(true)
		  .attr('id', divR)
		  .appendTo(divP);
		  var taskListID = buttonid.replace("button-tk-","");
		  $("div#" + divR + " " + "#hidTaskList").attr("value",taskListID);
		  $("div#" + divR + " " + "#frmDatePicker-").attr("id","frmDatePicker-" + taskListID);
		  $("div#" + divR + " " + "#frmDatePicker-" + taskListID).attr("name","frmDatePicker-" + taskListID);
		  //$("div#" + divR + " " + "#frmDatePicker-" + taskListID).datepicker();
		  $("div#" + divR + " " + "#frmDatePicker-" + taskListID).datepicker({inline: true,dateFormat: 'yy-mm-dd'});
		  $("div#" + divR + " " + "#frmDatePicker2-").attr("id","frmDatePicker2-" + taskListID);
		  $("div#" + divR + " " + "#frmDatePicker2-" + taskListID).attr("name","frmDatePicker2-" + taskListID);
		  //$("div#" + divR + " " + "#frmDatePicker2-" + taskListID).datepicker();
		  $("div#" + divR + " " + "#frmDatePicker2-" + taskListID).datepicker({inline: true,dateFormat: 'yy-mm-dd'});
		  $("div#" + divR + " " + "#btn-task-update").remove();

		  $("#" + divR).css('display', 'block');

		  CKEDITOR.replace( 'frmTaskDescription' );
	  }
	};
	  
	// new task button
	simpris.project.showEditTaskDiv = function(linkid,table,tableRow) {
	  var div = "#" + linkid;
	  var divR = linkid.replace("link-task-edit-","toggle-tk-");
	  // check if div alresdy exists if it does delete it as a toggle
	  if ($('.task-edit-div').length) {
		  $('.task-edit-div').toggle();
		  $('.task-edit-div').remove();
	  }
	  var taskID = linkid.replace("link-task-edit-","");
	  $('#' + table + ' > tbody > tr').eq(tableRow).after('<tr id="table-row-edit-' + taskID + '"><td colspan="5" id="table-row-placeholder-' + taskID + '"></td></tr>');
	  var divP = div.replace("link-task-edit","table-placeholder");
	  $('#toggle-tk-')
	  .clone(true)
	  .attr('id', divR)
	  .appendTo('#table-row-placeholder-' + taskID);
	  var taskListID = table.replace("taskTable_","");
	  $("div#" + divR + " " + "#hidTaskList").attr("value",taskListID);
	  $("div#" + divR + " " + "#hidTaskID").attr("value",taskID);
	  $("div#" + divR + " " + "#frmTaskAdd-taskListID").html(taskListID);
	  $("div#" + divR + " " + "#frmDatePicker-").attr("id","frmDatePicker-" + taskID);
	  $("div#" + divR + " " + "#frmDatePicker-" + taskID).attr("name","frmDatePicker-" + taskID);
	  $("div#" + divR + " " + "#frmDatePicker-" + taskID).datepicker({inline: true,dateFormat: 'yy-mm-dd'});
	  $("div#" + divR + " " + "#frmDatePicker2-").attr("id","frmDatePicker2-" + taskID);
	  $("div#" + divR + " " + "#frmDatePicker2-" + taskID).attr("name","frmDatePicker2-" + taskID);
	  $("div#" + divR + " " + "#frmDatePicker2-" + taskID).datepicker({inline: true,dateFormat: 'yy-mm-dd'});
	  $("div#" + divR + " " + "#btn-task-add").remove();
	  $("div#" + divR + " " + "#header-task-edit").html("Edit task");
	  $("#" + divR).addClass('task-edit-div');

	  // populate visible form with data
	  var taskid = taskID;
	  $.ajax({
		  url: '/api/task/detail/',
		  data: { taskid: taskid},
		  type: 'GET',
	  })
	  .error(function(r){
		  $('#spnError').text(r.statusText);
	  })
	  .success(function(r){
		  // add to page
		  simpris.project.populate_form(taskid,taskListID, r.taskName,r.taskDescription,r.taskType,r.taskPriority,r.taskStatus,r.taskAssignee,r.taskDatePicker,r.taskEstimatedTime,r.taskDependency,r.taskPercentageComplete, r.completionDate, r.phaseID);
	  });

	  $("#" + divR).css('display', 'block');
	};

	// get task data
	simpris.project.populate_form = function(taskid,taskListID,taskName,taskDescription,taskType,taskPriority,taskStatus,taskAssignee,taskDatePicker,taskEstimatedTime,taskDependency,taskPercentageComplete,completionDate,phaseID) {
		var divR = ('toggle-tk-' + taskid);
		$("div#" + divR + " " + "#frmTaskName").val(taskName);
		$("div#" + divR + " " + "#frmTaskDescription").html(taskDescription);
		$("div#" + divR + " " + "#frmTaskType").val(taskType);
		$("div#" + divR + " " + "#frmTaskPriority").val(taskPriority);
		$("div#" + divR + " " + "#frmTaskStatus").val(taskStatus);
		$("div#" + divR + " " + "#frmTaskAssignee").val(taskAssignee);
		if (taskDatePicker !== null) {
		  	var dBDate = new Date(taskDatePicker)
		  	var displayDate = dBDate.getFullYear() + "-" + ('0' + (dBDate.getMonth() + 1)).slice(-2) + "-" + ('0' + (dBDate.getDate())).slice(-2);
		}
		else {
			var displayDate = null;
		}
		//$("div#" + divR + " " + "#frmDatePicker2-" + taskid).val(displayDate2);
		//var dBDate = new Date(taskDatePicker);
		//var displayDate = dBDate.getFullYear() + "-" + ('0' + (dBDate.getMonth()+1)).slice(-2) + "-" + ('0' + (dBDate.getDate())).slice(-2);
		$("div#" + divR + " " + "#frmDatePicker-" + taskid).val(displayDate);
		$("div#" + divR + " " + "#frmEstimatedTime").val(taskEstimatedTime);
		$("div#" + divR + " " + "#frmTaskDependency").val(taskDependency);
		$("div#" + divR + " " + "#frmPercentageComplete").val(taskPercentageComplete);
		if (completionDate !== null) {
		  	var dBDate2 = new Date(completionDate)
		  	var displayDate2 = dBDate2.getFullYear() + "-" + ('0' + (dBDate2.getMonth() + 1)).slice(-2) + "-" + ('0' + (dBDate2.getDate())).slice(-2);
		}
		else {
			var displayDate2 = null;
		}
		$("div#" + divR + " " + "#frmDatePicker2-" + taskid).val(displayDate2);
		$("div#" + divR + " " + "#selPhaseID").val(phaseID);

		CKEDITOR.replace( 'frmTaskDescription' );

	  	simpris.project.get_task_dependencies(simpris.project.project_id_stored, taskDependency);
	};

	// insert new task
	simpris.project.perform_task_create = function() {
		var $form = $('#frmTaskAdd');
	  	var taskListID = $("#hidTaskList", '#frmTaskAdd').val();
	  	var URL = $("#hidURL", '#frmTaskAdd').val();
		var taskName = $("#frmTaskName", "#frmTaskAdd").val();
		var taskDescription = $("#frmTaskDescription", '#frmTaskAdd').val();
		var taskType = $("#frmTaskType", '#frmTaskAdd').val();
		var taskAssignee = $("#frmTaskAssignee", '#frmTaskAdd').val();
		var taskDatePicker = $("#frmDatePicker-" + taskListID, '#frmTaskAdd').val();
		var taskEstimatedTime = $("#frmEstimatedTime", '#frmTaskAdd').val();
		var taskDatePicker2 = $("#frmDatePicker2-" + taskListID, '#frmTaskAdd').val();
		var taskPhaseID = $("#selPhaseID" + taskListID, '#frmTaskAdd').val();
		var taskDependency = $("#frmTaskDependency", '#frmTaskAdd').val();

		var is_valid = simpris.project.validate_task('i', taskListID);
		if (!is_valid) {
			return false;
		}

		var data = $("#frmTaskAdd").serializeArray();
		var ckedited = CKEDITOR.instances.frmTaskDescription.getData();
		data.push({name: 'ckedited', value: ckedited});

		$.ajax({
		  url: '/api/task/insert/',
		  data: data,
		  type: 'POST',
		})
		.error(function(err){
		  $('#spnError').text(err.statusText);
		})
		.success(function(r){
		  // add to page
		  simpris.project.append_task(r.taskid,taskListID,taskName,taskType,r.taskpriority,r.taskstatus,taskAssignee,taskDatePicker,taskEstimatedTime,taskDependency,URL);
		});
	};

	// edit task
	simpris.project.perform_task_update = function() {
	var $form = $('#frmTaskAdd');
	var taskID = $("#hidTaskID", '#frmTaskAdd').val();
	var taskListID = $("#hidTaskList", '#frmTaskAdd').val();
	var URL = $("#hidURL", '#frmTaskAdd').val();
	var taskDescription = $("#frmTaskDescription", '#frmTaskAdd').val();
	var taskType = $("#frmTaskType", '#frmTaskAdd').val();
	var taskAssignee = $("#frmTaskAssignee", '#frmTaskAdd').val();
	var taskDatePicker = $("#frmDatePicker-" + taskID, '#frmTaskAdd').val();
	var taskEstimatedTime = $("#frmEstimatedTime", '#frmTaskAdd').val();
	var taskPercentComplete = $('#frmTaskPercentageComplete', '#frmTaskAdd').val();
	var taskPhaseID = $('#selPhaseID', '#frmTaskAdd').val();
	var taskCompletionDate = $("#frmDatePicker2-" + taskID, '#frmTaskAdd').val();
	var taskDependency = $("#frmTaskDependency", '#frmTaskAdd').val();

	var is_valid = simpris.project.validate_task('u', taskID);
	if (!is_valid) {
		return false;
	}

	var data = $("#frmTaskAdd").serializeArray();
	var ckedited = CKEDITOR.instances.frmTaskDescription.getData();
	data.push({name: 'ckedited', value: ckedited});

	$.ajax({
		url: '/api/task/update/',
		data: data,
		type: 'POST',
	})
	.error(function(err){
		  $('#spnError').text(err.statusText);
	})
	.success(function(r){
		// add to page
		simpris.project.after_update_task(r.taskid);//,taskListID,taskDescription,taskType,r.taskpriority,r.taskstatus,taskAssignee,taskDatePicker,taskEstimatedTime,taskDependency,URL);
	});
	};

	// add new task to tasklist div
	simpris.project.append_task = function(taskid,taskListID,taskName,taskType,taskpriority,taskstatus,taskAssignee,taskDatePicker,taskEstimatedTime,taskDependency,URL) {
	  $( "#toggle-tk-" + taskListID ).toggle();
	  var newContainer = "taskTable_" + taskListID;
	  var jqContainerID = "#" + newContainer + " tbody";
	  $(jqContainerID).append("<tr><td><u>Task</u> " + taskid + "</td><td><a id=\"link-task-edit-" + taskid + "\" href=\"#\" title=\"Edit the task\" class=\"task-edit\"><i class=\"fa fa-edit\"></i>Edit</a></td><td><a href=\"" + URL + "/task/detail/" + taskid + "\">" + taskName + "</a></td><td>" + taskpriority + "</td><td>" + taskstatus + "</td></tr>");
	  $( "#toggle-tk-" + taskListID ).remove();
	  $(jqContainerID).on("click","a",function() { var tableRow = $(this).closest("tr").index(); var table = $(this).closest("table").attr('id'); simpris.project.showEditTaskDiv(this.id,table,tableRow); return false; });
	};

	// remove task update form and tidy up
	simpris.project.after_update_task = function(taskid) {
	  $( "#toggle-tk-" + taskid ).toggle();
	  $( "#toggle-tk-" + taskid ).remove();
	  $( "#table-row-edit-" + taskid ).toggle();
	  $( "#table-row-edit-" + taskid ).remove();
	};

	// Note this is not the only task validation routine - see task.js
	simpris.project.validate_task = function (action, taskListID) {

		// action is i for insert or u for update

		// if insert the form is frmUserAdd else frmUserEdit
		var form = null;
		if (action == "i") {
			form = '#frmTaskAdd';
		}
		else {
			form = '#frmTaskAdd';
		}

		var taskName = $("#frmTaskName", form).val();
		var taskDescription = CKEDITOR.instances.frmTaskDescription.getData();
		var taskType = $("#frmTaskType", form).val();
		var taskPriority = $("#frmTaskPriority", form).val();
		var taskStatus = $("#frmTaskStatus", form).val();
		var taskAssignee = $("#frmTaskAssignee", form).val();
		var taskStartDate = $("#frmDatePicker-" + taskListID, form).val();
		var taskEstimatedTime = $("#frmEstimatedTime").val();
		var taskCompletion = $("#frmDatePicker2-" + taskListID).val();
		var taskPercentageComplete = $("#frmPercentageComplete", form).val();

		var valid = true;

		$('#spnError').text("");

		if (taskName == "") {
			$('#spnError').append("Task name required. " + "<br>");
			valid = false;
		}
		if (taskDescription == "") {
			$('#spnError').append("Task description required. " + "<br>");
			valid = false;
		}
		if (taskType == "") {
			$('#spnError').append("Task type required. " + "<br>");
			valid = false;
		}
		if (taskPriority == "") {
			$('#spnError').append("Task priority required. " + "<br>");
			valid = false;
		}
		if (taskStatus == "") {
			$('#spnError').append("Task status required. " + "<br>");
			valid = false;
		}
		if (taskAssignee == "") {
			$('#spnError').append("Task assignee required. " + "<br>");
			valid = false;
		}
		if (taskEstimatedTime == "" || isNaN(taskEstimatedTime)) {
			$('#spnError').append("Task estimated time required and should be a number. " + "<br>");
			valid = false;
		}
		if (taskPercentageComplete == "" || isNaN(taskPercentageComplete)) {
			$('#spnError').append("Task percent complete required and should be a number. " + "<br>");
			valid = false;
		}

		return valid;
	};

	simpris.project.get_task_dependencies = function (projectID, dependencyID) {
		var projectid = projectID;
		$.ajax({
			url: '/api/task/dependencies/',
			data: { projectid: projectid },
			type: 'GET',
		})
		.error(function(err){
		  	$('#spnError').text(err.statusText);
		})
		.success(function(data){
		  	// add to page
			var dependencies = data.taskDependencies;
			$.each(dependencies, function(index, dependency) {
				$('#frmTaskDependency')
				.append($("<option></option>")
				.attr("value",dependency.taskid)
				.text(dependency.taskname));
				if (dependency.taskid == dependencyID) {
					$('#frmTaskDependency').val(dependency.taskid).prop('selected', true);
				}
			});
		});
	};

});   
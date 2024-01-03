"use strict";

	$(function() {
	  
	  $("#btn-task-create").click(function() {
		  simpris.project.perform_task_create();
		  return false;
	  });
	  
	  $("#btn-task-update").click(function() {
		  simpris.project.perform_task_update();
		  return false;
	  });

	  $("#btn-task-move").click(function() {
		  simpris.project.perform_task_move();
		  return false;
	  });
	  
	  // insert new task
	  simpris.project.perform_task_create = function() {
		  var $form = $('#frmTaskAdd');
		  var taskListID = $("#hidTaskList", '#frmTaskAdd').val();
		  var URL = $("#hidURL", '#frmTaskAdd').val();	   	
		  var taskDescription = $("#frmTaskDescription", '#frmTaskAdd').val();
		  var taskType = $("#frmTaskType", '#frmTaskAdd').val();	   	
		  var taskAssignee = $("#frmTaskAssignee", '#frmTaskAdd').val();
		  var taskDatePicker = $("#frmDatePicker-" + taskListID, '#frmTaskAdd').val();
		  var taskEstimatedTime = $("#frmEstimatedTime", '#frmTaskAdd').val();
		  var taskDependency = $("#frmTaskDependency", '#frmTaskAdd').val();	   	
		
		  $.ajax({
			  url: '/api/task/insert/',
			  data: $("#frmTaskAdd").serialize(),
			  type: 'POST',
		  })
		  .fail(function(err){
			  $('#spnError').text(err.statusText);
			  //console.log("error",err);
		  })
		  .done(function(r){ 
			  //console.log("success", r);
			  //console.log(r.responseText);
			  // add to page    		
			  simpris.project.append_task(r.taskid,taskListID,taskDescription,taskType,r.taskpriority,r.taskstatus,taskAssignee,taskDatePicker,taskEstimatedTime,taskDependency,URL);
		  });
	  };
	  
	  // edit task
	  simpris.project.perform_task_update = function() {
		var $form = $('#frmTaskEdit');

		$('#spnError').empty();

		var valid = simpris.project.validate_task_form("u");

		if (valid == false) {
			return false;
		}

		var data = $('#frmTaskEdit').serializeArray();
		var ckedited = CKEDITOR.instances.frmTaskDescription.getData();
	  	data.push({name: 'ckedited', value: ckedited});

		$.ajax({
		    url: '/api/task/update/',
		    data: data,
		    type: 'POST',
		})
		.fail(function(err){
			  $('#spnError').text(err.statusText);
		})
		.done(function(r){
			//console.log(r.task_id);
			// add to page    		
			window.location.reload(true);
		});
	  };

	  // move task
	  simpris.project.perform_task_move = function() {
		var $form = $('#frmTaskMove');
		var taskMove = $("#frmTaskList", "#frmTaskMove").val();

		$('#spnError').empty();

		if (taskMove == "") {
			$('#spnError').text("Task description required.");
			return false;
		}

		$.ajax({
		    url: '/api/task/move/',
		    data: $("#frmTaskMove").serialize(),
		    type: 'POST',
		})
		.fail(function(err){
			//console.log("error",err);
		})
		.done(function(r){
			//console.log(r.taskid);
			// add to page
			//window.location.reload(true);
			window.location.replace("/task/detail/" + r.taskid);
		});
	  };

	simpris.project.validate_task_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmUserAdd else frmUserEdit
		var form = null;
		if (action == "i") {
			form = '#frmTaskAdd';
		}
		else {
			form = '#frmTaskEdit';
		}

		var taskName = $("#frmTaskName", form).val();
		var taskDescription = $("#frmTaskDescription", form).val();
		var taskType = $("#frmTaskType", form).val();
		var taskPriority = $("#frmTaskPriority", form).val();
		var taskStatus = $("#frmTaskStatus", form).val();
		var taskAssignee = $("#frmTaskAssignee", form).val();
		var taskStartDate = $("#frmDatePicker", form).val();
		var taskEstimatedTime = $("#frmEstimatedTime", form).val();

		var valid = true;

		if (taskDescription == "") {
			$('#spnError').text("Task description required. " + "<br>");
			valid = false;
		}
		if (taskType == "") {
			$('#spnError').text("Task type required. " + "<br>");
			valid = false;
		}
		if (taskPriority == "") {
			$('#spnError').text("Task priority required. " + "<br>");
			valid = false;
		}
		if (taskStatus == "") {
			$('#spnError').text("Task status required. " + "<br>");
			valid = false;
		}

		return valid;
	}

	simpris.project.task_search = function (type) {
		var search_term = $('#txtTask').val();
		if (search_term.length < 3) {
		  return;
		}
		if (type == "sel") {
		  $('#task_list').show();
		  $('#task_list').empty();
		}
		var data = {
		  term: search_term
		};
		$.ajax({
		  url: '/api/task/searchj/',
		  data: data
		})
		.fail(function (r) {
		  //$('#spnError').text("There has been an error: " + r.statusText);
		  $('#div-notification').addClass("alert-danger");
		  $("#div-notification").css('display','block');
		})
		.done(function (r) {
		  if (type == "sel") {
			  $('#task_list').append('<option value="0">Select a task from list</option>');
			  for (var i = 0; i < r.length; i++) {
				  $('#task_list').append('<option value="' + r[i].taskid + '">' + r[i].taskname + '</option>');
				  $("#task_list").css("display", "block");
				  $('#task_list').attr('size', r.length);
			  }
			  $('#task_list').trigger('mousedown');
		  }
		  else if (type == "sch") {
			  $("#schedule-list-0").empty();
			  for (var x = 0; x < r.length; x++) {
				  $('#schedule-list-0').append('<li id="schedule-item-' + r[x].taskid + '" class="schedule-list-item">' +
					  '<div id="status_col_2" class="card card task-item">' +
					  '<div id="item_type"></div>' +
					  '<div id="item_desc" class="card-header">Task ID: ' + r[x].taskid + ' ' + r[x].taskname + '</div>' +
					  '<div class="card-body">' + r[x].taskdescription + '</div>' +
					  '</div></li>');
			  }
		  }
		  else if (type == "kan") {
			  $("#kanban-list-1").empty();
			  for (var y = 0; y < r.length; y++) {
				  $('#kanban-list-1').append('<li id="kanban-item-' + r[y].taskid + '" data-source-column="0" class="kanban-list-item">' +
						'<div id="status_col_1" class="card card bg-primary text-white kanban-item">' +
						'<div class="card-header" id="item_id">Task id:' + r[y].taskid + '</div>' +
					  	'<div class="card-body">' + r[y].taskdescription + '</div>' +
					'</div>' +
				'</li>');
			  }
		  }
		});
	}

	simpris.project.task_search_change = function () {
		var selected_task = $("#task_list").find(":selected").text();
		var selected_task_id = $("#task_list").find(":selected").val();
		//$("#selected_project").text(selected_proj);
		$("#txtTask").val(selected_task);
		$("#hidTaskID").val(selected_task_id);
		$("#task_list").hide();
	};

});   
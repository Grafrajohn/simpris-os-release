"use strict";

$(function() {

    // set effect from select menu value
    $("#button-tkl").click(function() {
    	simpris.project.showTklDiv();
    });

	// create tasklist
    $("#btn-tasklist-create").click(function() {
    	simpris.project.post_tasklist_create();
    	return false;
    });

	// edit tasklist
    $("#btn-tasklist-edit").click(function() {
    	simpris.project.post_tasklist_edit();
    	return false;
    });

	// delete tasklist
    $(".tasklist-delete").click(function() {
		var confirm_delete = confirm("Are you sure you want to delete?");
		if (confirm_delete == false) {
			return;
		}
		var task_id = $(this).attr('id');
		var project_id = $(this).attr('data-project-id');
    	simpris.project.post_tasklist_delete(task_id,project_id);
    	return false;
    });
    
    // edit tasklist link
    $(".tasklist-edit").click(function() {
    	var link = $(this).attr('id');
    	var taskListID = link.replace("tasklist-edit-link-","");
    	simpris.project.showTklEdit(taskListID);
    	return false;
    });

	$("#btn-tasklist-cancel").click(function() {
	  var id = $("#btn-tasklist-cancel").closest("div").attr("id");
	  $('#' + id).toggle();
	  $('#' + id).remove();
	  //$( "#table-row-edit-" + id ).toggle();
	  //$( "#table-row-edit-" + id ).remove();
	  return false;
	});
    
    // show new tasklist div at top of project
    simpris.project.showTklDiv = function() {
    	// run the effect
		if ($("#toggle-tkl-new").length) {
			$("#toggle-tkl-new").toggle();
			$("#toggle-tkl-new").remove();
			return;
		}    	
		$('#toggle-tkl-')
		.clone(true)
		.attr('id', "toggle-tkl-new")
		.appendTo("#placeholder-tasklist-new");
		$("div#toggle-tkl-new #btn-tasklist-edit").remove();			
    	$("#toggle-tkl-new" ).toggle();
    };    
    
    // show edit tasklist div in tasklist parent div
    simpris.project.showTklEdit = function (taskListID) {
    	// clone edit tasklist div into correct div
    	var divP = "placeholder-tkl-" + taskListID;
    	// check if div exists and if so remove it
    	var newDiv = "toggle-tkl-" + taskListID;
		if ($("#" + newDiv).length) {
			$("#" + newDiv).toggle();
			$("#" + newDiv).remove();
			return;
		}
		// clone div
		$('#toggle-tkl-')
		.clone(true)
		.attr('id', newDiv)
		.appendTo("#" + divP);
		// set attributes for new div
		var taskListName = $("#tkl-tasklistname-span", "#tasklistpanel-" + taskListID).text();
		var taskListDescription = $("#tkl-tasklistdescription-para", "#tasklistpanel-" + taskListID).text();
		$("div#" + newDiv + " " + "#frmTaskListName").attr("value",taskListName);
		$("div#" + newDiv + " " + "#frmTaskListDescription").text(taskListDescription);
		$("div#" + newDiv + " " + "#btn-tasklist-create").remove();					
		$("div#" + newDiv + " " + "#hidTasklistID").val(taskListID);		
	    $("#" + newDiv).toggle();  
		$("#" + newDiv).css('display', 'block');
    };    
    
    // create new tasklist via ajax api
    simpris.project.post_tasklist_create = function () {
    	var $form = $('#frmTaskListAdd');
    	var tasklistname = $("#frmTaskListName", '#frmTaskListAdd').val();
    	var tasklistdesc = $("#frmTaskListDescription", '#frmTaskListAdd').val();

		if (tasklistname == "") {
			$("#tklErrors").text("Tasklist name should be entered");
			return false;
		}

		if (tasklistdesc == "") {
			$("#tklErrors").text("Tasklist description should be entered");
			return false;
		}

		$("#tklErrors").text("");

    	$.ajax({
    	    url: '/api/tasklist/insert/',
    	    data: $("#frmTaskListAdd").serialize(),
    	    type: 'POST',

    	}).error(function(r){ 
    		console.log("error",r) 
    	})
    	.success(function(r){ 
    		//console.log("success", r);
    		// add to page    		
    		simpris.project.append_tasklist(r,tasklistname,tasklistdesc);
    	})
    };
    
    // edit existing tasklist via ajax api
    simpris.project.post_tasklist_edit = function () {
    	var $form = $('#frmTaskListAdd');
    	var tasklistid = $("#hidTasklistID", '#frmTaskListAdd').val();    	
    	var tasklistname = $("#frmTaskListName", '#frmTaskListAdd').val();
    	var tasklistdesc = $("#frmTaskListDescription", '#frmTaskListAdd').val();

		if (tasklistname == "") {
			$("#tklErrors").text("Tasklist name should be entered");
			return false;
		}

		if (tasklistdesc == "") {
			$("#tklErrors").text("Tasklist description should be entered");
			return false;
		}

		$("#tklErrors").text("");

    	$.ajax({
    	    url: '/api/tasklist/update/',
    	    data: $("#frmTaskListAdd").serialize(),
    	    type: 'POST',

    	}).error(function(r){ 
    		console.log("error",r) 
    	})
    	.success(function(response){ 
    		//console.log("success", r);
    		// add to page    		
    		simpris.project.update_tasklist(response.tasklistid,response.tasklistname,response.tasklistdescription);
    	})
    };

    // append newly created tasklist to the page and move to it
    simpris.project.append_tasklist = function (r,tasklistname,tasklistdesc) {
	    $("#toggle-tkl-new").toggle(); 
	    $("#toggle-tkl-new").remove(); 	    
	    var newContainer = "tasklist-container-" + r;
	    var jqContainerID = "#" + newContainer;
	    $("#projectPanel").append("<a name=\"anchor-" + r + "\"></a>");
		// do a full deep jquery clone and append to the project panel
        $('#cloneContainerTkl')
        .clone(true)
        .attr('id', newContainer)
        .appendTo("#projectPanel");
        $("div" + jqContainerID + " " + "#tasklist-edit-link-").attr("id", "tasklist-edit-link-" + r);
        $("div" + jqContainerID + " " + "#tasklistspan").text(r + "  " + tasklistname);
        $("div" + jqContainerID + " " + "#taskdescpara").text(tasklistdesc);
        var _href = $("div" + jqContainerID + " " + "#tasklistlink").attr("href");
        $("div" + jqContainerID + " " + "#tasklistlink").attr("href", _href + r);
        $("div" + jqContainerID + " " + "#button-tk-").attr("id", "button-tk-" + r);
        $(jqContainerID).css('display', '');
        window.location.hash = "#anchor-" + r;
		window.location.reload(true);
    };
    
    // append newly created tasklist to the page and move to it
    simpris.project.update_tasklist = function (tasklistid,tasklistname,tasklistdesc) {
	    //$("#toggle-tkl-" + tasklistid).toggle(); 
	    $("#toggle-tkl-" + tasklistid).remove(); 	    
        $("div#tasklistpanel-" + tasklistid + " #tkl-tasklistdescription-para").text(tasklistdesc);
        $("div#tasklistpanel-" + tasklistid + " #tkl-tasklistname-span").text(tasklistname);
        location.hash = "#anchor-" + tasklistid;
    };    
  });
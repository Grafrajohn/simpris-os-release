"use strict";

$(function () {

	// button click to add project user
	$("#btn-project-user-add").click(function () {
		simpris.project.post_project_user_create();
		return false;
    });

	// button click to delete project user
	$(".btn-project-user-delete").click(function () {
		var link = $(this).attr('id');
    	var userProjectID = link.replace("btn-project-user-delete-", "");
		simpris.project.post_project_user_delete(userProjectID);
		return false;
    });

	// button click to edit project
	$("#btn-project-edit").click(function () {
		simpris.project.post_project_edit();
		return false;
    });

	// button click to add project
	$("#btn-project-create").click(function () {
		var status = simpris.project.post_project_create();
		return false;
    });

	// button click to add link
	$("#btnAddLink").click(function () {
		var status = simpris.project.post_project_link_create();
		return false;
    });

    // create new project via ajax api
    simpris.project.post_project_create = function () {
    	var $form = $('#frmProjectAdd');
    	var projectOrganisation = $("#frmProjectOrganisation", '#frmProjectAdd').val();
    	var projectname = $("#frmProjectName", '#frmProjectAdd').val();
    	//var projectdesc = $("#frmProjectDescription", '#frmProjectAdd').val();
		var projectdesc = CKEDITOR.instances.frmProjectDescription.getData();
    	var projectBudget = $("#frmProjectBudget", '#frmProjectAdd').val();
		var projectImportance = $("#frmProjectImportance", '#frmProjectAdd').val();

		var valid = true;
		$('#div-notification').text('');

		if (projectOrganisation == '') {
			$('#div-notification').text('Organisation must be selected. ');
			valid = false;
		}
		if (projectname == '') {
			$('#div-notification').append('Project name must be completed. ');
			valid = false;
		}
		if (projectdesc == '') {
			$('#div-notification').append('Project description must be completed. ');
			valid = false;
		}
		if (projectBudget != '' && isNaN(projectBudget) == true ) {
			$('#div-notification').append('Project budget must be numeric if entered. ');
			valid = false;
		}
		if (projectImportance == '') {
			$('#div-notification').append('Project importance must be selected. ');
			valid = false;
		}

		if (valid == false) {
            $('#div-notification').addClass("alert-danger");
			$("#div-notification").css('display','block');
			return false;
		}

		var data = $("#frmProjectAdd").serializeArray();
		var ckeditedDescription = CKEDITOR.instances.frmProjectDescription.getData();
		var ckeditedDeliverables = CKEDITOR.instances.frmProjectDeliverables.getData();
	  	data.push({name: 'ckeditedDescription', value: ckeditedDescription});
	  	data.push({name: 'ckeditedDeliverables', value: ckeditedDeliverables});

    	$.ajax({
    	    url: '/api/project/insert/',
    	    data: data,
    	    type: 'POST'
    	}).error(function (r) {
			$('#div-notification').text("There has been an error - check your form carefully");
    	})
    	.success(function(r){
    		$('#div-notification').text("Project successfully created");
            if (r.project_id == null && r.projectid == null) {
                window.location.replace("/projectlist");
            }
            else {
                window.location.replace("/project/detail/" + r.project_id);
            }
    	});
    }

    // create new project link via ajax api
    simpris.project.post_project_link_create = function () {
    	var $form = $('#frmLinkAdd');
    	var project_link = $("#txtProjectLink" ).text();
    	$.ajax({
    	    url: '/api/project/insertlink/',
    	    data: $("#frmlinkAdd").serialize(),
    	    type: 'POST'
    	}).error(function(response){
            $('#div-notification2').text("There has been an error: " + response.statusText);
    	})
    	.success(function(response){
			window.location.reload(true);
    	});
    };
	
    // create new project user via ajax api
    simpris.project.post_project_user_create = function () {
    	var $form = $('#form-project-user');
    	var project_user = $("#selProjectUser :selected" ).text();
    	$.ajax({
    	    url: '/api/project/insertuser/',
    	    data: $("#form-project-user").serialize(),
    	    type: 'POST'
    	}).error(function(response){
            $('#div-notification2').text("There has been an error: " + response.statusText);
    	})
    	.success(function(response){
			window.location.reload(true);
    	});
    };

	// delete project user via ajax api
    simpris.project.post_project_user_delete = function (user_project_id) {
		var post_data = $('#form-project-user').serializeArray();
		post_data.push({name: 'user_project_id', value: user_project_id});
    	$.ajax({
    	    url: '/api/project/deleteuser/',
    	    data: post_data,
    	    type: 'POST'
    	}).error(function(response){
            $('#div-notification2').text("There has been an error: " + response.statusText);
    	})
    	.success(function(response){
			window.location.reload(true);
    	});
    };
    
    // edit existing project via ajax api
    simpris.project.post_project_edit = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_project_form("u");

		if (valid == false) {
            $('#div-notification').addClass("alert-danger");
			$("#div-notification").css('display','block');
			return false;
		}

		var data = $("#frmProjectEdit").serializeArray();
		var ckeditedDescription = CKEDITOR.instances.frmProjectDescription.getData();
		var ckeditedDeliverables = CKEDITOR.instances.frmProjectDeliverables.getData();
	  	data.push({name: 'ckeditedDescription', value: ckeditedDescription});
	  	data.push({name: 'ckeditedDeliverables', value: ckeditedDeliverables});

    	$.ajax({
    	    url: '/api/project/update/',
    	    data: data,
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text("There has been an error: " + r.responseText);
			$('#div-notification').addClass("alert-danger");
			$("#div-notification").css('display','block');
    	})
    	.success(function(r){
            $('#div-notification').text("Project successfully updated");
			window.location.replace("/project/edit/" + r);
    	});
    };    
    
    // append newly created project to the page and move to it
    simpris.project.append_project_user = function (r, project_user) {
		$('#tabProjectUsers tr:last').after('<tr><td>' + project_user + '</td></tr>');
    };

	simpris.project.validate_project_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmorganisationAdd else frmorganisationEdit
		var form = null;
		if (action == "i") {
			form = '#frmProjectAdd';
		}
		else {
			form = '#frmProjectEdit';
		}

		var projectName = $("#frmProjectName", form).val();
		var projectDescription = CKEDITOR.instances.frmProjectDescription.getData();
		var projectManager = $("#frmProjectManager", form).val();
		var projectStakeholder = $("#frmProjectStakeholder", form).val();
		var projectBudget = $("#frmProjectBudget", form).val();

		var valid = true;

		if (projectName == "") {
			$('#div-notification').text("Project name required. ");
			valid = false;
		}

		if (projectDescription == "") {
			$('#div-notification').append("Project description required. ");
			valid = false;
		}

		if (action == "u") {
			if (projectStakeholder == "" || projectStakeholder == "0") {
				$('#div-notification').append("Project stakeholder required. ");
				valid = false;
			}
		}

		if (action == "u") {
			if (projectManager == "" || projectManager == "0") {
				$('#div-notification').append("Project manager required. ");
				valid = false;
			}
		}

		if (projectBudget != "") {
			if (isNaN(projectBudget)) {
				$('#div-notification').append("Budget must be whole number with no decimal places or commas");
				valid = false;
			}
			else if (projectBudget != parseInt(projectBudget)) {
				$('#div-notification').append("Budget must be whole number with no decimal places or commas");
				valid = false;
			}
		}

		return valid;
	}
  });
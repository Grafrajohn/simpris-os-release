/**
 * Created by Graham on 13/09/2015.
 */
"use strict";

$(function () {

	// button click to edit problem
	$("#btn-problem-edit").click(function () {
		simpris.project.post_problem_edit();
		return false;
    });

	// button click to add problem
	$("#btn-problem-create").click(function () {
		var status = simpris.project.post_problem_create();
		return false;
    });

	// label click to select problem filter
	$(".problem-radio").click(function () {
		var filter = $('input[name=range]:checked').val();
		var status = simpris.project.filter_problems(filter);
    });

	// select click to select queue
	$(".queue-select").change(function () {
		$(".problem-radio").each(function(){
				$(this).prop('checked', false);
			}
		)
		var queue = $(this).find(":selected").val();
		var status = simpris.project.filter_problems(queue);
    });

    // create new problem via ajax api
    simpris.project.post_problem_create = function () {

		$('#div-notification').empty();

		tinyMCE.triggerSave();

		var valid = simpris.project.validate_problem_form("i");

		if (valid == false) {
			return false;
		}

    	var $form = $('#frmProblemAdd');
    	var problemHeader = $("#frmProblemHeader", '#frmProblemAdd').val();
    	var problemDescription = $("#frmProblemDescription", '#frmProblemAdd').val();
    	var problemType = $("#frmProblemType", '#frmProblemAdd').val();
    	var problemSubtype = $("#frmProblemSubType", '#frmProblemAdd').val();
    	var problemNoAffected = $("#frmNoofPeopleAffected", '#frmProblemAdd').val();
    	var problemScope = $("#frmProblemScope", '#frmProblemAdd').val();
    	var problemStatus = $("#frmProblemStatus", '#frmProblemAdd').val();
    	var problemPriority = $("#frmproblemPriority", '#frmProblemAdd').val();
    	var problemQueue = $("#frmproblemPriority", '#frmProblemQueue').val();
    	$.ajax({
    	    url: '/api/problem/insert/',
    	    data: $("#frmProblemAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error");
    	})
    	.success(function(r){
    		$('#spnError').text("Problem successfully created");
            if (r.problem_id == null && r.problemid == null) {
                window.location.replace("/problemlist");
            }
            else {
                window.location.replace("/problem/detail/" + r.problem_id);
            }
    	});
    }

    // edit existing problem via ajax api
    simpris.project.post_problem_edit = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_problem_form("u");

		if (valid == false) {
			return false;
		}

		tinyMCE.triggerSave();

    	var $form = $('#frmProblemEdit');
    	var problemHeader = $("#frmProblemHeader", '#frmProblemEdit').val();
    	var problemDescription = $("#frmProblemDescription", '#frmProblemEdit').val();
    	var problemType = $("#frmProblemType", '#frmProblemEdit').val();
    	var problemSubType = $("#frmProblemSubType", '#frmProblemEdit').val();
    	var problemNoAffected = $("#frmNoofPeopleAffected", '#frmProblemEdit').val();
    	var problemScope = $("#frmProblemScope", '#frmProblemEdit').val();
    	var problemStatus = $("#frmProblemStatus", '#frmProblemEdit').val();
    	var problemPriority = $("#frmProblemPriority", '#frmProblemEdit').val();
    	var problemAssignee = $("#frmProblemAssignee", '#frmProblemEdit').val();
    	var problemQueue = $("#frmProblemQueue", '#frmProblemEdit').val();
    	var projectLink = $("#frmProjectLink", '#frmProblemEdit').val();
    	var problemLink = $("#frmProblemLink", '#frmProblemEdit').val();
    	$.ajax({
    	    url: '/api/problem/update/',
    	    data: $("#frmProblemEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text("There has been an error " + r.responseText);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
            window.location.reload(true);
    	});
    };

	simpris.project.validate_problem_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmorganisationAdd else frmorganisationEdit
		var form = null;
		if (action === "i") {
			form = '#frmProblemAdd';
		}
		else {
			form = '#frmProblemEdit';
		}

		var problemOrganisation = $("#frmOrganisation", form).val();
		var problemHeader = $("#frmProblemHeader", form).val();
		var problemDescription = $("#frmProblemDescription", form).val();
		var problemType = $("#frmProblemType", form).val();
		var problemSubType = $("#frmProblemSubType", form).val();
		var problemNoAffected = $("#frmNoofPeopleAffected", form).val();
		var problemScope = $("#frmProblemScope", form).val();
		var problemStatus = $("#frmProblemStatus", form).val();
		var problemPriority = $("#frmProblemPriority", form).val();
		var problemAssignee = "";
		if (action === "u") {
			problemAssignee = $("#frmProblemAssignee", form).val();
		}

		var valid = true;

		if (problemOrganisation === "" && action === "i") {
			$('#div-notification').append("Problem organisation required. ");
			valid = false;
		}

		if (problemHeader === "") {
			$('#div-notification').append("Problem name required. ");
			valid = false;
		}

		if (problemDescription === "") {
			$('#div-notification').append("Problem description required. ");
			valid = false;
		}

		if (problemType === "") {
			$('#div-notification').append("Problem type required. ");
			valid = false;
		}

		if (problemSubType === "") {
			$('#div-notification').append("Problem subtype required. ");
			valid = false;
		}

		if (problemNoAffected === "") {
			$('#div-notification').append("Problem no of people affected required. ");
			valid = false;
		}

		if (problemScope == "") {
			$('#div-notification').append("Problem scope required. ");
			valid = false;
		}

		if (problemStatus == "") {
			$('#div-notification').append("Problem status required. ");
			valid = false;
		}

		if (problemPriority == "") {
			$('#div-notification').append("Problem priority required. ");
			valid = false;
		}

		// if (problemAssignee == "" && action == "u") {
		// 	$('#div-notification').append("Problem assignee required. ");
		// 	valid = false;
		// }

		if (valid == false) {
			$('#div-notification').addClass("alert-danger");
			$("#div-notification").css('display','block');
		}

		return valid;
	};

	simpris.project.filter_problems = function (filter) {
		$('#tbProblemIndex').dataTable( {
			destroy: true,
			"language": {
				"zeroRecords": "No records to display"
			},
			"pageLength": 20,
			"ajax": "/api/problem/problems/" + filter + "/",
			"sAjaxDataProp": "",
			"data_id": "problemid",
			"sEmptyTable" : "No data found",
			"dom": 'Bfrtip',
			"buttons": [
				'copy', 'csv', 'excel', 'pdf', 'print'
			],
			"select": true,
			"columns": [
				{ "className": "hidden-xs","render": function (data, type, row) {
				return '<a id="lnk-problem-delete-' + row.problemid + '" href="#" onclick="simpris.project.problem_delete(' + row.problemid + ')" class="lnk-problem-delete" title="Delete"><i class="fas fa-trash" style="color: red;"></a>';
				} },
				{ "className": "hidden-xs","render": function ( data, type, row) {
				return '<a href="' + simpris.base_url + '/problem/edit/' + row.problemid + '" title="Edit"><i class="fa fa-edit" style="color: scarlet;"></a>';
				} },
				{ "render": function ( data, type, row) {
				return '<a href="' + simpris.base_url + '/problem/detail/' + row.problemid + '" title="View"><i class="fa fa-eye" style="color: green;"></a>';
				} },
				{ "title": "Problem","mDataProp": "problemheader"},
				{ "title": "Problem Type" ,"mDataProp": "problemtype"},
				{ "className": "hidden-xs","title": "Problem Priority" ,"mDataProp": "problempriority"},
				{ "className": "hidden-xs","title": "Problem Scope" ,"mDataProp": "problemscope"},
				{ "className": "hidden-xs hidden-sm","title": "Assignee", "render": function ( data, type, row) {
				return row.first_name + ' ' + row.last_name;
				} },
			]
		} );
    };

  });
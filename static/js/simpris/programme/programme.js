/**
 * Created by Graham on 13/09/2015.
 */
"use strict";

$(function () {

	// button click to edit programme
	$("#btn-programme-edit").click(function () {
		simpris.project.post_programme_edit();
		return false;
    });

	// button click to add programme
	$("#btn-programme-create").click(function () {
		var status = simpris.project.post_programme_create();
		return false;
    });

    // create new programme via ajax api
    simpris.project.post_programme_create = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_programme_form("i");

		if (valid == false) {
			return false;
		}

    	var $form = $('#frmProgrammeAdd');
    	var programmeHeader = $("#frmProgrammeName", '#frmProgrammeAdd').val();
    	var programmeDescription = $("#frmProgrammeDescription", '#frmProgrammeAdd').val();

    	$.ajax({
    	    url: '/api/programme/insert/',
    	    data: $("#frmProgrammeAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error");
    	})
    	.success(function(r){
    		$('#div-notification').text("Programme successfully created");
            if (r.programme_id == null) {
                window.location.replace("/programme/list");
            }
            else {
                window.location.replace("/programme/detail/" + r.programme_id);
            }
    	});
    }

    // edit existing programme via ajax api
    simpris.project.post_programme_edit = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_programme_form("u");

		if (valid == false) {
			return false;
		}

    	var $form = $('#frmProgrammeEdit');
    	var programmeName = $("#frmProgrammeName", '#frmProgrammeEdit').val();
    	var programmeDescription = $("#frmProgrammeDescription", '#frmProgrammeEdit').val();

    	$.ajax({
    	    url: '/api/programme/update/',
    	    data: $("#frmProgrammeEdit").serialize(),
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

	simpris.project.validate_programme_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmorganisationAdd else frmorganisationEdit
		var form = null;
		if (action === "i") {
			form = '#frmProgrammeAdd';
		}
		else {
			form = '#frmProgrammeEdit';
		}

		var programmeName = $("#frmProgrammeName", form).val();
		var programmeDescription = $("#frmProgrammeDescription", form).val();
		var programmeAssignee = "";

		var valid = true;

		if (programmeName === "") {
			$('#div-notification').append("programme name required. ");
			valid = false;
		}

		if (programmeDescription === "") {
			$('#div-notification').append("programme description required. ");
			valid = false;
		}

		if (valid == false) {
			$('#div-notification').addClass("alert-danger");
			$("#div-notification").css('display','block');
		}

		return valid;
	}

  });
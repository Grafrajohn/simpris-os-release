/**
 * Created by Graham on 21/01/2016.
 */
'use strict';

$(function () {

	// button click to edit phase
	$("#btn-phase-edit").click(function () {
		simpris.project.post_phase_edit();
		return false;
    });

	// button click to add phase
	$("#btn-phase-create").click(function () {
		var status = simpris.project.post_phase_create();
		return false;
    });

    // create new phase via ajax api
    simpris.project.post_phase_create = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_phase_form("i");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/phase/insert/',
    	    data: $("#frmPhaseAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(r){
            if (r.phase_id == null) {
                window.location.replace("/clientlist");
            }
            else {
                window.location.replace("/phase/detail/" + r.phase_id);
            }
    	});
    };

    // edit existing phase via ajax api
    simpris.project.post_phase_edit = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_phase_form("u");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/phase/update/',
    	    data: $("#frmPhaseEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("phase successfully updated");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_phase_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmphaseAdd else frmphaseEdit
		var form = null;
		if (action == "i") {
			form = '#frmPhaseAdd';
		}
		else {
			form = '#frmPhaseEdit';
		}

		var phaseName = $("#frmPhaseName", form).val();
		var phaseDescription = $("#frmPhaseDescription", form).val();

		var valid = true;

		if (phaseName == "") {
			$('#spnError').append("phase name required. ");
			valid = false;
		}

		return valid;
	};
  });
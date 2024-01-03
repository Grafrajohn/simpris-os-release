/**
 * Created by Graham on 27/09/2015.
 */

$(function () {

	// button click to edit time
	$("#btn-time-edit").click(function () {
		simpris.project.post_time_edit();
		return false;
    });

	// button click to add time
	$("#btn-time-create").click(function () {
		simpris.project.post_time_create();
		return false;
    });

    // create new time via ajax api
    simpris.project.post_time_create = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_time_form("i");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/time/insert/',
    	    data: $("#frmTimeAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(r){
            if (r.time_id == null) {
                window.location.replace("/timelist");
            }
            else {
                window.location.replace("/time/detail/" + r.time_id);
            }
    	});
    }

    // edit existing time via ajax api
    simpris.project.post_time_edit = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_time_form("u");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/time/update/',
    	    data: $("#frmTimeEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').text("time successfully updated");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_time_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmTimeAdd else frmTimeEdit
		var form = null;
		if (action == "i") {
			form = '#frmTimeAdd';
		}
		else {
			form = '#frmTimeEdit';
		}

		var datePicker = $("#frmDatePicker", form).val();
		var timeType = $("#frmTimeType", form).val();
		var comment = $("#frmComment", form).val();
		var hoursIn = $("#frmHours", form).val();
		var minsIn = $("#frmMins", form).val();
		var task = $("#frmTaskID", form).val();

		var valid = true;

		if (action == "i" && !datePicker) {
			$('#spnError').append("Date required. " + "<br>");
			valid = false;
		}
		if (action == "i" && (hoursIn == 0 && minsIn == 0)) {
			$('#spnError').append("Hours and minutes required. " + "<br>");
			valid = false;
		}
		if (action == "i" && !task) {
			$('#spnError').append("Task required. " + "<br>");
			valid = false;
		}
		if (!timeType) {
			$('#spnError').append("Time type required. " + "<br>");
			valid = false;
		}
		//if (action == "i" && comment == "") {
		//	$('#spnError').append("Time type required. " + "<br>");
		//	valid = false;
		//}

		return valid;
	}
  });
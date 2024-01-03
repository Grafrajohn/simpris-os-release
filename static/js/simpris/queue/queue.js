/**
 * Created by Graham on 21/01/2016.
 */
'use strict';

$(function () {

	// button click to edit queue
	$("#btn-queue-edit").click(function () {
		simpris.project.post_queue_edit();
		return false;
    });

	// button click to add queue
	$("#btn-queue-create").click(function () {
		var status = simpris.project.post_queue_create();
		return false;
    });

	// button click to add queue member
	$("#btn-queue-member-add").click(function () {
		var status = simpris.project.add_queue_member();
		return false;
    });

	// button click to add queue team
	$("#btn-queue-team-add").click(function () {
		var status = simpris.project.add_queue_team();
		return false;
    });

	// button click to delete queue member
	$(".btn-queue-member-delete").click(function () {
		var queue_member_id = $(this).attr('id').replace('btn-queue-member-delete-','');
		var queue_id = $(this).attr("data-queue-id");
		var id = $(this).attr("data-id");
		var status = simpris.project.delete_queue_member(id, queue_id, queue_member_id);
		return false;
    });

	// button click to delete queue team
	$(".btn-queue-team-delete").click(function () {
		var queue_team_id = $(this).attr('id').replace('btn-queue-team-delete-','');
		var queue_id = $(this).attr("data-queue-id");
		var id = $(this).attr("data-id");
		var status = simpris.project.delete_queue_team(id, queue_id, queue_team_id);
		return false;
    });

    // create new queue via ajax api
    simpris.project.post_queue_create = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_queue_form("i");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/queue/insert/',
    	    data: $("#frmQueueAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(r){
            if (r.queue_id == null) {
                window.location.replace("/clientlist");
            }
            else {
                window.location.replace("/queue/detail/" + r.queue_id);
            }
    	});
    };

    // edit existing queue via ajax api
    simpris.project.post_queue_edit = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_queue_form("u");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/queue/update/',
    	    data: $("#frmQueueEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("queue successfully updated");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_queue_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmqueueAdd else frmqueueEdit
		var form = null;
		if (action == "i") {
			form = '#frmQueueAdd';
		}
		else {
			form = '#frmQueueEdit';
		}

		var queueName = $("#frmQueueName", form).val();
		var queueDescription = $("#frmQueueDescription", form).val();

		var valid = true;

		if (queueName == "") {
			$('#spnError').append("queue name required. ");
			valid = false;
		}

		return valid;
	};

    // add queue member
    simpris.project.add_queue_member = function () {

		$('#spnError').empty();
		var selected_queue_member = $('#selQueueMember').val();
		if (selected_queue_member == undefined || selected_queue_member == "") {
			$('#spnError').text("Please select someone to add to queue");
			return false;
		}

    	$.ajax({
    	    url: '/api/queue/member_create/',
    	    data: $("#form-queue-member").serialize(),
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Queue member successfully created");
            window.location.reload(true);
    	});
    };

    // add queue team
    simpris.project.add_queue_team = function () {

		$('#spnError').empty();
		var selected_queue_team = $('#selQueueTeam').val();
		if (selected_queue_team == undefined || selected_queue_team == "") {
			$('#spnError').text("Please select a team to add to queue");
			return false;
		}

    	$.ajax({
    	    url: '/api/queue/team_create/',
    	    data: $("#form-queue-team").serialize(),
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Queue team successfully created");
            window.location.reload(true);
    	});
    };

    // delete queue member
    simpris.project.delete_queue_member = function (id, queue_id, queue_member_id) {

		$('#spnError').empty();

		if (queue_member_id == undefined || queue_member_id == "") {
			$('#spnError').text("Please select someone to delete from queue");
			return false;
		}
		if (queue_id == undefined || queue_id == "") {
			$('#spnError').text("Please select someone to delete from queue");
			return false;
		}

		var data = {
                    csrfmiddlewaretoken: simpris.csrf_token,
                    queue_member_id: queue_member_id,
					queue_id: queue_id,
					id: id
                    };

    	$.ajax({
    	    url: '/api/queue/member_delete/',
    	    data: data,
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Queue member successfully deleted");
            window.location.reload(true);
    	});
    };

    // delete queue team
    simpris.project.delete_queue_team = function (id, queue_id, queue_team_id) {

		$('#spnError').empty();

		if (queue_team_id == undefined || queue_team_id == "") {
			$('#spnError').text("Please select  a team to delete from queue");
			return false;
		}
		if (queue_id == undefined || queue_id == "") {
			$('#spnError').text("Please select a team to delete from queue");
			return false;
		}

		var data = {
                    csrfmiddlewaretoken: simpris.csrf_token,
                    queue_team_id: queue_team_id,
					queue_id: queue_id,
					id: id
                    };

    	$.ajax({
    	    url: '/api/queue/team_delete/',
    	    data: data,
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Queue team successfully deleted");
            window.location.reload(true);
    	});
    };

});
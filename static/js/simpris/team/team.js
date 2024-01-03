/**
 * Created by Graham on 21/01/2016.
 */
'use strict';

$(function () {

	// button click to edit team
	$("#btn-team-edit").click(function () {
		simpris.project.post_team_edit();
		return false;
    });

	// button click to add team
	$("#btn-team-create").click(function () {
		var status = simpris.project.post_team_create();
		return false;
    });

	// button click to add team member
	$("#btn-team-member-add").click(function () {
		var status = simpris.project.add_team_member();
		return false;
    });

	// button click to delete team member
	$(".btn-team-member-delete").click(function () {
		var team_member_id = $(this).attr('id').replace('btn-team-member-delete-','');
		var team_id = $(this).attr("data-team-id");
		var id = $(this).attr("data-id");
		var status = simpris.project.delete_team_member(id, team_id, team_member_id);
		return false;
    });

    // create new team via ajax api
    simpris.project.post_team_create = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_team_form("i");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/team/insert/',
    	    data: $("#frmTeamAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(r){
            if (r.team_id == null) {
                window.location.replace("/clientlist");
            }
            else {
                window.location.replace("/team/detail/" + r.team_id);
            }
    	});
    };

    // edit existing team via ajax api
    simpris.project.post_team_edit = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_team_form("u");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/team/update/',
    	    data: $("#frmTeamEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("team successfully updated");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_team_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmteamAdd else frmteamEdit
		var form = null;
		if (action == "i") {
			form = '#frmTeamAdd';
		}
		else {
			form = '#frmTeamEdit';
		}

		var teamName = $("#frmTeamName", form).val();
		var teamDescription = $("#frmTeamDescription", form).val();

		var valid = true;

		if (teamName == "") {
			$('#spnError').append("team name required. ");
			valid = false;
		}

		return valid;
	};

    // add team member
    simpris.project.add_team_member = function () {

		$('#spnError').empty();
		var selected_team_member = $('#selTeamMember').val();
		if (selected_team_member == undefined || selected_team_member == "") {
			$('#spnError').text("Please select someone to add to team");
			return false;
		}

    	$.ajax({
    	    url: '/api/team/member_create/',
    	    data: $("#form-team-member").serialize(),
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Team member successfully created");
            window.location.reload(true);
    	});
    };

    // delete team member
    simpris.project.delete_team_member = function (id, team_id, team_member_id) {

		$('#spnError').empty();

		if (team_member_id == undefined || team_member_id == "") {
			$('#spnError').text("Please select someone to delete from team");
			return false;
		}
		if (team_id == undefined || team_id == "") {
			$('#spnError').text("Please select someone to delete from team");
			return false;
		}

		var data = {
                    csrfmiddlewaretoken: simpris.csrf_token,
                    team_member_id: team_member_id,
					team_id: team_id,
					id: id
                    };

    	$.ajax({
    	    url: '/api/team/member_delete/',
    	    data: data,
    	    type: 'POST'
    	})
		.error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').css('color','green');
            $('#spnError').text("Team member successfully deleted");
            window.location.reload(true);
    	});
    };

});
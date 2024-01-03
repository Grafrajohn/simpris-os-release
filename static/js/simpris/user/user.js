/**
 * Created by Graham on 22/09/2015.
 */
"use strict";

$(function () {

	// button click to edit user
	$("#btn-user-edit").click(function () {
		simpris.project.post_user_edit();
		return false;
    });

	// button click to add user
	$("#btn-user-create").click(function () {
		var status = simpris.project.post_user_create();
		return false;
    });

	// button click to edit profile
	$("#btn-user-profile").click(function () {
		var status = simpris.project.post_user_profile();
		return false;
    });

	// button click to edit profile
	$("#butUserProjectAdd").click(function () {
		var status = simpris.project.post_user_project_create();
		return false;
    });

    // create new user via ajax api
    simpris.project.post_user_create = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_user_form("i");

		if (valid == false) {
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
			return false;
		}

    	$.ajax({
    	    url: '/api/user/insert/',
    	    data: $("#frmUserAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
            $('#div-notification').text("There has been an error " + r.responseJSON.username[0]);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(r){
            if (r.user_id == null) {
                window.location.replace("/userlist");
            }
            else {
                window.location.replace("/user/detail/" + r.user_id);
            }
    	});
    }

    // edit existing user via ajax api
    simpris.project.post_user_edit = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_user_form("u");

		if (valid == false) {
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
			return false;
		}

    	$.ajax({
    	    url: '/api/user/update/',
    	    data: $("#frmUserEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text("There has been an error " + r.responseJSON.username[0]);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
            $('#div-notification').text("User successfully updated");
            window.location.reload(true);
    	});
    };

    // edit existing user via ajax api
    simpris.project.post_user_profile = function () {

		$('#div-notification').empty();

		var valid = simpris.project.validate_user_profile_form("u");

		if (valid == false) {
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
			return false;
		}

    	$.ajax({
    	    url: '/api/user/profile/',
    	    data: $("#frmProfile").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text("There has been an error " + r.responseJSON.username[0]);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
            $('#div-notification').text("User successfully updated");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_user_profile_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmUserAdd else frmUserEdit
		var form = null;
		if (action == "i") {
			form = '#frmProfile';
		}
		else {
			form = '#frmProfile';
		}

		var email = $("#frmEmail", form).val();
		var phone = $("#frmPhone", form).val();

		var valid = true;

		if (email == "") {
			$('#div-notification').append("Email required. " + "<br>");
			valid = false;
		}
		else {
			// regex to validate emails
			var re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
			valid = re.test(email);
			if (valid == false) {
				$('#div-notification').append("Email should be in correct format. " + "<br>");
            	$('#div-notification').addClass("alert-danger");
            	$("#div-notification").css('display','block');
				valid = false;
			}
		}

		return valid;
	}

	simpris.project.validate_user_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmUserAdd else frmUserEdit
		var form = null;
		if (action == "i") {
			form = '#frmUserAdd';
		}
		else {
			form = '#frmUserEdit';
		}

		var username = $("#frmUsername", form).val();
		var firstName = $("#frmFirstName", form).val();
		var lastName = $("#frmLastName", form).val();
		var email = $("#frmEmail", form).val();
		var phone = $("#frmPhone", form).val();
		var password = "";
		var passwordConfirm = "";
		if (action == "i") {
			password = $("#frmPassword", form).val();
			passwordConfirm = $("#frmPasswordConfirm", form).val();
		}
		var organisation = $("#frmOrganisation", form).val();

		var valid = true;

		if (action == "i" && (username == "" || username.length < 8)) {
			$('#div-notification').append("Username required and should be at least 8 characters length. " + "<br>");
			valid = false;
		}
		if (firstName == "") {
			$('#div-notification').append("First name required. " + "<br>");
			valid = false;
		}
		if (lastName == "") {
			$('#div-notification').append("Last name required. " + "<br>");
			valid = false;
		}
		if (email == "") {
			$('#div-notification').append("Email required. " + "<br>");
			valid = false;
		}
		else {
			// regex to validate emails
			var re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
			valid = re.test(email);
			if (valid == false) {
				$('#div-notification').append("Email should be in correct format. " + "<br>");
				valid = false;
			}
		}
		if (action == "i" && (password == "" || password.length < 8)) {
			$('#div-notification').append("Password required and should be at least 8 characters in length. " + "<br>");
			valid = false;
		}
		if (action == "i" && (passwordConfirm == "" || passwordConfirm.length < 8)) {
			$('#div-notification').append("Password confirm required and should be at least 8 characters in length. " + "<br>");
			valid = false;
		}
		if (action == "i" && password != passwordConfirm) {
			$('#div-notification').append("Passwords should match. " + "<br>");
			valid = false;
		}
		if (organisation == "") {
			$('#div-notification').append("Organisation required. " + "<br>");
			valid = false;
		}

		return valid;
	}

    // create new project user via ajax api
    simpris.project.post_user_project_create = function () {
    	var $form = $('#frmUserProject');
    	var project_user = $("#selUserProject :selected" ).text();
    	$.ajax({
    	    url: '/api/project/insertuser/',
    	    data: $("#frmUserProject").serialize(),
    	    type: 'POST'
    	}).error(function(response){
            $('#div-notification2').text("There has been an error: " + response.responseText);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
			window.location.reload(true);
    	});
    };
  });
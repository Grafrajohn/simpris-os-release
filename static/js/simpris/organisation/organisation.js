/**
 * Created by Graham on 24/09/2015.
 */

'use strict';


$(function () {

	// button click to edit organisation
	$("#btn-organisation-edit").click(function () {
		simpris.project.post_organisation_edit();
		return false;
    });

	// button click to add organisation
	$("#btn-organisation-create").click(function () {
		var status = simpris.project.post_organisation_create();
		return false;
    });

	// button click to add organisation
	$(".btn-organisation-user-delete").click(function () {
		var link = $(this).attr('id');
    	var organisationUserID = link.replace("btn-organisation-user-delete-", "");
		var status = simpris.project.post_organisation_user_delete(organisationUserID);
		return false;
    });

	// button click to add organisation
	$("#btn-organisation-user-add").click(function () {
		var status = simpris.project.post_organisation_user_add();
		return false;
    });

    // create new organisation via ajax api
    simpris.project.post_organisation_create = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_organisation_form("i");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/organisation/insert/',
    	    data: $("#frmOrganisationAdd").serialize(),
    	    type: 'POST'
    	}).error(function (r) {
			$('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(r){
            if (r.organisation_id == null) {
                window.location.replace("/clientlist");
            }
            else {
                window.location.replace("/organisation/detail/" + r.organisation_id);
            }
    	});
    }

    // edit existing organisation via ajax api
    simpris.project.post_organisation_edit = function () {

		$('#spnError').empty();

		var valid = simpris.project.validate_organisation_form("u");

		if (valid == false) {
			return false;
		}

    	$.ajax({
    	    url: '/api/organisation/update/',
    	    data: $("#frmOrganisationEdit").serialize(),
    	    type: 'POST'
    	}).error(function(r){
            $('#spnError').text("There has been an error: " + r.statusText);
    	})
    	.success(function(response){
            $('#spnError').text("organisation successfully updated");
            window.location.reload(true);
    	});
    };

    // delete existing organisation user via ajax api
    simpris.project.post_organisation_user_delete = function (user_id) {

		$('#div-notification').empty();

		var post_data = $('#form-organisation-user').serializeArray();
		post_data.push({name: 'organisation_user_id', value: user_id});

    	$.ajax({
    	    url: '/api/organisation/deleteuser/',
    	    data: post_data,
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text("This user cannot be deleted from the organisation.");
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
            $('#div-notification').text("organisation successfully updated");
            window.location.reload(true);
    	});
    };

    simpris.project.post_organisation_user_add = function () {

		$('#div-notification').empty();

		var post_data = $('#form-organisation-user').serializeArray();

    	$.ajax({
    	    url: '/api/organisation/adduser/',
    	    data: post_data,
    	    type: 'POST'
    	}).error(function(r){
            $('#div-notification').text(r.statusText);
            $('#div-notification').addClass("alert-danger");
            $("#div-notification").css('display','block');
    	})
    	.success(function(response){
            $('#div-notification').text("Organisation user successfully added");
            window.location.reload(true);
    	});
    };

	simpris.project.validate_organisation_form = function (action) {

		// action is i for insert or u for update

		// if insert the form is frmorganisationAdd else frmorganisationEdit
		var form = null;
		if (action == "i") {
			form = '#frmOrganisationAdd';
		}
		else {
			form = '#frmOrganisationEdit';
		}

		var organisationName = $("#frmOrganisationName", form).val();

		var valid = true;

		if (organisationName == "") {
			$('#spnError').append("Organisation name required. ");
			valid = false;
		}

		return valid;
	}
  });
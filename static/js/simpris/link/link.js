'use strict';

    var _appLinks = new Vue({
        el: '#links',
        delimiters: ['<%', '%>'],
        components: {
        },
        data: {
            linkData: [],
            projectData: [],
            noLinkPanelVisible: true,
            linkPanelVisible: false,
            lnkURLText: true,
            lnkURLEdit: true,
            lnkURLEditText: false
        },
        ready: function () {
        },
        mounted: function () {
        },
        created: function () {
            var self = this;
            this.getLinks(simpris.project.project_id_stored, 2);
        },
        methods: {
            confirmDeleteLink: function (link_id) {
                event.preventDefault();
                var result = confirm("Are you sure you want to delete the link?");
                if (result == true)
                    this.deleteLink(link_id);
                else
                    return false;
            },
            deleteLink: function (link_id) {
                var self = this;
                var post_data = {
                    link_id: link_id,
                    csrfmiddlewaretoken: simpris.csrf_token
                };
                $.ajax({
                    url: '/api/link/delete/' + link_id + '/',
                    type: 'DELETE',
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", simpris.csrf_token);
                    }
                }).done(function (data) {
                    window.location.replace("/project/edit/" + simpris.project.project_id_stored + "/");
                }).fail(function (response) {
                    simpris.common.errorNotify(response.statusText);
                });
            },
            editLink: function (link_id) {
                event.preventDefault();
                var self = this;
                self.lnkURLText = false;
                self.lnkURLEdit = true;
                self.lnkURLEditText = true;
                return false;
            },
            // list project links
            getLinks: function (entity_id, entity_type) {
                var self = this;
                self.lnkURLText = true;
                $.ajax({
                    url: '/api/link/list/' + entity_id + '/' + entity_type + '/',
                    type: 'GET'
                }).done(function (data) {
                    self.linkData = data;
                    if (data.length > 0) {
                        self.linkPanelVisible = true;
                        self.noLinkPanelVisible = false;
                    }
                    else {
                        self.linkPanelVisible = false;
                        self.noLinkPanelVisible = true;
                    }
                }).fail(function (response) {
                    simpris.common.errorNotify(response.statusText);
                });
            },
            updateLink: function (link_id) {
                var self = this;
                var post_data = {
                    link_id: link_id,
                    data: $("#frmLinkEdit").serializeArray(),
                    csrfmiddlewaretoken: simpris.csrf_token
                };
                $.ajax({
                    url: '/api/link/update/' + link_id + '/',
                    type: 'PUT',
                    data: post_data,
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", simpris.csrf_token);
                    }
                }).done(function (data) {
                    simpris.common.successNotify("Link has been updated");
                }).fail(function (response) {
                    simpris.common.errorNotify(response.statusText);
                });
            }
        },
        events: {}
    });

    var _appLinkEdit = new Vue({
        el: '#addLink',
        delimiters: ['<%', '%>'],
        components: {
        },
        data: {
            linkData: [],
            lnkURLText: true,
            lnkURLEdit: false,
            lnkURLEditText: false
        },
        ready: function () {
        },
        mounted: function () {
        },
        created: function () {
        },
        methods: {
            insertLink: function () {
                var self = this;
                var data = $("#frmLinkAdd").serializeArray();
                $.ajax({
                    url: '/api/link/insert/',
                    type: 'POST',
                    data: data
                }).done(function (data) {
                    //simpris.common.successNotify("Link has been inserted");
                    // if (data.link_id == null) {
                    //     window.location.replace("/project/detail/" + simpris.project.project_id_stored + "/");
                    // }
                    // else {
                    window.location.replace("/project/edit/" + simpris.project.project_id_stored + "/");
                    // }
                }).fail(function (response) {
                    simpris.common.errorNotify(response.statusText);
                });
            }
        },
        events: {}
    });
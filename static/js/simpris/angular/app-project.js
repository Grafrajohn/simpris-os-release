'use strict';

var app = angular.module('projectSPA', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}).controller('projectdetail', function ($anchorScroll, $scope, $http, $location) {

    $scope.url_move_task = "/api/task/move/";
    $scope.close_move_panel = true;

    $scope.code = null;
    $scope.response = null;
    $scope.data = null;
    $scope.taskdata = null;
    $scope.status = null;
    $scope.show_row_move_task = null;
    $scope.move_tasklist_id = null;
    $scope.move_task_id = null;
    $scope.task_move_status = null;

    var today = new Date();
    $scope.frmDate = today.getFullYear() + '/' + (today.getMonth() + 1) + '/' + today.getDate();

    $scope.txtProject = "";
    $http.get($scope.urlTasks).
        success(function (data, status) {
            $scope.status = status;
            $scope.taskdata = data;
        });

    $scope.close_move_panel = function () {
        $scope.close_move_panel = true;
    };

    $scope.open_move_panel = function (tasklist_id, task_id, task_name) {
        $scope.show_move_panel = true;
        $scope.move_panel_task_name = task_name;
        $scope.source_tasklist_id = tasklist_id;
        $scope.source_task_id = task_id;
        $location.hash('move_panel');
        $anchorScroll();
    };

    $scope.move_task = function () {
        $http({
            method: "post",
            url: $scope.url_move_task,
            data: {
                taskid: $scope.move_task_id,
                task_list_to: $scope.move_tasklist_id
            }
        }).success(function () {
            $scope.task_move_status = "Move successful";
        }).error(function () {
            $scope.task_move_status = "Move failed";
        });
    };
});
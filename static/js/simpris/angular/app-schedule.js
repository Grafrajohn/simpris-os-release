var app = angular.module('schedule',function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).
config(function($httpProvider) {// provider-injector
	  // This is an example of config block.
	  // You can have as many of these as you want.
	  // You can only inject Providers (not instances)
	  // into config blocks.
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';	
	}).
controller('scheduleController', function($scope, $http, $filter) {

    var indata = null;

    $scope.method = 'GET';
    $scope.urlgrid = $scope.ajaxURL + "/api/time/timegrid";
    $scope.urlTasks = $scope.ajaxURL + "/api/time/timetask";

    $http.get($scope.urlTasks).
      success(function(data, status) {
        $scope.status = status;
        $scope.taskdata = data;
    });
    
    $scope.changeSelection = function(time) {
        $scope.selProjectHide = "true";
        $scope.selTasklistHide = "true";
        $scope.selTaskHide = "true";
    };
});
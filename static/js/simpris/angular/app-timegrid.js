var app = angular.module('simpris', ['ngTable'],function($interpolateProvider) {
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
controller('timegrid', function($scope, $http, $filter, ngTableParams) {

    var indata = null;

    $scope.method = 'GET';
    $scope.urlgrid = $scope.ajaxURL + "/api/time/timegrid";
    $scope.urlTasks = $scope.ajaxURL + "/api/time/timetask";
    $scope.urlInsertTime = $scope.ajaxURL + "/api/time/inserttime/";
    $scope.urlUpdateTime = $scope.ajaxURL + "/api/time/updatetime/";  
    $scope.urlDeleteTime = $scope.ajaxURL + "/api/time/deletetime/";
    //$scope.csrfToken = null;
    
    $scope.code = null;
    $scope.response = null;
    $scope.data = null;
    $scope.taskdata = null;
    $scope.status = null;
    
    var today = new Date;
    $scope.frmDate = today.getFullYear() + '/' + (today.getMonth()+1) + '/' + today.getDate();
    
    $scope.updateStatus = null;
    $scope.clsUpdateStatus = "updateStatus";
    
    $scope.selectedTaskTime = null;    
    $scope.selProjectOption = null;
    $scope.selTaskOption = null;
    
    $scope.selTaskTimeHide = "true";
    $scope.selTaskID = null;
    $scope.seltime = null;

    $scope.starthour = null;
    $scope.startmin = null;
    $scope.hours = null;
    $scope.mins = null;
    
    $scope.butSave = "false";
    $scope.butInsert = "true";
    $scope.butDelete = "false";
    $scope.butClearInsert = "false";
    
    $scope.txtProject = "";
    
    $http.get($scope.urlTasks).
      success(function(data, status) {
        $scope.status = status;
        $scope.taskdata = data;
    });
    
    $scope.tableParams = new ngTableParams({
        page: 1,            // show first page
        count: 25,          // count per page
        filter: {             
            //name: 'M'       // initial filter
        },
        sorting: {
            starthour: 'asc',     // initial sorting
            startmin: 'asc'
        } 
    }, {
        total: 0,//indata.length, // length of data
        getData: function ($defer, params) {
            $http(
                    {url:$scope.urlgrid,
                    method:"GET",
                    params:{indate: $scope.frmDate}}
                 ).
              success(function(data, status) {
                $scope.status = status;
                $scope.data = data;
                indata = data;
                total: indata.length;
                var filteredData = params.filter() ?
                        $filter('filter')(indata, params.filter()) :
                        indata;
                var orderedData = params.sorting() ?
                        $filter('orderBy')(filteredData, params.orderBy()) :
                        indata; 
            
                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            });
        }
    });    
    
    $scope.changeSelection = function(time) {
        $scope.selProjectHide = "true";
        $scope.selTasklistHide = "true";
        $scope.selTaskHide = "true";
        
        $scope.selectedTaskTime = time.project + " : " + time.tasklist + " : " + time.task;
        $scope.starthour = time.starthour;
        $scope.startmin = time.startmin;
        $scope.hours = time.hours;
        $scope.mins = time.mins;
        
        $scope.selTaskTimeHide = "false";
        $scope.seltime = time.id;
        $scope.selTaskID = time.taskid;

        $scope.butDelete = "true";
        $scope.butInsert = "false";
        $scope.butSave = "true";
        $scope.butClearInsert = "true";
    };
    
    $scope.clearSelection = function() {
        $scope.butDelete = "false";
        $scope.butInsert = "true";
        $scope.butSave = "false";
        $scope.butClearInsert = "false";
        
        $scope.selTaskTimeHide = "true";
        $scope.selProjectHide = "false";
        $scope.selTasklistHide = "false";
        $scope.selTaskHide = "false";
    };
    
    $scope.insertTime = function(taskid,frmDate,starthour,startmin,hours,mins) 
    {
        $http({
            method: "post",
            url: $scope.urlInsertTime,
            data: {
                taskid: taskid,
                frmdate: frmDate,
                starthour: starthour,
                startmin: startmin,
                hours: hours,
                mins: mins
            }
        }).success(function(taskid,frmDate,starthour,startmin,hours,mins){
            $scope.updateStatus = "Insert successful";
            $scope.clsUpdateStatus = "";
            var newdata = {};
            newdata['project'] = ''; 
            newdata['tasklist'] = ''; 
            newdata['task'] = taskid;
            newdata['starthour'] = starthour; 
            newdata['startmin'] = startmin; 
            newdata['hours'] = hours; 
            newdata['mins'] = mins; 
            newdata['minsformat'] = mins;             
            $scope.data.push(newdata);
            $scope.tableParams.reload();
        }).error(function(data, status) {
            $scope.updateStatus = "Insert failed";
            $scope.clsUpdateStatus = "updateStatusError";            
        });
    }; 
    
    $scope.updateTime = function(timeid,taskid,frmDate,starthour,startmin,hours,mins) 
    {       
        $http({
            method: "post",
            url: $scope.urlUpdateTime,
            data: {
                timeid: timeid,
                taskid: taskid,
                frmdate: frmDate,
                starthour: starthour,
                startmin: startmin,
                hours: hours,
                mins: mins
            }
        }).success(function(taskid,frmDate,starthour,startmin,hours,mins){
            $scope.updateStatus = "Update successful";
            $scope.starthour = starthour; 
            $scope.startmin = startmin; 
            $scope.hours = hours; 
            $scope.mins = mins;  
            $scope.minsformat = mins;             
            $scope.tableParams.reload();
            $scope.selectedTaskTime = null;
            $scope.butSave = false;
            $scope.butDelete = false;
            $scope.butInsert = true;
            $scope.selTaskHide = false;
        }).error(function(data, status) {
            $scope.updateStatus = "Update failed";
            $scope.clsUpdateStatus = "updateStatusError";
        });
    }; 
    
    $scope.deleteTime = function(timeid) 
    {
        $http({
            method: "post",
            url: $scope.urlDeleteTime,
            data: {
                timeid: timeid
            }
        }).success(function(taskid,frmDate,starthour,startmin,hours,mins){
            $scope.updateStatus = "Delete successful";
        }).error(function(data, status) {
            $scope.updateStatus = "Delete failed";
        });
    };
    
    $scope.selectDate = function(frmDate) 
    {
        $scope.tableParams.reload();
    }; 
});
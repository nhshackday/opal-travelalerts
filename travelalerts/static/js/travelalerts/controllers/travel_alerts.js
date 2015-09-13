//
// Controller for travel alerts
//
angular.module('opal.controllers').controller(
    'TravelAlertsCtrl', function(
        $scope, $rootScope, $modalInstance, $window, $http,
        destination)
    {
        $scope.destination = destination;
        $scope.alerts = [];
        
        $http.get('http://localhost:5000/api/'+destination).then(
            function(resp){
                $scope.alerts = resp.data;
            })
        
        $scope.cancel = function(){
            $modalInstance.close(null);
        };
        
    }
);

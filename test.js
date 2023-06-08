angular.module('app', [])
    .controller('RedirectController', ['$scope', '$window', function($scope, $window) {
        $scope.redirect = function(userInput) {
            $window.location.href = '/home' + userInput;
        }
    }]);

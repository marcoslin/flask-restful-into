(function () {

    var app = angular.module('webapp', []);

    app.controller('mainController', ['$scope', '$http', '$log', function($scope, $http, $log) {
        $http.get('/d/collegio/').then(function (result) {
            $scope.collegios = result.data;
        });

        $scope.showDeputatos = function () {
            var collegio = $scope.collegio.id;
            $http.get('/d/deputato/' + collegio + '/').then(function (result) {
                $scope.deputatos = result.data.results.bindings;
            });
        };
    }]);

})();
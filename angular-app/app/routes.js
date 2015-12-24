(function(angular) {
  'use strict';

  angular
    .module('app')
    .config(routes);

  routes.$inject = ['$routeProvider', '$locationProvider'];

  function routes($routeProvider, $locationProvider) {

    $routeProvider
      .when('/main', {
        templateUrl: '/ng/templates/home.html',
        controller: 'Main',
        controllerAs: 'main',
      })
      .otherwise({
        redirectTo: '/main',
      });

    $locationProvider.html5Mode(false);
  }

})(window.angular);

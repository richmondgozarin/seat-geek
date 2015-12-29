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
        controller: 'TicketCtrl',
        controllerAs: 'ticket',
      })

      .when('/deals', {
        templateUrl: '/ng/templates/deals.html',
        controller: 'Deals',
        controllerAs: 'deals',
      })

      .when('/checkout', {
        templateUrl: '/ng/templates/checkout.html',
        controller: 'Checkout',
        controllerAs: 'checkout',
      })

      .when('/signup', {
        templateUrl: '/ng/templates/signup.html',
        controller: 'Signup',
        controllerAs: 'signup',
      })

      .otherwise({
        redirectTo: '/main',
      });

    $locationProvider.html5Mode(false);
  }

})(window.angular);

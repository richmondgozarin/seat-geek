(function(angular) {
  'use strict';

  angular
    .module('app')
    .config(routes);

  routes.$inject = ['$routeProvider', '$locationProvider'];

  function routes($routeProvider, $locationProvider) {

    $routeProvider
      .when('/home', {
        templateUrl: '/ng/templates/admin-home.html',
        controller: 'EventCtrl',
        controllerAs: 'event',
      })

      .when('/deals/:event_key', {
        templateUrl: '/ng/templates/deals.html',
        controller: 'DealsCtrl',
        controllerAs: 'deals',
      })

      .when('/checkout/:ticket_key', {
        templateUrl: '/ng/templates/checkout.html',
        controller: 'TicketCtrl',
        controllerAs: 'ticket',
      })

      .when('/signup', {
        templateUrl: '/ng/templates/signup.html',
        controller: 'AccountCtrl',
        controllerAs: 'acct',
      })

      .when('/seller', {
        templateUrl: '/ng/templates/admin-seller.html',
        controller: 'SellerCtrl',
        controllerAs: 'seller',
      })

      .when('/login', {
        templateUrl: '/ng/templates/login.html',
        controller: 'AccountCtrl',
        controllerAs: 'acct',
      })

      .otherwise({
        redirectTo: '/home',
      });

    $locationProvider.html5Mode(false);
  }

})(window.angular);

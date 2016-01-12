(function(angular) {
    'use strict';

    angular
    .module('app.services')
    .service('TicketRest', ticketRest);

    ticketRest.$inject = [
      '$http'
    ];

    function ticketRest($http) {

    var base_url = '/api/tickets';

    this.list = function() {
      return $http.get(base_url);
    };

    this.get = function(tckt_key) {
      return $http.get(base_url + '/:' + tckt_key + '/list');
    };

    this.get_details = function(tckt_key) {
      return $http.get(base_url + '/:' + tckt_key + '/details');
    };

    this.create = function(params) {
      return $http.post(base_url, params);
    };

    this.update = function(a_key, params) {
      return $http.put(base_url + '/:' + a_key, params);
    };

  }

})(window.angular);

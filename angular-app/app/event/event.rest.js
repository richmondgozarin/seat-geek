(function(angular) {
    'use strict';

    angular
    .module('app.services')
    .service('EventRest', eventRest);

    eventRest.$inject = [
      '$http'
    ];

    function eventRest($http) {

    var base_url = '/api/events';

    this.list = function() {
      return $http.get(base_url);
    };

    this.get = function(a_key) {
      return $http.get(base_url + '/get_tickets' + '/:' + a_key);
    };

    this.create = function(params) {
      return $http.post(base_url, params);
    };

    this.update = function(a_key, params) {
      return $http.put(base_url + '/:' + a_key, params);
    };

  }

})(window.angular);

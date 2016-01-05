(function(angular) {
    'use strict';

    angular
    .module('app.services')
    .service('DealRest', dealRest);

    dealRest.$inject = [
      '$http'
    ];

    function dealRest($http) {

    var base_url = '/api/tickets';

    this.list = function() {
      return $http.get(base_url);
    };

    this.get = function(e_key) {
      return $http.get(base_url + '/:' + e_key + '/deals' );
    };

    this.get_details = function(e_key) {
      return $http.get(base_url + '/:' + e_key + '/details' );
    };

    this.create = function(params) {
      return $http.post(base_url, params);
    };

    this.update = function(a_key, params) {
      return $http.put(base_url + '/:' + a_key, params);
    };

  }

})(window.angular);

(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('DealsCtrl', dealsCtrl);

  dealsCtrl.$inject = [
    'DealsModel',
    '$scope',
    '$routeParams'
  ];

  function dealsCtrl(DealsModel, $scope, routeParams) {
    var deals = this;
    deals.model = DealsModel;

    function activate(){
      DealsModel.dealListing(routeParams.event_key);
    }

    activate();

  }
})(window.angular);

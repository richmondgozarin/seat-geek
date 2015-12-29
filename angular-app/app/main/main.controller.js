(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('TicketCtrl', ticketCtrl);

  ticketCtrl.$inject = [
    'TicketModel',
    '$scope'
  ];

  function ticketCtrl(TicketModel, $scope) {
    var main = this;

    main.data = TicketModel;

    function activate(){
      TicketModel.ticketListing();
    }

    activate();

  }
})(window.angular);

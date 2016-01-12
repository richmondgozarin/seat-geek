(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('TicketCtrl', ticketCtrl);

  ticketCtrl.$inject = [
    'TicketModel',
    '$scope',
    '$routeParams'
  ];

  function ticketCtrl(TicketModel, $scope, routeParams) {
    var ticket = this;

    ticket.model = TicketModel;

    function activate(){
      TicketModel.ticketListing();
      if (routeParams.ticket_key){
        TicketModel.details(routeParams.ticket_key);
      }
    }

    activate();

  }
})(window.angular);

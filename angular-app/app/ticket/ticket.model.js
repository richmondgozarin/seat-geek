(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('TicketModel', ticketModel);

    ticketModel.$inject = [
        'TicketRest',
        'loading',
        '$routeParams',
        /*'passive_messenger'*/
    ];

    function ticketModel(TicketRest, loading, routeParams){
        this.loading = loading.new();
        this.ticketListing = tickets;
        this.info = details;
        this.buy = buy;

        function tickets(){
          var self = this;
          self.loading.watch(TicketRest.list())
          .success(function(d){
            console.log(d);
            self.ticketData = d;
          })
        }

        function details(ticket_key){
            var self = this;
            self.loading.watch(TicketRest.get_details(ticket_key))
            .success(function(d){
              console.log(d.tickets[0]);
              self.details = d.tickets[0];
              self.total = self.details.price * self.details.quantity * commission;
            })
        }

        function buy(ticket_key){
          var self = this;
          self.loading.watch(TicketRest.buy(routeParams.ticket_key))
          .success(function(d){
            /*passive_messenger.success('Redirecting to Paypal shortly...')*/
            console.log('BUY:: ' + d);
            window.location = d;
          })
        }
    }

})(window.angular);

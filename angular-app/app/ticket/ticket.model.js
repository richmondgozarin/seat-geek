(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('TicketModel', ticketModel);

    ticketModel.$inject = [
        'TicketRest',
        'loading'
    ];

    function ticketModel(TicketRest, loading){
        this.loading = loading.new();
        this.ticketListing = tickets;
        this.info = details;

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
            self.total = self.details.price * self.details.quantity * 1.10;
          })
        }
    }

})(window.angular);

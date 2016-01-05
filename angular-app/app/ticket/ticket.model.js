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
        this.ticketListing = events;


        function events(){
          var self = this;
          self.loading.watch(TicketRest.list())
          .success(function(d){
            console.log(d);
            self.ticketData = d;
          })
        }
    }

})(window.angular);

(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('TicketModel', mainModel);

    mainModel.$inject = [
        'TicketRest',
        'loading'
    ];

    function mainModel(TicketRest, loading){
        this.loading = loading.new();
        this.ticketListing = tickets;


        function tickets(){
          var self = this;
          self.loading.watch(TicketRest.list())
          .success(function(d){
            console.log(d);
            self.ticketData = d;
          })
        }
    }

})(window.angular);

(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('SellerModel', sellerModel);

    sellerModel.$inject = [
        'SellerRest',
        'EventRest',
        'loading',
        '$q'
    ];

    function sellerModel(SellerRest, EventRest, loading, $q){

        function Seller(data) {
            this._dbSaved = null;
            this.isLoading = loading.new();
        }

        Seller.loading = loading.new();
        Seller.listing = listing;
        Seller.submit = submit;
        Seller.event_key = null;
        Seller.ticket_image = null;
        Seller.section = null;
        Seller.quantity = null;
        Seller.price = null;

        function listing(key){
          var self = this;
          var call1 = SellerRest.get_tickets(key)
                    .success(function(d){
                      console.log(d);
                      self.lists = d.tickets || [];
                    });
          var call2 = EventRest.list()
                      .success(function(d){
                        console.log(d.events);
                        self.events = d.events || [];
                      })
                      .error(function(d){
                        self.events = 'No events for today.';
                      });

          self.loading
            .watch($q.all([call1,call2]));
        }

        function submit(){
          var self = this;
            if (Seller.section == ''){
              alert('Section is required.');
            } else {
              var params = {
                'event': Seller.event_key,
                'scalper_name': active_user.key,
                'ticket_img': Seller.ticket_image,
                'section': Seller.section,
                'quantity': Seller.quantity,
                'price': Seller.price
              }

              var call1 = SellerRest.create(params)
              .success(function(d){
                console.log(d);
                alert('New Ticket Created.');
                Seller.event_key = null;
                Seller.ticket_image = null;
                Seller.section = null;
                Seller.quantity = null;
                Seller.price = null;
                Seller.listing(active_user.key);
                /*window.location = "/#/seller";*/
              });

              self.loading
                .watch($q.all([call1]));
            }
        }

        return Seller;
    }

})(window.angular);

(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('SellerModel', sellerModel);

    sellerModel.$inject = [
        'SellerRest',
        'loading'
    ];

    function sellerModel(SellerRest, loading){

        function Seller(data) {
            this._dbSaved = null;
            this.isLoading = loading.new();
        }

        Seller.loading = loading.new();
        Seller.listing = listing;
        Seller.search = search;
        Seller.keyword = null;

        function listing(){
          var self = this;
          self.loading.watch(SellerRest.list())
          .success(function(d){
            console.log(d);
            self.lists = d.Sellers;
          })
        }

        function search(){
          var self = this;
          self.loading.watch(SellerRest.search(Seller.keyword))
          .success(function(d){
            console.log(d);
            self.found = d.Sellers || [];
          })
          .error(function(d){
            self.found = 'Keyword not found.';
          });
        }

        return Seller
    }

})(window.angular);

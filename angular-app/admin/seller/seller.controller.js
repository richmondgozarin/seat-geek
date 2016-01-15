(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('SellerCtrl', sellerCtrl);

  sellerCtrl.$inject = [
    'SellerModel',
  ];

  function sellerCtrl(Seller) {
    var seller = this;

    seller.model = Seller;
    function activate(){
      Seller.listing(active_user.key);
    }

    $('select').on('contentChanged', function() {
      // re-initialize (update)
      $(this).material_select();
    });
    activate();

  }
})(window.angular);

(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('SellerCtrl', sellerCtrl);

  sellerCtrl.$inject = [
    'SellerModel',
    '$scope'
  ];

  function sellerCtrl(Seller, $scope) {
    var seller = this;

    seller.model = Seller;
    function activate(){
      Seller.listing();
    }

    activate();

  }
})(window.angular);

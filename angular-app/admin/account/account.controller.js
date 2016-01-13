(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('AccountCtrl', accountCtrl);

  accountCtrl.$inject = [
    'AccountModel',
    '$routeParams'
  ];

  function accountCtrl(Account, routeParams) {
    var account = this;
    account.model = Account;
  }
})(window.angular);

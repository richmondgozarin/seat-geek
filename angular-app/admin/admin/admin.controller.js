(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('AdminCtrl', adminCtrl);

  adminCtrl.$inject = [
    'AdminModel',
    '$routeParams'
  ];

  function adminCtrl(Admin, routeParams) {
    var admin = this;
    admin.model = Admin;
  }
})(window.angular);

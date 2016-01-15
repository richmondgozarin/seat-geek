(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('AccountModel', accountModel);

    accountModel.$inject = [
        'AccountRest',
        'loading',
        '$q'
    ];

    function accountModel(AccountRest, loading, $q){

      function Account(data) {
        this._dbSaved = null;
        this.isLoading = loading.new();
      }

      Account.loading = loading.new();
      Account.create = create;
      Account.email = null;
      Account.first_name = null;
      Account.last_name = null;
      Account.password = null;
      Account.conf_password = null;


      function create(){
        var self = this;
        if (Account.password != Account.conf_password){
          alert('Password and Confirm Password does not match.');
        } else {
          var params = {
            'email': Account.email,
            'first_name': Account.first_name,
            'last_name': Account.last_name,
            'password': Account.password
          }

          var call1 = AccountRest.create(params)
          .success(function(d){
            console.log(d);
            alert('Registration Completed.');
            window.location = "/#/seller";
          });

          self.loading
            .watch($q.all([call1]));
        }

      }

      return Account
    }

})(window.angular);

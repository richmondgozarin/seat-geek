(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('AdminModel', adminModel);

    adminModel.$inject = [
        'AdminRest',
        'loading',
        '$q'
    ];

    function adminModel(AdminRest, loading, $q){

      function Admin(data) {
        this._dbSaved = null;
        this.isLoading = loading.new();
      }

      Admin.loading = loading.new();
      Admin.create = create;
      Admin.email = null;
      Admin.first_name = null;
      Admin.last_name = null;
      Admin.password = null;
      Admin.conf_password = null;


      function create(){
        var self = this;
        alert(Admin.email);
        if (Admin.password != Admin.conf_password){
          alert('Password and Confirm Password does not match.');
        } else {
          var params = {
            'email': Admin.email,
            'first_name': Admin.first_name,
            'last_name': Admin.last_name,
            'password': Admin.password
          }

          var call1 = AdminRest.create(params)
          .success(function(d){
            console.log(d);
            alert('Registration Completed.');
            window.location = "/#/seller";
          });

          self.loading
            .watch($q.all([call1]));
        }

      }

      return Admin
    }

})(window.angular);

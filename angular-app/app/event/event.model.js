(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('EventModel', eventModel);

    eventModel.$inject = [
        'EventRest',
        'loading'
    ];

    function eventModel(EventRest, loading){
        this.loading = loading.new();
        this.eventListing = events;


        function events(){
          var self = this;
          self.loading.watch(EventRest.list())
          .success(function(d){
            console.log(d);
            self.eventData = d;
          })
        }
    }

})(window.angular);

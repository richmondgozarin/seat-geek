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

        function Event(data) {
            this._dbSaved = null;
            this.isLoading = loading.new();
        }

        Event.loading = loading.new();
        Event.listing = listing;
        Event.search = search;
        Event.logout_url = logout_url;
        Event.greeter = greeter;
        Event.keyword = null;

        function listing(){
          var self = this;
          self.loading.watch(EventRest.list())
          .success(function(d){
            console.log(d);
            self.lists = d.events;
          })
        }

        function search(){
          var self = this;
          self.loading.watch(EventRest.search(Event.keyword))
          .success(function(d){
            console.log(d);
            self.found = d.events || [];
          })
          .error(function(d){
            self.found = 'Keyword not found.';
          });
        }

        return Event
    }

})(window.angular);

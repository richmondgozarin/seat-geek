(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('EventCtrl', eventCtrl);

  eventCtrl.$inject = [
    'EventModel',
    '$scope'
  ];

  function eventCtrl(EventModel, $scope) {
    var main = this;

    main.data = EventModel;

    function activate(){
      EventModel.eventListing();
    }

    activate();

  }
})(window.angular);

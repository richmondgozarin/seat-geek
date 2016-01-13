(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('EventCtrl', eventCtrl);

  eventCtrl.$inject = [
    'EventModel',
    '$scope'
  ];

  function eventCtrl(Event, $scope) {
    var main = this;

    main.model = Event;
    function activate(){
      Event.listing();
    }

    activate();

  }
})(window.angular);

(function(angular) {
  'use strict';

  angular
    .module('app')
    .directive("date", date);

  date.$inject = ['$compile'];

  function date($compile){
    return {
      scope: true,
      restrict: 'A',
      link: function (scope, elm, attrs) {
          $compile(elm.contents())(scope);
          var $elm = $(elm);
          var schedule = attrs.schedDate;

          $elm.html(moment(schedule).format("YYYY-MM-DD"));
      }
    };
  }

})(window.angular);

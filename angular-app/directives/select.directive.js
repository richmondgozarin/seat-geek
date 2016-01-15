(function(angular) {
  'use strict';

  angular
    .module('app')
    .directive("select", select);

  select.$inject = ['$document','$compile'];

  function select($document, $compile){
    return {
      restrict: 'EA',
      link: function (scope, elm, attrs) {
          $('select').material_select();
      }
    };
  }

})(window.angular);

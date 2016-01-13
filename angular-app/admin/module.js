(function(angular) {
  'use strict';

  angular
    .module('cs.utilities', [
      'cs.pubsub',
      'cs.passive-messenger',
      'cs.loading',
      'cs.modal',
    ]);

  angular
    .module('app.services', [
      'cs.utilities',
    ]);

  angular
    .module('app.controllers', [
      'app.services',
    ]);

  angular
    .module('app.directives', [
      'cs.utilities',
    ]);

  angular
    .module('app.filters', [
    ]);

  angular
    .module('app', [
      'app.services',
      'app.directives',
      'app.controllers',
      'ngRoute',
      'ngSanitize',
      'ui.select',
      'ui.materialize'
    ])
    .run(app);

  app.$inject = ['$log', 'passive_messenger', '$timeout', '$rootScope'];

  function app($log, passive_messenger, $timeout, $rootScope) {
    $log.info('Angular App Loaded');
    $timeout(function() { passive_messenger.success('Loaded'); });
    $rootScope.ngLoadingFinished = true;
  }
})(window.angular);

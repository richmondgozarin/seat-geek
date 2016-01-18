(function(angular){
    'use strict';

    angular
        .module('app.services')
        .service('SellerModel', sellerModel);

    sellerModel.$inject = [
        'SellerRest',
        'EventRest',
        'loading',
        'FileUploader',
        '$q'
    ];

    function sellerModel(SellerRest, EventRest, loading, FileUploader, $q){

        function Seller(data) {
            this._dbSaved = null;
            this.isLoading = loading.new();
        }

        Seller.loading = loading.new();
        Seller.fileUpload = new FileUploader();
        Seller.listing = listing;
        Seller.submit = submit;
        Seller.uploader = uploader;
        Seller.event_key = null;
        Seller.ticket_image = null;
        Seller.section = null;
        Seller.quantity = null;
        Seller.price = null;

        function listing(key){
          var self = this;
          var call1 = SellerRest.get_tickets(key)
                    .success(function(d){
                      console.log(d);
                      self.lists = d.tickets || [];
                    });
          var call2 = EventRest.list()
                      .success(function(d){
                        console.log(d.events);
                        self.events = d.events || [];
                      })
                      .error(function(d){
                        self.events = 'No events for today.';
                      });

          self.loading
            .watch($q.all([call1,call2]));
        }

        function submit(){
          var self = this;
            if (Seller.section == ''){
              alert('Section is required.');
            } else {
              var params = {
                'event': Seller.event_key,
                'scalper_name': active_user.key,
                'ticket_img': Seller.ticket_image,
                'section': Seller.section,
                'quantity': Seller.quantity,
                'price': Seller.price
              }

              var call1 = SellerRest.create(params)
              .success(function(d){
                console.log(d);
                alert('New Ticket Created.');
                Seller.event_key = null;
                Seller.ticket_image = null;
                Seller.section = null;
                Seller.quantity = null;
                Seller.price = null;
                Seller.listing(active_user.key);
                /*window.location = "/#/seller";*/
              });

              self.loading
                .watch($q.all([call1]));
            }
        }

        function uploader(){
          var self = this;
          self.seller_rest = SellerREST;
          self.fileUpload = new FileUploader();

          self.fileUpload.filters.push({
              name: 'customFilter',
              fn: function(item /*{File|FileLikeObject}*/, options) {
                  return this.queue.length < 10;
              }
          });

          self.fileUpload.onWhenAddingFileFailed = function(item /*{File|FileLikeObject}*/, filter, options) {
              console.warn('onWhenAddingFileFailed', item, filter, options);
          };
          self.fileUpload.onAfterAddingFile = function(fileItem) {
            console.info('onAfterAddingFile', fileItem);
            var importfile = fileItem;
            self.seller_rest.upload_url()
            .success(function(data, status, headers, config){
                importfile.url = data.upload_url;
                // importfile.upload();
                console.log('success', importfile);

            }).error(function(data, status, headers, config){
                console.log('fail');
            });
          };

          self.fileUpload.onAfterAddingAll = function(addedFileItems) {
              console.info('onAfterAddingAll', addedFileItems);
          };

          self.fileUpload.onBeforeUploadItem = function(item) {
              console.info('onBeforeUploadItem', item);
              var params = {
                'event': Seller.event_key,
                'scalper_name': active_user.key,
                'ticket_img': Seller.ticket_image,
                'section': Seller.section,
                'quantity': Seller.quantity,
                'price': Seller.price
              }
              item.formData.push(params);
          };
          self.fileUpload.onProgressItem = function(fileItem, progress) {
              console.info('onProgressItem', fileItem, progress);
          };
          self.fileUpload.onProgressAll = function(progress) {
              console.info('onProgressAll', progress);
          };
          self.fileUpload.onSuccessItem = function(fileItem, response, status, headers) {
              console.info('onSuccessItem', fileItem, response, status, headers);
          };
          self.fileUpload.onErrorItem = function(fileItem, response, status, headers) {
              console.info('onErrorItem', fileItem, response, status, headers);
          };
          self.fileUpload.onCancelItem = function(fileItem, response, status, headers) {
              console.info('onCancelItem', fileItem, response, status, headers);
          };
          self.fileUpload.onCompleteItem = function(fileItem, response, status, headers) {
              console.info('onCompleteItem', fileItem, response, status, headers);
          };
          self.fileUpload.onCompleteAll = function() {
              console.info('onCompleteAll');
              /*passive_messenger.success("upload successful");*/
          };
        }

        return Seller;
    }

})(window.angular);

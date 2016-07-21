'use strict';

require.config({
	shim: {
        'storage':{
            deps:['jquery'],
            exports: 'storage',
        },
    },
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/underscore/underscore',
        //swig: '../swig/swig',
        storage: '../bower_components/jquery-storage-api/jquery.storageapi',
    }
});

require([
    'backbone',
], function (Backbone) {
    console.log('comenzo');
    Backbone.history.start({
        pushState:true,
    });
    $(function(){
        $.ajaxSetup({
            crossDomain: true,
            beforeSend: function(xhr, settings) {
                var csrfSafeMethod = function(method) { 
                    // these HTTP methods do not require CSRF protection
                    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                };
                if (!csrfSafeMethod(settings.type)) {
                    var csrftoken = $.cookie('csrftoken');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    });
});
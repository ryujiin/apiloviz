
'use strict';

require.config({
    shim: {
        'owl':{
            deps:['jquery'],
            exports: 'owlCarousel'
        },
        swig: {
            exports: 'Swig'
        },
        handlebars: {
            exports: 'handlebars'
        },
        'zoom':{
            deps:['jquery'],
            exports: 'zoom',
        },
        'storage':{
            deps:['jquery'],
            exports: 'storage',
        },
        'coockie':{
            deps:['jquery'],
            exports: 'coockie',
        },
        'bootstrap':{
            deps:['jquery'],
        },
        'facetr':{
            deps:['backbone'],
        }
    },
    paths: {

        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/underscore/underscore',
        bootstrap: '../bower_components/bootstrap/dist/js/bootstrap',
        handlebars: '../bower_components/handlebars/handlebars',        
        swig: 'vendor/swig/swig',
        owl: 'vendor/owl/owl.carousel',
        zoom: 'vendor/bower_components/jquery-zoom/jquery.zoom',
        storage: 'vendor/bower_components/jQuery-Storage-API/jquery.storageapi',
        coockie: 'vendor/coockie/jquery.cookie',
        facetr:'vendor/facetas/backbone.facetr'
    }
});

require([
    'backbone',
    '../js/backbone/routers/rutas',
    '../js/backbone/views/app',
    '../js/backbone/collections/categoria',
    '../js/backbone/collections/catalogo/productos',
], function (Backbone,Rutas,App,Categorias,Productos) {
    var app = new App(Rutas);

    /* Views */
    Productos.fetch().done(function () {
        Categorias.fetch().done(function () {
            Backbone.history.start({
                pushState:true,
            });
        })    
    })

    function fixDiv() {
        if ($(window).scrollTop()> 34) {
            $('#header').addClass('fijo');
        }else{
            $('#header').removeClass('fijo');
        };

    }
    $(window).scroll(fixDiv);
    fixDiv();

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
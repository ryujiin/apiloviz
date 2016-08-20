/*global define*/

define([
    'jquery',
    'backbone',
    '../views/carro/page_carro',
    '../views/pages/pages',
    '../views/catalogo/page_catalogo',
    '../views/productosingle/page_producto',
    '../collections/categoria',
    '../views/procesar/page_procesar',
    '../views/usuario/page_user',
    '../views/app/page_error',
], function ($, Backbone,CarroPage,Pages,CatalogoPage,ProductoSingle,Categorias,PageProcesar,PageUser,PageError) {
    'use strict';

    var AppRouter = Backbone.Router.extend({
        routes: {
            "":"root",
            "usuario/perfil/":"perfil",
            "producto/:slug/":'productoSingle',
            'carro/':'carro_page',
            'catalogo/:categoria/':'catalogo',
            'ingresar/':'ingresar',
            'procesar-compra/':'procesar_compra',
            'felicidades/':'felicidades',
            'sp/:page_slug/':'pagina_statica',
            '*notFound': 'notFound',
        },

        initialize:function(){
            //this.bind('all', this.trackPageview);
        },
        root:function(){
            $('body').removeClass();            
            Pages.buscar_page('front');
            var url = Backbone.history.getFragment();
        },
        perfil:function(){
            if ($.localStorage.get('pagina_procesar')===true) {
                $.localStorage.remove('pagina_procesar');
                this.navigate('procesar-compra/',{trigger: true});
            };
            $('body').removeClass();            
            PageUser.verificar_login();
            var url = Backbone.history.getFragment();
        },
        productoSingle:function (slug) {
            $('body').removeClass();   

            ProductoSingle.cambiar_producto(slug);

            console.log(slug)            
        },
        carro_page:function(){
            $('body').removeClass();            

            console.log('carro');
            CarroPage.render();
            var url = Backbone.history.getFragment();
        },
        catalogo:function (slug) {
            $('body').removeClass();            
            $('body').addClass('catalogo');
            var coincidencia = Categorias.findWhere({slug:slug});

            if (coincidencia) {
                CatalogoPage.render(coincidencia,Categorias);
                var url = Backbone.history.getFragment();
            }else{
                this.notFound();
            }           
        },
        ingresar:function () {            
            $('body').removeClass();            
            PageUser.render();
            var url = Backbone.history.getFragment();
        },
        procesar_compra:function () {
            $('body').removeClass();              
            PageProcesar.verificar_render();            
        },
        pagina_statica:function (page_slug) {
            Pages.buscar_page(page_slug);
            var url = Backbone.history.getFragment();
        },
        felicidades:function () {
            var url = Backbone.history.getFragment();
        },
        trackPageview:function () {
            var url = Backbone.history.getFragment();
        },
        notFound:function () {
            $('body').removeClass();           

            PageError.render();
        },
    });

    var rutas = new AppRouter();

    return rutas;
});

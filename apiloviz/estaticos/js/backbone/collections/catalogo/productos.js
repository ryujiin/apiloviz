/*global define*/

define([
    'underscore',
    'backbone',
    '../../models/catalogo/producto'
], function (_, Backbone, ProductosModel) {
    'use strict';

    var ProductosCollection = Backbone.Collection.extend({
    	url: '/api/producto/lista/',

        model: ProductosModel,
    });

    var productoslista = new ProductosCollection();

    return productoslista;
});

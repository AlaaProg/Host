
odoo.define("om_hospital.WebClient", function(require){
    var abstractWebClient = require('web.AbstractWebClient')

    abstractWebClient.include({

        start: function(parent){
            this.set("title_part", {'zopenerp': "Hospital"})

            this._super(parent)
        }
    })
})
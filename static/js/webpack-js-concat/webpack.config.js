var $ = require("jquery");

module.exports = {
    entry: {
        main: [
            // '../jquery/jquery-ui.min.js',
            '../jqueryui/jquery-ui.min.js',
            '../bootstrap/bootstrap.min.js',
            '../jquery-components/jquery.nanoscroller.min.js',
            '../jqueryui/jquery.ui.touch-punch.min.js',
            '../simpris/common/common.js',
            '../jquery-components/scripts.js',
            '../pace.min.js'
        ],
        datatables: [
            //'../jquery-components/datatables/jquery.dataTables.min.js',
            '../jquery-components/ZeroClipboard.js',
            '../jquery-components/jquery.nanoscroller.min.js',
            '../jquery-components/datatables/dataTables.buttons.min.js',
            '../jquery-components/datatables/buttons.flash.min.js',
            '../jquery-components/datatables/buttons.html5.min.js',
            '../jquery-components/datatables/buttons.print.min.js',
            '../jquery-components/datatables/buttons.colVis.min.js'
        ]
    },
    output: {
        path: './dist',
        filename: 'output_[name].js'
    },
    //resolve: {
    //    alias: {
    //        //'jquery': '../jquery/jquery-1.12.0.min.js',
    //        'datatables.net': '../jquery-components/datatables/jquery.dataTables.min.js'
    //    }
    //}
}
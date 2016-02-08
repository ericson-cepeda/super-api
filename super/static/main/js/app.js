/*
    App configuration
*/
require.config({
    urlArgs: "bust=" + (new Date()).getTime()
});

define([], function(){

    //configuration
    var app = {
        id:         "admin-demo",
        name:       "Admin",
        version:    "0.1",
        debug:      true,
        start:      "/app/results"
    };

    return app;
});

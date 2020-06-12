function launch(file) {
    fetch("http://127.0.0.1:5000/launch", {

        method: 'POST',

        body: file
    }).then(function(response) {
        return response.text();
    }).then(function(text) {

        console.log('POST response: ');

        console.log(text);
    });
}

function kill(file) {
    fetch("http://127.0.0.1:5000/kill", {

        method: 'POST',

        body: file
    }).then(function(response) {
        return response.text();
    }).then(function(text) {

        console.log('POST response: ');

        console.log(text);
    });
}

function quit() {
    fetch("http://127.0.0.1:5000/quit", {

        method: 'POST',

        body: ""
    }).then(function(response) {
        return response.text();
    }).then(function(text) {

        console.log('POST response: ');

        console.log(text);
    });
}

function create(name, orgname, orgid, bundleid) {
    fetch("http://127.0.0.1:5000/info", {

        method: 'POST',

        body: name + "," + orgname + "," + orgid + "," + bundleid
    }).then(function(response) {
        return response.text();
    }).then(function(text) {

        console.log('POST response: ');

        console.log(text);
    });
}

window.onkeypress = function(e) {
    if (event.ctrlKey && event.key == "w") {
        quit()
    }
}
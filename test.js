var express = require('express');
var child_process = require('child_process');
var app = express();

app.get('/unsafe', function(req, res){
  var userProvidedPath = req.query.path;
  
  child_process.exec('ls ' + userProvidedPath, function (error, stdout, stderr) {
    res.send(stdout);
  });
});

app.listen(3000);


// ruleid:dom-based-xss
document.write("<OPTION value=1>"+document.location.href.substring(document.location.href.indexOf("default=")+8)+"</OPTION>");

// ok:dom-based-xss
document.write("<OPTION value=2>English</OPTION>");

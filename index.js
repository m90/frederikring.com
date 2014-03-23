var express = require('express');
var app = express();

var fs = require('fs');

var lessMiddleware = require('less-middleware');

app.set('views', __dirname + '/views');
app.set('view engine', 'jade');

app.use(express.compress());

app.use(lessMiddleware(__dirname + '/static', {
	compress: true
	, once: (process.env.APP_MODE === 'uberspace')
}));

app.use(express.static(__dirname + '/static'));

var port = process.env.APP_MODE === 'uberspace' ? process.env.PORT : 1337;

app.get('/:foo?', function(req, res){
	res.render('index');
});

app.listen(port);
console.log('app up and running @port: ' + port);
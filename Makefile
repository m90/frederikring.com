docs/CNAME:
	echo "www.frederikring.com" > ./docs/CNAME

docs/index.html: index.jade
	./node_modules/.bin/jade index.jade --out ./docs

all: docs/CNAME docs/index.html
all: build build/CNAME build/index.html

build:
	mkdir -p build

build/CNAME:
	echo "www.frederikring.com" > ./build/CNAME

build/index.html: index.jade
	./node_modules/.bin/jade index.jade --out ./build

.PHONY: build/*
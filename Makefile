build: docs/index.html docs/CNAME

docs/index.html:
	./node_modules/.bin/jade ./index.jade --out ./docs

docs/CNAME:
	echo "www.frederikring.com" > ./docs/CNAME

.PHONY: docs/index.html

docs/CNAME:
	echo "www.frederikring.com" > ./docs/CNAME

docs/%.html: %.jade
	./node_modules/.bin/jade ./$^ --out ./docs

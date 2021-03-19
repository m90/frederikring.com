.PHONY: build
build: index CNAME tachyons
	@mkdir -p build

.PHONY: CNAME
CNAME:
	@echo "www.frederikring.com" > ./build/CNAME

index: index.jade
	@$$(npm bin)/jade index.jade --out ./build

tachyons: ./public/tachyons.min.css
	@cp ./public/tachyons.min.css ./build

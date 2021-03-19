.PHONY: build
build: index CNAME public
	@mkdir -p build

.PHONY: CNAME
CNAME:
	@echo "www.frederikring.com" > ./build/CNAME

.PHONY: index
index:
	@$$(npm bin)/jade index.jade --out ./build

.PHONY: public
public:
	@cp -R ./public ./build

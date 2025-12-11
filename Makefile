.PHONY: build local-run

build:
	docker build -t sampleapp:local .

local-run:
	docker run -p 8080:8080 sampleapp:local

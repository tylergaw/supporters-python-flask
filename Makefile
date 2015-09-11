.PHONY: clean release test setup run

SHELL := /bin/bash

VERSION := $(shell python setup.py --version)
CURR_HASH := $(shell echo "$$(git rev-list --pretty=%h --max-count=1 HEAD | grep -v ^commit)")

setup:
	python setup.py develop

run:
	python supporter_signup/application.py

test:
	@python setup.py test

release:
	git tag -a v$(VERSION) -m "Release version: v$(VERSION)"
	git push origin v$(VERSION)

clean:
	rm -rf dist/
	rm -rf build/

.PHONY: build run

IMAGE_NAME=airlines
CONTAINER_NAME=airlines-django-container
PORT=8000

build:
	docker build -t airlines .

run:
	docker run -it --rm -p 8000:8000 --name airlines-django-container airlines

stop:
	docker stop airlines-django-container

### Создание образа
	docker image build ./ -t task
### Создание контейнера
	docker run --name=hw_cont -p 8002:80 task

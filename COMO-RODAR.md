--- Ja criei o RABBITMQ e subtitui a URL.

OBS: as vezes da um bug de nao publicar evento, parar todos docker, iniciar o admin primeiro depois o main.
-- Sempre startar primeiro o admin.

Pasta ADMIN:
cd admin

1 - docker compose up  -d.
2- RODAR MIGRATIONS: PARA ISSO =>
	docker compose exec backend sh
	- por algum motivo na minha maquina deu problema na porta 8000 entrao troquei tudo para 8002
	python manage.py migrate


PASTA MAIN:
cd main

1 - docker compose up  -d.
2- RODAR MIGRATIONS: PARA ISSO =>
	docker compose exec backend sh
	FLASK_APP=main.py flask db upgrade

PASTA REACT:
se necessario => nvm use 16

1 - npm intall.
2- npm run start.
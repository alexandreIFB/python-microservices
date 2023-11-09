1- Criar o CLOUD RABITMQ, pegar url de conecxao e substituir no codigo no lugar do your_rabbitmq_url.

2- Substituir os requirements 

Flask-SQLAlchemy==2.5.1
SQLAlchemy==1.3.20
Flask-Migrate==3.0.1
Flask-Script==2.0.6
Flask-Cors==3.0.9
requests==2.25.0
mysqlclient==2.0.1
pika==1.1.0
Flask==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1


Pasta ADMIN:

1 - Rodar banco de dados OK. docker compose up db -d.

2 - Rodar o backend. docker compose up backend


PASTA MAIN:

1- remover pasta dbdata e migrations
2- DOCKER COMPOSE UP
3- Atualizar a lib das migrations colocando o codigo no main.py
3- RODAR MIGRATIONS: PARA ISSO =>
	docker compose exec backend sh
	FLASK_APP=main.py flask db init
	FLASK_APP=main.py flask db migrate -m "Initial migration."
	FLASK_APP=main.py flask db upgrade


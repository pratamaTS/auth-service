init:
	npx sequelize-cli init

migration:
	npx sequelize-cli migration:generate --name

migrate:
	npx sequelize db:migrate

seed:
	npx sequelize-cli db:seed:all
	

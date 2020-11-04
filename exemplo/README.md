# Exemplo de ecommerce utilizando dataloaders no Graphene

Este projeto é parte da palestra "Utilizando Dataloaders para melhorar o desempenho das suas queries no GraphQL", apresentada na [Python Brasil 2020](https://2020.pythonbrasil.org.br).

## Instalando o projeto exemplo

- Configurar um ambiente virtual

```sh
sudo apt install python3-venv
python3 -m venv venv
```

- Ativar o ambiente

```sh
source venv/bin/activate
```

- Instalar dependências

```sh
pip install -r requirements.txt
```

- Rodar migrations

```sh
python manage.py migrate
```

- Carregar dados de exemplo

```sh
python manage.py loaddata produtos
```

## Rodando

```sh
python manage.py runserver
```

## Testando

- acessar [interface graphiql](localhost:8000/graphql) para rodar as queries

    - você pode visualizar as queries disponíveis navegando pela aba "Docs" na interface GraphiQL. Mas se preferir, pode visualizá-las no arquivo [queries.gql](./queries.gql)

- acessar [interface do silk](localhost:8000/silk) para verificar o que foi rodado no backend a cada requisição

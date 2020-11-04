from collections import defaultdict

from promise import Promise
from promise.dataloader import DataLoader

from .models import Categoria, Produto


class ProdutosPorCategoriaDataloader(DataLoader):
    def batch_load_fn(self, ids_categorias):
        produtos_por_categoria = defaultdict(list)

        # organiza os produtos por categoria em um dicionário
        for produto in Produto.objects.filter(categoria_id__in=ids_categorias).iterator():
            produtos_por_categoria[produto.categoria_id].append(produto)

        # coloca os produtos por categoria em uma lista na mesma ordem em que os resolvers de
        # cada categoria foram executados
        resultado = [
            produtos_por_categoria.get(categoria_id, [])
            for categoria_id in ids_categorias
        ]

        # retorna o resultado em uma Promise
        return Promise.resolve(resultado)


class CategoriasDataloader(DataLoader):
    def batch_load_fn(self, ids_categorias):
        categoria_por_produto = defaultdict(Categoria)

        # organiza as categorias em um dicionário com a chave sendo o id de uma categoria e o valor um objeto Categoria
        for categoria in Categoria.objects.filter(id__in=ids_categorias).iterator():
            categoria_por_produto[categoria.id] = categoria

        # coloca as categorias em uma lista na mesma ordem em que os resolvers foram executados
        result = [
            categoria_por_produto.get(categoria_id, None)
            for categoria_id in ids_categorias
        ]

        return Promise.resolve(result)


class Dataloader:
    def load(key):
        """
        adiciona a chave em uma lista para executar
        a consulta posteriormente e retorna uma Promise
        """
        ...

    def batch_load_fn(key):
        """
        Recebe as chaves, faz a consulta uma vez só e retorna um resolver para a Promise
        """
        ...

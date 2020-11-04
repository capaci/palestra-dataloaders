import graphene

from .models import Categoria, Produto


class TipoProduto(graphene.ObjectType):
    id = graphene.ID()
    nome = graphene.String()
    descricao = graphene.String()
    categoria = graphene.Field('ecommerce.produto.schema.TipoCategoria')

    def resolve_categoria(produto, info):
        return Categoria.objects.get(pk=produto.categoria_id)


class TipoCategoria(graphene.ObjectType):
    id = graphene.ID()
    nome = graphene.String()
    produtos = graphene.List(TipoProduto)

    def resolve_produtos(categoria, info):
        return Produto.objects.filter(categoria_id=categoria.id)


class QueriesProduto(graphene.ObjectType):
    produtos = graphene.List(TipoProduto)
    categorias = graphene.List(TipoCategoria)

    def resolve_produtos(root, info):
        return Produto.objects.all()

    def resolve_categorias(root, info):
        return Categoria.objects.all()

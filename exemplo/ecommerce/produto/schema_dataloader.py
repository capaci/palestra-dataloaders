import graphene
from .models import Categoria, Produto


class TipoProdutoDataloader(graphene.ObjectType):
    id = graphene.ID()
    nome = graphene.String()
    descricao = graphene.String()
    categoria = graphene.Field('ecommerce.produto.schema_dataloader.TipoCategoriaDataloader')

    def resolve_categoria(parent, info):
        return info.context.categorias_dataloader.load(parent.categoria_id)


class TipoCategoriaDataloader(graphene.ObjectType):
    id = graphene.ID()
    nome = graphene.String()
    produtos = graphene.List(TipoProdutoDataloader)

    def resolve_produtos(parent, info):
        return info.context.produtos_por_categoria_dataloader.load(parent.id)


class QueriesProdutoDataloader(graphene.ObjectType):
    produtos_com_dataloader = graphene.List(TipoProdutoDataloader)
    categorias_com_dataloader = graphene.List(TipoCategoriaDataloader)

    def resolve_produtos_com_dataloader(root, info):
        return Produto.objects.all()

    def resolve_categorias_com_dataloader(root, info):
        return Categoria.objects.all()

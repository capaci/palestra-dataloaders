import graphene
from graphene_django import DjangoObjectType
from .models import Categoria, Produto


class TipoProdutoSelectRelated(DjangoObjectType):
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'categoria',
        ]


class TipoCategoriaPrefetchRelated(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome',
            'descricao',
            'produtos',
        ]


class QueriesProdutoSelectPrefetchRelated(graphene.ObjectType):
    produtos_com_select_related = graphene.List(TipoProdutoSelectRelated)
    categorias_com_prefetch_related = graphene.List(TipoCategoriaPrefetchRelated)

    def resolve_produtos_com_select_related(root, info):
        return Produto.objects.select_related('categoria').all()

    def resolve_categorias_com_prefetch_related(root, info):
        return Categoria.objects.prefetch_related('produtos').all()

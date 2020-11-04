import graphene
from graphene_django.debug import DjangoDebug

from ecommerce.produto.schema import QueriesProduto
from ecommerce.produto.schema_dataloader import QueriesProdutoDataloader
from ecommerce.produto.schema_select_prefetch_related import QueriesProdutoSelectPrefetchRelated


class Query(QueriesProduto,
            QueriesProdutoDataloader,
            QueriesProdutoSelectPrefetchRelated,
            graphene.ObjectType,
            ):
    debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query)

import json

from django.utils.functional import cached_property
from graphene_django.views import GraphQLView
from silk.profiling.profiler import silk_profile

from ecommerce.produto.dataloaders import (CategoriasDataloader,
                                           ProdutosPorCategoriaDataloader)


class GQLContext:
    """
    Contexto personalizado para incluir os dataloaders no contexto da requisição
    """
    def __init__(self, request):
        self.request = request

    @cached_property
    def produtos_por_categoria_dataloader(self):
        return ProdutosPorCategoriaDataloader()

    @cached_property
    def categorias_dataloader(self):
        return CategoriasDataloader()


class CustomGraphQLView(GraphQLView):
    """
    View personalizada para poder incluir o contexto e utilizar o silk para fazer profiling das requisições
    """
    def get_context(self, request):
        return GQLContext(request)

    def dispatch(self, request, *args, **kwargs):
        if not request.body:
            return super().dispatch(request, *args, **kwargs)

        body = json.loads(request.body)
        operation_name = body.get('operationName', 'Request sem nome')

        # fazer o profile da aplicação, pra ver tudo que foi executado na requisição
        with silk_profile(name=operation_name):
            response = super().dispatch(request, *args, **kwargs)

        return response

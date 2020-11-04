from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from .views import CustomGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(CustomGraphQLView.as_view(graphiql=True))),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

from django.db import models
from django.utils.translation import gettext_lazy as _


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        app_label = 'produto'
        db_table = 'categoria'
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    class Meta:
        app_label = 'produto'
        db_table = 'produto'
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return self.nome

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass


class ArticleScopeInlineFormset(BaseInlineFormSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count_main = 0

    def clean(self):

        for form in self.forms:
            if form.cleaned_data['is_main']:
                self.count_main += 1
                if self.count_main > 1:
                    raise ValidationError('is_main выбран более 1 раза')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

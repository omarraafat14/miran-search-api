from django.contrib import admin

from . import models
from ..services.admin import BaseModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import StackedInline
from unfold.contrib.filters.admin import (
    AutocompleteSelectFilter,
    AutocompleteSelectMultipleFilter,
    BooleanRadioFilter,
)


class NutritionFactsInline(StackedInline):
    model = models.NutritionFacts
    can_delete = False
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(BaseModelAdmin, TabbedTranslationAdmin):
    search_fields = ["name"]


@admin.register(models.Brand)
class BrandAdmin(BaseModelAdmin, TabbedTranslationAdmin):
    search_fields = ["name"]


@admin.register(models.Product)
class ProductAdmin(BaseModelAdmin, TabbedTranslationAdmin):
    list_display = ["name", "brand", "category", "price", "is_active"]
    list_filter = [
        ("brand", AutocompleteSelectFilter),
        ("category", AutocompleteSelectMultipleFilter),
        ("is_active", BooleanRadioFilter),
    ]
    list_filter_submit = True
    list_filter_sheet = False
    search_fields = ["name", "sku"]
    search_help_text = "Search by name or sku"
    inlines = [NutritionFactsInline]

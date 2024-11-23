from modeltranslation.translator import TranslationOptions, register
from fastfood import models


@register(models.FoodMeny)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')

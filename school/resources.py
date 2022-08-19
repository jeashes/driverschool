from import_export import resources
from school.models import Area, Alphabet, Category


class AreaResource(resources.ModelResource):
    class Meta:
        model = Area


class AlphabetResource(resources.ModelResource):
    class Meta:
        model = Alphabet


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

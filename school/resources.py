from import_export import resources
from school.models import Area, Alphabet


class AreaResource(resources.ModelResource):
    class Meta:
        model = Area


class AlphabetResource(resources.ModelResource):
    class Meta:
        model = Alphabet

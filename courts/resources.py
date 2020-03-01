from import_export import resources
from .models import Court

class CourtResource(resources.ModelResource):
    class Meta:
        model = Court
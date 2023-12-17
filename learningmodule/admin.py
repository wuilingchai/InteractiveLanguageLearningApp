from django.contrib import admin
from .models import Vocabulary, Pharmacy, Airport, Direction, Restaurant, Teatime, Transportation
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Create resource classes
class VocabularyResource(resources.ModelResource):
    class Meta:
        model = Vocabulary

class PharmacyResource(resources.ModelResource):
    class Meta:
        model = Pharmacy

class AirportResource(resources.ModelResource):
    class Meta:
        model = Airport

class DirectionResource(resources.ModelResource):
    class Meta:
        model = Direction

class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant

class TeatimeResource(resources.ModelResource):
    class Meta:
        model = Teatime

class TransportationResource(resources.ModelResource):
    class Meta:
        model = Transportation

# Register your models using ImportExportModelAdmin
@admin.register(Vocabulary)
class VocabularyAdmin(ImportExportModelAdmin):
    resource_class = VocabularyResource

@admin.register(Pharmacy)
class PharmacyAdmin(ImportExportModelAdmin):
    resource_class = PharmacyResource

@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    resource_class = AirportResource

@admin.register(Direction)
class DirectionAdmin(ImportExportModelAdmin):
    resource_class = DirectionResource

@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    resource_class = RestaurantResource

@admin.register(Teatime)
class TeatimeAdmin(ImportExportModelAdmin):
    resource_class = TeatimeResource

@admin.register(Transportation)
class TransportationAdmin(ImportExportModelAdmin):
    resource_class = TransportationResource

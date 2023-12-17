from django.contrib import admin
from .models import Word, Choices
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Create resource classes
class WordResource(resources.ModelResource):
    class Meta:
        model = Word

class ChoicesResource(resources.ModelResource):
    class Meta:
        model = Choices

# Register your models using ImportExportModelAdmin
@admin.register(Word)
class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource

@admin.register(Choices)
class ChoicesAdmin(ImportExportModelAdmin):
    resource_class = ChoicesResource

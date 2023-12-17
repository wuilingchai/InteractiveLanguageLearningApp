from django.contrib import admin
from .models import TranslationHistory
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Create resource class
class TranslationHistoryResource(resources.ModelResource):
    class Meta:
        model = TranslationHistory

# Register your model using ImportExportModelAdmin
@admin.register(TranslationHistory)
class TranslationHistoryAdmin(ImportExportModelAdmin):
    resource_class = TranslationHistoryResource

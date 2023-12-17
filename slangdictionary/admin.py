from django.contrib import admin
from .models import Slang
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Create resource class
class SlangResource(resources.ModelResource):
    class Meta:
        model = Slang

# Register your model using ImportExportModelAdmin
@admin.register(Slang)
class SlangAdmin(ImportExportModelAdmin):
    resource_class = SlangResource

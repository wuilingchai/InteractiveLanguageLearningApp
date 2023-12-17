from django.contrib import admin
from .models import User, LearningData
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
# from slangdictionary.models import Slang
# from learningmodule.models import Vocabulary

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class LearningDataResource(resources.ModelResource):
    class Meta:
        model = LearningData

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
class LearningDataAdmin(ImportExportModelAdmin):
    resource_class = LearningDataResource

admin.site.register(User, UserAdmin)
admin.site.register(LearningData, LearningDataAdmin)

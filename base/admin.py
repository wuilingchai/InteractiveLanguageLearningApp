from django.contrib import admin
from .models import User, LearningData, DialogData

# Register your models here.
# from slangdictionary.models import Slang
# from learningmodule.models import Vocabulary

admin.site.register(User)
admin.site.register(LearningData)
admin.site.register(DialogData)
# admin.site.register(Vocabulary)

from django.contrib import admin
from .models import Vocabulary, Pharmacy, Airport, Direction, Restaurant, Teatime, Transportation

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Pharmacy)
admin.site.register(Airport)
admin.site.register(Direction)
admin.site.register(Restaurant)
admin.site.register(Teatime)
admin.site.register(Transportation)
from django.contrib import admin
from graph.models import GraphPost

class GraghPostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','body','timestamp']

admin.site.register(GraphPost,GraghPostAdmin)
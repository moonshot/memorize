from django.contrib import admin
from .models import Passage, Phrase

class PhraseInline(admin.TabularInline):
    model = Phrase
    extra = 10

class PassageAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [PhraseInline]
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Passage, PassageAdmin)

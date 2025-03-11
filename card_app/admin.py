from django.contrib import admin
from .models import Card, CardHead, PageDetails

class CardInline(admin.TabularInline):
    model = Card
    extra = 1
    fields = ('title', 'description', 'image', 'button_text', 'button_url', 'published')

class CardHeadInline(admin.TabularInline):
    model = CardHead
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

@admin.register(CardHead)
class CardHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')    
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [CardInline]

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'head', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('head', 'created_at', 'updated_at', 'published')    
    search_fields = ('title', 'description')
    autocomplete_fields = ['head']

@admin.register(PageDetails)
class PageDetailsAdmin(admin.ModelAdmin):
    list_display = ('slugs', 'title', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('created_at', 'updated_at', 'published')
    search_fields = ('slugs',)
    inlines = [CardHeadInline]
    prepopulated_fields = {'slugs': ('title',)}
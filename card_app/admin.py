from django.contrib import admin
from .models import cardSectionItems, cardSection, pageDetails, bannerSection

class cardInline(admin.TabularInline):
    model = cardSectionItems
    extra = 1
    fields = ('title', 'description', 'image', 'button_text', 'button_url', 'published')

class cardHeadInline(admin.TabularInline):
    model = cardSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

@admin.register(cardSection)
class cardSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')    
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [cardInline]

@admin.register(cardSectionItems)
class cardSectionItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'head', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('head', 'created_at', 'updated_at', 'published')    
    search_fields = ('title', 'description')
    autocomplete_fields = ['head']

@admin.register(pageDetails)
class PageDetailsAdmin(admin.ModelAdmin):
    list_display = ('slugs', 'title', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('created_at', 'updated_at', 'published')
    search_fields = ('slugs',)
    inlines = [cardHeadInline]
    prepopulated_fields = {'slugs': ('title',)}

@admin.register(bannerSection)
class BannerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']

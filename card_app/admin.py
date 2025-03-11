from django.contrib import admin
from .models import CardSectionItems, CardSection, PageDetails, BannerSection, FaqSection, FaqSectionItems, QuickLinkSection, QuickLinkSectionItems, ContentSection, ContentSectionItems
class CardInline(admin.TabularInline):
    model = CardSectionItems
    extra = 1
    fields = ('title', 'description', 'image', 'button_text', 'button_url', 'published')

class CardHeadInline(admin.TabularInline):
    model = CardSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

class BannerSectionInline(admin.TabularInline):
    model = BannerSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

class FaqSectionInline(admin.TabularInline):
    model = FaqSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

class FaqSectionItemsInline(admin.TabularInline):
    model = FaqSectionItems
    extra = 1
    fields = ('question', 'answer', 'published')

class QuickLinksInline(admin.TabularInline):
    model = QuickLinkSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

class QuickLinkSectionItemsInline(admin.TabularInline):
    model = QuickLinkSectionItems
    extra = 1
    fields = ('btn1_text', 'btn1_url', 'btn2_text', 'btn2_url', 'btn3_text', 'btn3_url', 'published')

class ContentSectionInline(admin.TabularInline):
    model = ContentSection
    extra = 1
    fields = ('title', 'description', 'published')
    show_change_link = True

class ContentSectionItemsInline(admin.TabularInline):
    model = ContentSectionItems
    extra = 1
    fields = ('title', 'description', 'published')

@admin.register(CardSection)
class CardSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')    
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [CardInline]

@admin.register(CardSectionItems)
class CardSectionItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'section', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('section', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['section']

@admin.register(PageDetails)
class PageDetailsAdmin(admin.ModelAdmin):
    list_display = ('slugs', 'title', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('created_at', 'updated_at', 'published')
    search_fields = ('slugs',)
    inlines = [CardHeadInline, BannerSectionInline, QuickLinksInline, FaqSectionInline, ContentSectionInline]
    prepopulated_fields = {'slugs': ('title',)}

@admin.register(BannerSection)
class BannerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']

@admin.register(FaqSection)
class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published')
    list_editable = ['published']
    list_filter = ('page', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [FaqSectionItemsInline]

@admin.register(FaqSectionItems)
class FaqQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'section', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('section', 'created_at', 'updated_at', 'published')
    search_fields = ('question', 'answer')
    autocomplete_fields = ['section']

@admin.register(QuickLinkSection)
class QuickLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [QuickLinkSectionItemsInline]

@admin.register(QuickLinkSectionItems)
class QuickLinkSectionItemsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'section', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('section', 'created_at', 'updated_at', 'published')
    autocomplete_fields = ['section']

@admin.register(ContentSection)
class ContentSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('page', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['page']
    inlines = [ContentSectionItemsInline]

@admin.register(ContentSectionItems)
class ContentSectionItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'published', 'created_at', 'updated_at')
    list_editable = ['published']
    list_filter = ('section', 'created_at', 'updated_at', 'published')
    search_fields = ('title', 'description')
    autocomplete_fields = ['section']
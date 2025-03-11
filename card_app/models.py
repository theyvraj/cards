from django.db import models
from .mixins import UnpublishRelatedItemsMixin

class PageDetails(models.Model, UnpublishRelatedItemsMixin):
    slugs = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    published = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    feature_image = models.ImageField(upload_to='page_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    related_fields = ['cardSection', 'faqSection', 'bannerSection', 'quickLinkSection', 'contentSection']

    def __str__(self):
        return self.title or self.slugs
    
    class Meta:
        verbose_name = "Page Detail"
        verbose_name_plural = "Page Details"
        ordering = ['-created_at']

class BannerSection(models.Model):
    page = models.ForeignKey(PageDetails, on_delete=models.SET_NULL, related_name='bannerSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    feature_image = models.ImageField(upload_to='banner_images/', blank=True, null=True)
    feature_image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    btn1_text = models.CharField(max_length=50, default='placeholder')
    btn1_url = models.URLField(blank=True)
    btn2_text = models.CharField(max_length=50, default='placeholder')
    btn2_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Banner Section {self.id}"
    
    class Meta:
        verbose_name = "Banner Section"
        verbose_name_plural = "Banner Sections"
        ordering = ['-created_at']    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class CardSection(models.Model, UnpublishRelatedItemsMixin):
    page = models.ForeignKey(PageDetails, on_delete=models.SET_NULL, related_name='cardSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    related_fields = ['cardSectionItems']
    
    def __str__(self):
        return self.title or f"Card Section {self.id}"
    
    class Meta:
        verbose_name = "Card Section"
        verbose_name_plural = "Card Sections"
        ordering = ['-created_at']

class CardSectionItems(models.Model):
    section = models.ForeignKey(CardSection, on_delete=models.SET_NULL, null=True, related_name='cardSectionItems')
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Learn More')
    button_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title or f"Card Section Items {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "All Cards"
        ordering = ['-created_at']

class FaqSection(models.Model, UnpublishRelatedItemsMixin):
    page = models.ForeignKey(PageDetails, on_delete=models.SET_NULL, related_name='faqSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    related_fields = ['faqSectionItems']
    def __str__(self):
        return self.title or f"FAQ Section {self.id}"
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "All Page FAQs"
        ordering = ['-created_at']

class FaqSectionItems(models.Model):
    section = models.ForeignKey(FaqSection, on_delete=models.SET_NULL, null=True, related_name='faqSectionItems')
    question = models.CharField(max_length=200)
    answer = models.TextField()
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question or f"FAQ Questions {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "FAQ Question"
        verbose_name_plural = "All FAQ Questions"
        ordering = ['-created_at']

class QuickLinkSection(models.Model, UnpublishRelatedItemsMixin):
    page = models.ForeignKey(PageDetails, on_delete=models.SET_NULL, related_name='quickLinkSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    related_fields = ['quickLinkSectionItems']
    def __str__(self):
        return self.title or f"Quick Links {self.id}"
    
    class Meta:
        verbose_name = "Quick Link"
        verbose_name_plural = "Quick Links"
        ordering = ['-created_at']

class QuickLinkSectionItems(models.Model):
    section = models.ForeignKey(QuickLinkSection, on_delete=models.SET_NULL, null=True, related_name='quickLinkSectionItems')
    btn1_text = models.CharField(max_length=50, default='placeholder')
    btn1_url = models.URLField(blank=True)
    btn2_text = models.CharField(max_length=50, default='placeholder')
    btn2_url = models.URLField(blank=True)
    btn3_text = models.CharField(max_length=50, default='placeholder')
    btn3_url = models.URLField(blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        buttons = []
        if self.btn1_text and self.btn1_text != 'placeholder':
            buttons.append(self.btn1_text)
        if self.btn2_text and self.btn2_text != 'placeholder':
            buttons.append(self.btn2_text)
        if self.btn3_text and self.btn3_text != 'placeholder':
            buttons.append(self.btn3_text)
        
        if buttons:
            return " | ".join(buttons)
        return f"Quick Link Item {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Quick Link Item"
        verbose_name_plural = "All Quick Link Items"
        ordering = ['-created_at']

class ContentSection(models.Model, UnpublishRelatedItemsMixin):
    page = models.ForeignKey(PageDetails, on_delete=models.SET_NULL, related_name='contentSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    related_fields = ['contentSectionItems']

    def __str__(self):
        return self.title or f"Content Section {self.id}"
    
    class Meta:
        verbose_name = "Content Section"
        verbose_name_plural = "Content Sections"
        ordering = ['-created_at']

class ContentSectionItems(models.Model):
    section = models.ForeignKey(ContentSection, on_delete=models.SET_NULL, null=True, related_name='contentSectionItems')
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Content Section Item {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Content Section Item"
        verbose_name_plural = "All Content Section Items"
        ordering = ['-created_at']
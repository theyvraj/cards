from django.db import models
class pageDetails(models.Model):
    slugs = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    published = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    feature_image = models.ImageField(upload_to='page_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or self.slugs
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.published:
            self.cardSection.update(published=False)
    
    class Meta:
        verbose_name = "Page Detail"
        verbose_name_plural = "Page Details"
        ordering = ['-created_at']

class bannerSection(models.Model):
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

class cardSection(models.Model):
    page = models.ForeignKey(pageDetails, on_delete=models.SET_NULL, related_name='cardSection', null=True, blank=True)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title or f"Card Section {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.published:
            self.cardItems.update(published=False)
    
    class Meta:
        verbose_name = "Card Section"
        verbose_name_plural = "Card Sections"
        ordering = ['-created_at']

class cardSectionItems(models.Model):
    head = models.ForeignKey(cardSection, on_delete=models.SET_NULL, related_name='cardItems')
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Learn More')
    button_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title or f"Banner Section {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "All Cards"
        ordering = ['-created_at']


from django.db import models
class PageDetails(models.Model):
    slugs = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    feature_image = models.ImageField(upload_to='page_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title or self.slugs
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.published:
            self.card_heads.update(published=False)
    
    class Meta:
        verbose_name = "Page Detail"
        verbose_name_plural = "Page Details"

class CardHead(models.Model):
    page = models.ForeignKey(PageDetails, on_delete=models.CASCADE, related_name='card_heads', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title or f"Card Section {self.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.published:
            self.cards.update(published=False)
    
    class Meta:
        verbose_name = "Card Section"
        verbose_name_plural = "Card Sections"

class Card(models.Model):
    head = models.ForeignKey(CardHead, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Learn More')
    button_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        head_title = self.head.title if self.head else "No Section"
        return f"{self.title} ({head_title})"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "All Cards"


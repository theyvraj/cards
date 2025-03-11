class UnpublishRelatedItemsMixin:
    related_fields = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.published:
            for field in self.related_fields:
                related_manager = getattr(self, field, None)
                if related_manager:
                    related_manager.update(published=False)
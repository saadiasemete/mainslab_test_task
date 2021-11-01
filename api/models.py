from django.db import models
from datetime import datetime as dtm, timedelta as tmd

class SentMessageDataQuerySet(models.QuerySet):
    def last_24_hours(self):
        oldest = dtm.now()-tmd(days=1)
        return self.filter(created_at__gte = oldest)

class SentMessageDataManager(models.Manager):
    def get_queryset(self):
        return SentMessageDataQuerySet(self.model, using=self._db)

    def last_24_hours(self):
        return self.get_queryset().last_24_hours()

class SentMessageData(models.Model):
    id = models.UUIDField(primary_key=True)
    subject = models.CharField(max_length=256)
    to_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = SentMessageDataManager
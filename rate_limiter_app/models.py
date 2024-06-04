from django.db import models
# Create your models here.
import uuid


class AbstractTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Merchant(AbstractTimeStamp):
    name = models.CharField(max_length=100)
    ip_address = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rate_limit = models.IntegerField()
    burst_limit = models.IntegerField()

class RateLimit(AbstractTimeStamp):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    limit_per_minute = models.IntegerField()
    burst_limit = models.IntegerField()
    last_checked = models.DateTimeField(auto_now=True)
    tokens = models.FloatField(default=0)
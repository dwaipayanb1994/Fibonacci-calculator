from django.db import models

# Create your models here.

class Cashback(models.Model):
    app_id = models.PositiveIntegerField(primary_key = True)
    weight = models.FloatField()
    multiplier = models.FloatField()
    spends = models.PositiveIntegerField()
    available_cashback = models.PositiveIntegerField()
    def __str__(self):
        return str(self.app_id) + " Weight " + str(self.weight) + " Spends: " + str(self.spends) + " av_cb " + str(self.available_cashback)

p=Cashback(app_id=1, weight=0.33, multiplier=1, spends=0, available_cashback=0)
p.save()
p=Cashback(app_id=2, weight=0.33, multiplier=1, spends=0, available_cashback=0)
p.save()
p=Cashback(app_id=3, weight=0.34, multiplier=1, spends=0, available_cashback=0)
p.save()

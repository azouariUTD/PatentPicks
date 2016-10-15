from django.db import models
from django.contrib.auth.models import User

from PP_Core.models import InventionDetail


class Account(models.Model):
    user = models.ForeignKey(User)
    royalty_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    improvement_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    funding_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.user.email





# Create your models here.

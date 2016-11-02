from django.db import models
from django.contrib.auth.models import User
from PP_Core.models import InventionDetail


class Profile(models.Model):
    user = models.ForeignKey(User)
    royalty_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    improvement_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    funding_income = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    invention_funded = models.IntegerField()
    inventions_saved = models.IntegerField()
    inventions_hidden = models.IntegerField()
    inventions_viewed = models.IntegerField()
    inventions_not_viewed = models.IntegerField()
    pledges_to_fund = models.IntegerField()
    number_of_picks = models.IntegerField()
    picks_in_production = models.IntegerField()

    def __str__(self):
        return  "" + self.user.username






# Create your models here.

from django.db import models
from datetime import datetime

class Photography(models.Model):
    class CategoryChoices(models.IntegerChoices):
        n_a = 0, 'N/A'
        nebula = 1, 'Nebula'
        star = 2, 'Star'
        galaxy = 3, 'Galaxy'
        planet = 4, 'Planet'

    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    category = models.PositiveSmallIntegerField(choices=CategoryChoices.choices, default=CategoryChoices.n_a)
    photo = models.ImageField(null=False, blank=True)
    date = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True)

    @classmethod
    def get_category_choices(cls):
        return [choice[1] if choice[1] != 'N/A' else 'NA' for choice in cls.CategoryChoices.choices]
    
    @classmethod
    def get_category_id(cls, category_display):
        if category_display == 'NA':
            category_display = 'N/A'
        for choice in cls.CategoryChoices.choices:
            if category_display == choice[1]:
                return choice[0]

    def __str__(self):
        return self.name

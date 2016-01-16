from django.db import models
from django_date_extensions import fields as dde


class ExampleModel(models.Model):
    first_month = dde.ApproximateDateField()
    second_month = dde.ApproximateDateField()
    third_month = dde.ApproximateDateField()

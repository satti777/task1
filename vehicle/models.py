from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class VehicleData(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    model = models.IntegerField(default=0000)
    registration_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

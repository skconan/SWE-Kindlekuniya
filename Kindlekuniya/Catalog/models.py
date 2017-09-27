from django.db import models

class Product(models.Model):
    isbn = models.DecimalField(max_digits = 13, decimal_places = 0, unique = True)
    name = models.CharField(max_length = 250)
    author = models.CharField(max_length = 250)
    publisher = models.CharField(max_length = 250)
    price = models.FloatField()
    weight = models.FloatField()
    isMonocrome = models.BooleanField(default = True)
    paperType = models.CharField(max_length = 100)
    coverType = models.CharField(max_length = 100)
    size_height = models.FloatField()
    size_width = models.FloatField()
    size_thickness = models.FloatField()
    description = models.TextField()
    pictureUrl = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CatagoryMap(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.catagory) + " - " + str(self.product)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique = True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.product) + " - " + str(self.quantity)

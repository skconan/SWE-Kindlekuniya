from django.db import models

class Product(models.Model):
    isbn = DecimalField(unique = True, max_digits = 13, decimal_places = 0)
    name = CharField(max_length = 250)
    author = CharField(max_length = 250)
    publisher = CharField(max_length = 250)
    price = FloatField()
    weight = FloatField()
    isMonocrome = BooleanField(default = True)
    paperType = CharField(max_length = 100)
    coverType = CharField(max_length = 100)
    size_height = FloatField()
    size_width = FloatField()
    size_thickness = FloatField()
    description = TextField()
    pictureUrl = CharField(max_length = 500)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = CharField(max_length = 100)
    description = TextField()

    def __str__(self):
        return self.name

class CatagoryMap(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.catagory) + " - " + str(self.product)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique = True)
    quantity = PositiveIntegerField()

    def __str__(self):
        return str(self.product) + " - " + str(self.quantity)

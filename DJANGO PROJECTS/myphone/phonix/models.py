from django.db import models

# Create your models here.
class product(models.Model):
    productname=models.CharField(max_length=30)

    def __str__(self):
        return self.productname

class productdetails(models.Model):
    product=models.ForeignKey(product,null=True,on_delete=models.CASCADE)
    productprice=models.FloatField()
    productimage=models.ImageField(upload_to='media',blank=True)
    productmodel=models.CharField(max_length=30)
    productRAM=models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.product},{self.productprice},{self.productimage},{ self.productmodel},{self.productRAM}')


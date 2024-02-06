from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=255)
    info=models.TextField(blank=True)
    price=models.IntegerField()
    categories=models.ManyToManyField("Category",related_name="products")
    image=models.ImageField(upload_to='images/',default='images/default.png')

    def __str__(self):
        return self.title


class Category(models.Model):
    title=models.CharField(max_length=150)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural="Categories"   


class Order(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
            


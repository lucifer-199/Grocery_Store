from django.db import models

# Create your models here.
class Product(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_quantity= models.CharField(max_length=100)
    item_status= models.CharField(max_length=300)
    pub_date = models.DateField()
    is_saved= models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
    
class SavedItems(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_quantity= models.CharField(max_length=100)
    item_status= models.CharField(max_length=300)
    pub_date = models.DateField()

    def __str__(self):
        return self.item_name
    
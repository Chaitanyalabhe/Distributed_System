from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.id}"
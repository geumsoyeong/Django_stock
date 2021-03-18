from django.db import models

# Create your models here.
class MyTopicStock(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_rank = models.TextField()
    title = models.TextField()
    price = models.IntegerField()
    low = models.TextField()
    volume = models.IntegerField()
    payment = models.IntegerField()
    buy = models.IntegerField()
    sell = models.IntegerField()
    capitalization = models.TextField()
    per = models.TextField()
    roe = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_topic_stock'



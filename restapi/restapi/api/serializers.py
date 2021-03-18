from restapi.api.models import MyTopicStock
from rest_framework import serializers

class MyTopicStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicStock
        fields = ['id','stock_rank','title','price','low','volume','payment','buy','sell','capitalization','per','roe','created_at'] #####

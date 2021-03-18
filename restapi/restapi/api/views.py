from rest_framework import viewsets
from rest_framework import permissions
from restapi.api.models import MyTopicStock
from restapi.api.serializers import MyTopicStockSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class MyTopicStockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicStock.objects.all()
    serializer_class = MyTopicStockSerializer

    permission_classes = [permissions.IsAuthenticated]

    # /my_topic_users/search?q=???  #강사님 토픽 이름 기준임
    @action(detail=False, methods=['GET'])
    def search(self, requset):
        q= requset.query_params.get('q', None)

        qs = self.get_queryset().filter(title=q)
        serializer = self.get_serializer(qs, many=True)
        
        #print(requset.query_params.get('q', None))

        return Response(serializer.data)

    # price 현재가 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def price_highlist(self, requset):
        highlist = MyTopicStock.objects.all().order_by('-price')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    # volume 거래량 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def volume_highlist(self, requset):
        highlist = MyTopicStock.objects.all().order_by('-volume')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    # payment 거래대금 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def payment_highlist(self, requset):
        highlist = MyTopicStock.objects.all().order_by('-payment')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    # buy 매수호가 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def buy_highlist(self, requset):
        highlist = MyTopicStock.objects.all().order_by('-buy')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    # sell 매도호가 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def sell_highlist(self, requset):
        highlist = MyTopicStock.objects.all().order_by('-sell')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)



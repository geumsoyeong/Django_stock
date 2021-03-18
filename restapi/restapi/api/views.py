from rest_framework import viewsets
from rest_framework import permissions
from restapi.api.models import MyTopicStock
from restapi.api.serializers import MyTopicStockSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

import matplotlib
matplotlib.rcParams['font.family']
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

import pymysql
import matplotlib.pyplot as plt
import base64
from django.shortcuts import render

from matplotlib import font_manager, rc

# Create your views here.
class MyTopicStockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicStock.objects.all()
    serializer_class = MyTopicStockSerializer

    permission_classes = [permissions.IsAuthenticated]

    # /my_topic_users/search?q=???  #강사님 토픽 이름 기준임
    @action(detail=False, methods=['GET'])
    def search(self, request):
        q= requset.query_params.get('q', None)

        qs = self.get_queryset().filter(title=q)
        serializer = self.get_serializer(qs, many=True)

        #print(requset.query_params.get('q', None))

        return Response(serializer.data)

    ## 1-1 price 현재가 높은 순으로 데이터 그래프 보여주기
    @action(detail=False, methods=['GET'])
    def price_highlist_graph(self, request):
        highlist = MyTopicStock.objects.all().order_by('-price')
        serializer = self.get_serializer(highlist, many=True)

        data = pd.DataFrame(serializer.data)

        df1 = data.sort_values(by=['price'], axis=0, ascending=False).head(10)
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
        ax.plot(df1['title'],df1['price'])
        ax.set_xlabel('title')
        ax.set_ylabel('price')
        ax.set_title('현재가')
        font_name = font_manager.FontProperties(fname="C:\\Users\\A0501660\\Work\\font\\H2PORL.ttf").get_name() # Font 경로 재설정
        rc('font', family=font_name)
        plt.xticks(rotation=45, fontsize = 10)
        #plt.show()
        plt.savefig('price.png')
        # serializer.data

        # 파일 읽어오기
        with open('price.png', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # 파일 리턴
        ctx = {'image': image_data}
        return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)

        # return Response(serializer.data)

    ## 1-2 price 현재가 높은 순으로 데이터 정렬해서 보여주기

    @action(detail=False, methods=['GET'])
    def price_highlist(self, request):
        highlist = MyTopicStock.objects.all().order_by('-price')
        serializer = self.get_serializer(highlist, many=True)
        return Response(serializer.data)

    ## 2-1 volume 거래량 높은 순으로 데이터 그래프 보여주기
    @action(detail=False, methods=['GET'])
    def volume_highlist_graph(self, request):
        highlist = MyTopicStock.objects.all().order_by('-volume')
        serializer = self.get_serializer(highlist, many=True)

        data = pd.DataFrame(serializer.data)

        df2 = data.sort_values(by=['volume'], axis=0, ascending=False).head(10)
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
        ax.plot(df2['title'],df2['volume'])
        ax.set_xlabel('title')
        ax.set_ylabel('volume')
        ax.set_title('거래량')
        font_name = font_manager.FontProperties(fname="C:\\Users\\A0501660\\Work\\font\\H2PORL.ttf").get_name() # Font 경로 재설정        
        rc('font', family=font_name)
        plt.xticks(rotation=45, fontsize = 10)
        #plt.show()
        plt.savefig('volume.png')
        # serializer.data

        # 파일 읽어오기
        with open('volume.png', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # 파일 리턴
        ctx = {'image': image_data}
        return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)

    ## 2-2 volume 거래량 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def volume_highlist(self, request):
        highlist = MyTopicStock.objects.all().order_by('-volume')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    ## 3-1 payment 거래대금 높은 순으로 데이터 그래프 보여주기
    @action(detail=False, methods=['GET'])
    def payment_highlist_graph(self, request):
        highlist = MyTopicStock.objects.all().order_by('-payment')
        serializer = self.get_serializer(highlist, many=True)

        data = pd.DataFrame(serializer.data)

        df3 = data.sort_values(by=['payment'], axis=0, ascending=False).head(10)
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
        ax.plot(df3['title'],df3['payment'])
        ax.set_xlabel('title')
        ax.set_ylabel('payment')
        ax.set_title('거래대금')
        font_name = font_manager.FontProperties(fname="C:\\Users\\A0501660\\Work\\font\\H2PORL.ttf").get_name() # Font 경로 재설정        
        plt.xticks(rotation=45, fontsize = 10)
        #plt.show()
        plt.savefig('payment.png')
        # serializer.data

        # 파일 읽어오기
        with open('payment.png', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # 파일 리턴
        ctx = {'image': image_data}
        return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)

    ## 3-2 payment 거래대금 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def payment_highlist(self, request):
        highlist = MyTopicStock.objects.all().order_by('-payment')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    ## 4-1 buy 매수호가 높은 순으로 데이터 그래프 보여주기
    @action(detail=False, methods=['GET'])
    def buy_highlist_graph(self, request):
        highlist = MyTopicStock.objects.all().order_by('-buy')
        serializer = self.get_serializer(highlist, many=True)
        data = pd.DataFrame(serializer.data)

        df4 = data.sort_values(by=['buy'], axis=0, ascending=False).head(10)
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
        ax.plot(df4['title'],df4['buy'])
        ax.set_xlabel('title')
        ax.set_ylabel('buy')
        ax.set_title('매수호가')
        font_name = font_manager.FontProperties(fname="C:\\Users\\A0501660\\Work\\font\\H2PORL.ttf").get_name() # Font 경로 재설정        
        plt.xticks(rotation=45, fontsize = 10)
        #plt.show()
        plt.savefig('buy.png')
        # serializer.data

        # 파일 읽어오기
        with open('buy.png', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # 파일 리턴
        ctx = {'image': image_data}
        return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)        


    ## 4-2 buy 매수호가 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def buy_highlist(self, request):
        highlist = MyTopicStock.objects.all().order_by('-buy')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)

    ## 5-1 sell 매도호가 높은 순으로 데이터 그래프 보여주기
    @action(detail=False, methods=['GET'])
    def sell_highlist_graph(self, request):
        highlist = MyTopicStock.objects.all().order_by('-sell')
        serializer = self.get_serializer(highlist, many=True)
        data = pd.DataFrame(serializer.data)

        df5 = data.sort_values(by=['sell'], axis=0, ascending=False).head(10)
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
        ax.plot(df5['title'],df5['sell'])
        ax.set_xlabel('title')
        ax.set_ylabel('sell')
        ax.set_title('매도호가')
        font_name = font_manager.FontProperties(fname="C:\\Users\\A0501660\\Work\\font\\H2PORL.ttf").get_name() # Font 경로 재설정
        # serializer.data

        # 파일 읽어오기
        with open('sell.png', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # 파일 리턴
        ctx = {'image': image_data}
        return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)        

    ## 5-2 sell 매도호가 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def sell_highlist(self, request):
        highlist = MyTopicStock.objects.all().order_by('-sell')
        serializer = self.get_serializer(highlist, many=True)

        # serializer.data
        return Response(serializer.data)
    

    # ## 파일 읽어오기
    # with open('myfile.png', "rb") as image_file:
    #     image_data = base64.b64encode(image_file.read()).decode('utf-8')


    # ## 파일 리턴
    # ctx = {'image': image_data}
    # return render(request, 'C:\\Users\\A0501660\\Work\\rest_sample\\restapi\\restapi\\api\\index.html', ctx)

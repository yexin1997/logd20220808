"""
Created on July 30 2022
@author: Li,Ruijun
"""

from django.shortcuts import render
from graph.models import GraphPost
from .utils import count_nodes,graph_node_details,get_node_by_category,MODEL_ENTITIES,get_node_by_link,get_node_link_with_limit
import json

# Create your views here.

# page of graph
def graph_page(request):
    posts=GraphPost.objects.all()
    data = []
    links = []
    # for i in MODEL_ENTITIES.keys():
    #     a,b = get_node_by_category(i)
    #     data += a
    #     links += b
    for i in MODEL_ENTITIES.keys():
        a = get_node_by_category(i)
        data += a
    links = get_node_link_with_limit(3000)
    # print(data)
    # print(links)
    return render(request,'graph_page.html',{'posts':posts,'data0':json.dumps(data),'links0':json.dumps(links)})

# page of information of node
# def information(request,p1):
#     posts=GraphPost.objects.all()
#     return render(request,'information.html',{'posts':posts,'name':p1})

# page of information of node
def information(request,p1):
    posts=GraphPost.objects.all()
    # return render(request,'information.html',{'posts':posts})
    # p2 = str(p2).replace('.','-')
    node_detail = graph_node_details({'node_id':p1})
    links01 = get_node_by_link(p1)
    return render(request,'information.html',{'posts':posts,'node_detail':node_detail, 'Links01':links01})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetNodesData(APIView):
    def get(self, request):
        return Response('Temporary Data', status=status.HTTP_200_OK)


def logd(request):
    return render(request, 'logd.html')
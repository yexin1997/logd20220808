"""
Created on July 30 2022
@author: Li,Ruijun
"""

from django.urls import re_path
from . import views
from .views import GetNodesData

urlpatterns=[
    re_path(r'^information/(\w+)/',views.information),
    re_path(r'^logd$',views.logd),
    #re_path(r'^nodes[/]?$', GetNodesData.as_view() , name='get_nodes_data'),
]
# http://127.0.0.1:8000/graph/nodes

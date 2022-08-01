"""
Created on July 30 2022
@author: Li,Ruijun
"""

from .models import government, geography, media, social_networking, linguistics, user_generated, publications, cross_domain
import numpy as np
import pandas as pd
from py2neo import Node,Relationship,Graph,Path,Subgraph,NodeMatcher,RelationshipMatcher

# MODEL_ENTITIES = {
#     'Car': Car,
#     'Book': Book
#}

MODEL_ENTITIES = {
    'government': government,
    'geography': geography,
    'media': media,
    'social_networking': social_networking,
    'linguistics': linguistics,
    'user_generated': user_generated,
    'publications': publications,
    'cross_domain': cross_domain
}
# connect to neo4j database
neo4j_url = 'bolt://localhost:7687/'
user = 'neo4j'
pwd = 'yexin123'
graph = Graph(neo4j_url,  auth=(user, pwd))

# filter nodes
def filter_nodes(node_type,node_name):
    node_set = node_type.nodes

    node_set.filter(name__contains=node_name)
    # # On Address nodes we want to check the search_text against the address property
    # # For any other we check against the name property
    # if node_type.__name__ == 'Car':
    #     node_set.filter(address__icontains=node_name)
    # else:
    #     node_set.filter(name__icontains=node_name)

    return node_set

# count the number of nodes
def count_nodes(count_info):
    count = {}
    node_type               = count_info['node_type']
    name             = count_info['node_name']
    node_set                = filter_nodes(MODEL_ENTITIES[node_type], name)
    count['count']          = len(node_set)

    return count

# example of the required dictionary keys
# {
#     'node_type': '',
#     'node_id': ''
# }
# the detail of nodes
def graph_node_details(node_info):
    node_id = node_info['node_id']
    cypher_ = "MATCH(n) where id(n)=%d return n" % (int(node_id))
    df = graph.run(cypher_).to_data_frame()
    node_details = {}
    node_details['name'] = df.loc[0]['n']['dataSet_title']+'-'+ str(df.loc[0]['n'].identity)
    node_details['url'] = df.loc[0]['n']['uri']
    node_details['description'] = df.loc[0]['n']['dct__description']
    return node_details

# Get nodes by type
def get_node_by_category(category):
    node_type       = category
    node = MODEL_ENTITIES[node_type].nodes.all()
    index = 0
    data = []
    for row in node:
        data.append({
            'name': row.name,
            'des': row.name,
            'symbolSize': row.size,
            'category': category,
            'x' : row.x,
            'y' : row.y
        })
        index+=1
    # print(data)
    return data
    cypher_="MATCH (n:"+category+")-[r:links]- (m:"+category+") return n,m"
    # cypher_ = "MATCH (n)-[r:links]- (m) return n,m  LIMIT 20"
    df = graph.run(cypher_).to_data_frame()

    link = []
    for i, row in df.iterrows():
        node_link = {'source': row['n']['name'],
                     'target': row['m']['name'],
                     'name':'links',
                     # 'name': category+'_link_'+str(i),
                     # 'des': category+'_link_'+str(i)
            }
        # print(row['n']['name'], row['m']['name'])
        link.append(node_link)
    # print(link)
    return data,link

# Get its connected nodes by node
def get_node_by_link(node_id):
    # node_name = str(node_name).replace('-','.')
    cypher_ = "MATCH(m)--(n) where id(m)=%s return n" % (node_id)
    df = graph.run(cypher_).to_data_frame()
    link_nodes = []
    for i, row in df.iterrows():
        # link_nodes.append({'url': 'http://42.194.205.96:8000/graph/information/%s/%s' % (row['n']['category'], row['n']['name']),'name': row['n']['name']})
        link_nodes.append({'url':row['n']['uri']})
    # print(link_nodes)
    return link_nodes


# Get nodes by type
def get_node_link_with_limit(limit):
    cypher_ = "MATCH (n)-[r:links]- (m) return n,m  LIMIT %d" % (limit)
    df = graph.run(cypher_).to_data_frame()

    link = []
    for i, row in df.iterrows():
        node_link = {'source': row['n']['name'],
                     'target': row['m']['name'],
                     'name':'links',
                     # 'name': category+'_link_'+str(i),
                     # 'des': category+'_link_'+str(i)
            }
        # print(row['n']['name'], row['m']['name'])
        link.append(node_link)
    return link

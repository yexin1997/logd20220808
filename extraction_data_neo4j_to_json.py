"""
Created on July 30 2022
@author: Li,Ruijun

This file is extracting data from neo4j into a json file
"""
import random
from py2neo import Graph
import json

data_clean = {}
g = Graph("bolt://localhost:7687", auth=("neo4j", "yexin123"))
category = ['Economy_And_Finance', 'Education_Culture_And_Sport', 'Energy', 'Environment', 'Government', 'Health']

for c in category:
       cypher_ = "MATCH (n:%s) RETURN n" % c
       df_nodes = g.run(cypher_).to_data_frame()
       for row in df_nodes.iterrows():
              node_id = row[1]['n'].identity       # id of node
              # print(node_id)
              node_name = row[1]['n']['dataSet_title']+'-'+str(node_id)  # title of node
              node_url = row[1]['n']['uri']         # url of node
              # node_identifier = row['n']['ns2__identifier']     # identifier of node
              node_description = row[1]['n']['ns2__description']  # description of node

              data_clean[node_name] = {'name': node_name, 'url': node_url, 'description':node_description, 'category':c}
              cypher_2 = "MATCH p=(e)-->(m) where id(e)=%d RETURN m" % node_id
              df_links = g.run(cypher_2).to_data_frame()
              data_clean[node_name]['links'] = []
              for row2 in df_links.iterrows():
                     # id is row['e'].identity
                     target_name = row2[1]['m']['dataSet_title'] + '-' + str(row2[1]['m'].identity)
                     data_clean[node_name]['links'].append({'target': target_name})

# print(data_clean)
with open('data_europa_220728.json','w') as f:
    json.dump(data_clean,f)
    print('ok1')


r_position = []
path2 = "data_europa_220728.json"
# read data file
with open(path2, "r") as f:
    row_data2 = json.load(f)

# create node
# Connect to neo4j (4.*)
#g = Graph("bolt://localhost:7687", auth=("neo4j", "yexin123"))
data_json = {'nodes':[],'edges':[]}
# setting color
n_color = {'Economy_And_Finance': '#FF5809', 'Energy': '#921AFF', 'Education_Culture_And_Sport': '#0080FF',
           'Government': '#FF0000', 'Environment': '#00A600', 'Health': '#FF359A'}
# extraction process
for k in row_data2.keys():
    n = row_data2[k]

    n_size = len(n['links'])    # get the number of links
    # the size of node depends on the number of links
    # the minimum size is 1
    if n_size == 0:
        n_size = 1
    # the maximum size is 100
    elif n_size > 100:
        n_size = 100

    # setting random coordinate
    x_position = 0
    y_position = 0

    # restrict random coordinate points on the circular canvas
    while True:
        x_position = '%.4f' % random.uniform(-1500, 1500)
        y_position = '%.4f' % random.uniform(-1500, 1500)
        d_center = pow(pow(float(y_position), 2) + pow(float(x_position), 2), 0.5)
        # if the coordinate points is not on the circular canvas, it will be dropped.
        if str(x_position)+str(y_position) in r_position:
            continue
        elif d_center > 1500:
            continue
        else:
            r_position.append(str(x_position)+str(y_position))
            break

    # new node
    new_node = {'id': str(n['name']).split('-')[1],'name': str(n['name']), 'url': str(n['url']), 'description': n['description'],
             'category': str(n['category']), 'size': n_size, 'x': x_position, 'y': y_position,'color':n_color[str(n['category'])]}

    # append the node node
    data_json['nodes'].append(new_node)
    # append new links into dataset
    for l in n['links']:
        l['source'] = n['name']
        l['target'] = l['target']
        data_json['edges'].append(l)
# save data into local file
with open('data_europa_220729.json','w') as f:
    json.dump(data_json,f)
print('finished')
"""
Created on July 30 2022
@author: Li,Ruijun

This file is extracting RDF data into neo4j
"""
from py2neo import Graph
import os

files = ['Economy_And_Finance','Education_Culture_And_Sport','Energy','Environment','Government','Health']
g = Graph("bolt://localhost:7687", auth=("neo4j", "yexin123"))
cypher_="MATCH (n) DETACH DELETE n"
g.run(cypher_)
cypher_="call dbms.procedures()"
g.run(cypher_)
cypher_="CREATE(n:Resource)"
g.run(cypher_)
for c in files:
       path = '/usr/project/'+c
       all = []
       # os.walk is to get all directories
       for fpath, dirs, fs in os.walk(path):
              for f in fs:
                     filename = os.path.join(fpath, f)
                     # Judge whether it ends with "rule", and customize the rule
                     all.append(filename)
       for path in all:
              title = path.split('/')[4].split('.')[0]
              path = "file:///"+path
              print(title)
              print(path)
              cypher_1 = "call semantics.importRDF('%s', 'RDF/XML')" %(path)
              cypher_2 = "MATCH (n:Resource) set n:%s, n.dataSet_title='%s' return n" % (c,title)
              cypher_3 = "MATCH (n:Resource) REMOVE n:Resource RETURN n"
              # cypher_4 = "MATCH (n:%s) REMOVE n:%s RETURN n" %(title,title)
              # print(cypher_1)
              # print(cypher_2)
              # print(cypher_3)
              g.run(cypher_1)
              g.run(cypher_2)
              g.run(cypher_3)
              # g.run(cypher_4)
print('ok')

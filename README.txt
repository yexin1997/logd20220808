1.Introduction
The whole project is created by Li,Ruijun.
It is a practice of building a knowledge graph framework. Through the knowledge graph visualization system that builds the foundation for government public data sets, the relationships and information between different data sets are displayed. Each node represents a data set, and each edge represents a relationship between the two data sets. It shows users the classified structured knowledge in a graphical way, and organizes the government open data sets at the least cost to become knowledge that can be used. In addition, the project is finally constructed as a browser/server architecture (B/S) system and deployed on the public cloud. 

2.Development tools listings:
Python 3.9.7;
Neo4j 3.5.34 with JDK 8 (8u271);
Django 4,0,4;
django-neomodel 0.0.7;
djangorestframework 3.13.1;
numpy 1.21.2;
pandas 1.3.4;
neomodel 4.0.8;
py2neo 2021.2.3;
E-chart 5.3.3;

3.Source code listings:
-kg: The main file;
--graph: Knowledge graph application in the Django project;
---migrations: It is mainly used to synchronize the model class in Django application and the schema of database structure, Django automatic generation.;
---static: Storing data, image, JS and other static files;
----data: The JSON file of graph data;
----image: The image of legend;
----js: The JavaScript of the front-end web page;
---templates: It is the templates layer which has the HTML files of the front-end web page;
----logd.html: It is the home page showing the knowledge graph;
----information.html: It is the detail information page of nodes;
---_init_.py: Python initial file, automatically generated;
---admin.py: Application administration function;
---apps.py: The setting of application;
---models.py: Defining classes of node
---tests.py: Django TestCase, automatically generated;
---urls.py: Links jump settings;
---utils.py: It is the model layer which is for Back-end data processing function;
---views.py: It is the view layer which is for Fort-end data transmission function;
--kg: the main application in the Django project;
---asgi.py: Asynchronous framework settings, automatically generated;
---settings.py: the settings of Django framework;
---urls.py: Links jump settings;
---wsgi.py: Web Server Gateway Interface settings, automatically generated;
--manage.py: Manage Django servers, automatically generated;
--extraction_data_neo4j_to_json.py: extract data from neo4j into a json file;
--extraction_RDF_data_to_neo4j.py: extract rdf data to neo4j;
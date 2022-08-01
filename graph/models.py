"""
Created on July 30 2022
@author: Li,Ruijun
"""

from django.db import models
from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    FloatProperty
)

# Create your models here.
class GraphPost(models.Model):
    # title of main page
    title = models.CharField(max_length=150)
    # body of main page
    body = models.TextField()
    # time of create
    timestamp = models.DateTimeField()
    # name of node
    # name = models.CharField(max_length=150)


class Car(StructuredNode):
    name = StringProperty()
    id = StringProperty(index = True)

class Book(StructuredNode):
    name = StringProperty()
    id = StringProperty(index = True)

class government(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class geography(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class media(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class social_networking(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class linguistics(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class user_generated(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class publications(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

class cross_domain(StructuredNode):
    name = StringProperty(index=True)
    url = StringProperty()
    description = StringProperty()
    size = FloatProperty()
    x = FloatProperty()
    y = FloatProperty()

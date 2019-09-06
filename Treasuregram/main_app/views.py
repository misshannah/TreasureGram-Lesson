# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html', {'treasures' :treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url
treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",'nugget.jpg'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",'gold.jpg'),
    Treasure('Coffeee Can', 20.00, 'tin', "Acme, CA",'coffe.jpg')
]

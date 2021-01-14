from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request, tvno=0):
    tv_list = [
        {'name': 'bilibili', 'tvcode': '543720896&bvid=BV1Pv4y1f7ux&cid=281756331&page=1'},
        {'name': 'bilibili1', 'tvcode': '75873404&bvid=BV1rJ411U7JD&cid=129761418&page=1'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())


def engtv(request, tvno=0):
    tv_list = [
        {'name': 'bilibili', 'tvcode': '801018079&bvid=BV1Vy4y1v7Gs&cid=280335087&page=1'},
        {'name': 'bilibili1', 'tvcode': '455458860&bvid=BV1D5411x7DD&cid=185269426&page=1'},
        {'name': 'bilibili2', 'tvcode': '73442179&bvid=BV14E411a7UE&cid=125631043&page=1'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'engtv.html', locals())

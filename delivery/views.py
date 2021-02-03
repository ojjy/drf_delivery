from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipping_info
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
import requests
import json
from urllib import parse
from folium import Map, Marker, Icon, Figure
from folium.plugins import MarkerCluster
import folium

def getLatLng(addr):
    print("getLatLng function call")
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 9689cf5d703ad53dba79703ad0ebc485"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    print(requests.get(url, headers=headers))
    print(result)
    match_first = result['documents'][0]['address']
    lon = match_first['x']
    lat = match_first['y']
    print(lon, lat)
    print(match_first)

    return lon, lat


class ShippingDetailView(DetailView):
    model = Shipping_info
    template_name = "shipping_detail.html"

class ShippingReadOnlyDetailView(DetailView):
    model = Shipping_info
    template_name = "shipping_readonly_detail.html"

class FoliumView(TemplateView):
    template_name = "shipping_map.html"

    def get_context_data(self, **kwargs):
        figure = Figure()
        m = Map(location=[36.5053542, 127.7043419], zoom_start=8)
        m.add_to(figure)

        customer_list = Shipping_info.objects.all()

        for obj_list in Shipping_info.objects.values_list():
            print("=================================================")
            print("obj_list:: ", obj_list)
            print("=================================================")
            sender_addr = obj_list[6]
            print("view_test function call:: sender_addr - "+sender_addr)
            sender_lon, sender_lat = getLatLng(sender_addr)
            print("=================================================")
            print("sender_lat, sender_lon:: ", sender_lat, sender_lon)
            print("=================================================")

            html = folium.Html('<a href = "' + 'http://127.0.0.1:8000/shipping_detail/'+ str(obj_list[0])+ '"target="_blank">'+ '접수내역 확인' + '</a>', script=True)
            popup = folium.Popup(html, max_width=2650)
            Marker(location = [sender_lat, sender_lon], popup = popup, icon=Icon(color='green', icon='flag')).add_to(m)
        figure.render()
        return {"map":figure, "cutomer_list":customer_list}


class ShippingUpdateView(UpdateView):
    model = Shipping_info
    fields = ['pickup_man', 'delivery_man', 'memo', 'delivery_status']
    template_name = "shipping_edit.html"
    def get_success_url(self):
        return reverse('shipping_detail', args=[str(self.object.id)])


class ShippingDeleteView(DeleteView):
    model = Shipping_info
    template_name = "shipping_delete.html"

    def get_success_url(self):
        messages.success(self.request, "삭제 성공")
        return reverse('shipping_map')
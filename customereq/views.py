from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomereqSerializer
from .models import Customereq
from .forms import CustomereqForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
# Create your views here.

###########################################REST_API############################

class CustomereqViewset(viewsets.ModelViewSet):
    queryset = Customereq.objects.all()
    serializer_class = CustomereqSerializer

##############################################WEB#########################

class CustomereqCreateView(CreateView):
    model = Customereq
    template_name = "request_ship.html"
    form_class = CustomereqForm
    success_url = "request_detail"

    # 처음 객체 생성때, object의 값 저장, tracking넘버 생성해서 Customereq객체 내 할당
    def form_valid(self, form):
        self.object = form.save()
        # shipping_info = Shipping_info.objects.create_shipping(dam_request_id=form.cleaned_data['dam_request_id'],
        #                                                       departure=form.cleaned_data["sender_address"],
        #                                                       destination=form.cleaned_data["receiver_address"])
        # shipping_info.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, "배송요청 성공")
        return reverse('request_detail', kwargs={'pk':self.object.pk})


class CustomereqDetailView(DetailView):
    model = Customereq
    template_name = "request_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CustomereqDeleteView(DeleteView):
    model = Customereq
    success_url = reverse_lazy('index')
    template_name = "request_delete.html"

    def get_success_url(self):
        messages.success(self.request, "삭제 성공")
        return reverse('index')

class CustomereqUpdateView(UpdateView):
    model = Customereq
    template_name = 'request_update.html'
    form_class = CustomereqForm

    def get_success_url(self):
        messages.success(self.request, "배송요청 성공")
        return reverse('request_detail', kwargs={'pk':self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())


class CustomereqListView(ListView):
    model = Customereq
    template_name = 'request_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


from django.shortcuts import render
from .models import AnonymBoard
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from rest_framework import viewsets
from .serializers import AnonymBoardSerializer

# Create your views here.
class AnonymBoardCreateView(CreateView):
    model = AnonymBoard
    fields = ['title', 'content']
    template_name = "create.html"

    def get_success_url(self):
        messages.success(self.request, "글쓰기 성공")
        return reverse('detail', kwargs={'pk':self.object.pk})


class AnonymBoardDetailView(DetailView):
    model = AnonymBoard
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AnonymBoardDeleteView(DeleteView):
    model = AnonymBoard
    success_url = reverse_lazy('')
    template_name = "delete.html"

    def get_success_url(self):
        messages.success(self.request, "삭제 성공")
        return reverse('')

class AnonymBoardUpdateView(UpdateView):
    model = AnonymBoard
    fields = ['title', 'content']
    template_name = 'edit.html'

    def get_success_url(self):
       messages.success(self.request, "글수정 성공")
       return reverse('detail', kwargs={'pk':self.object.pk})



class AnonymBoardListView(ListView):
    model = AnonymBoard
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#######################################################################


class AnonymBoardViewset(viewsets.ModelViewSet):
    queryset = AnonymBoard.objects.all()
    serializer_class = AnonymBoardSerializer
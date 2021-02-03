from django.shortcuts import render, get_object_or_404
from .models import Board
from .models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse, reverse_lazy



class BoardCreateView(CreateView):
    model = Board
    fields = ['title', 'author', 'content']
    template_name = "bo_create.html"

    def get_success_url(self):
        messages.success(self.request, "글쓰기 성공")
        return reverse('bo_detail', kwargs={'pk':self.object.pk})

class BoardDetailView(DetailView):
    model = Board
    template_name = "bo_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BoardDeleteView(DeleteView):
    model = Board
    success_url = reverse_lazy('')
    template_name = "bo_delete.html"

    def get_success_url(self):
        messages.success(self.request, "삭제 성공")
        return reverse('')

class BoardUpdateView(UpdateView):
    model = Board
    fields = ['title', 'content']
    template_name = 'bo_edit.html'

    def get_success_url(self):
       messages.success(self.request, "글수정 성공")
       return reverse('bo_detail', kwargs={'pk':self.object.pk})



class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment_user', 'comment_body']
    template_name = "com_create.html"

    def post(self, request, *args, **kwargs):
        board = get_object_or_404(Board, pk=self)


    def get_success_url(self):
        messages.success(self.request, "글쓰기 성공")
        return reverse('com_detail', kwargs={'pk':self.object.pk})

class CommentDetailView(DetailView):
    model = Comment
    template_name = "com_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comment_body'] = Comment.objects.all()
        return context

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('')
    template_name = "com_delete.html"

    def get_success_url(self):
        messages.success(self.request, "삭제 성공")
        return reverse('')

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['comment_user', 'comment_body']
    template_name = 'com_edit.html'

    def get_success_url(self):
       messages.success(self.request, "글수정 성공")
       return reverse('com_detail', kwargs={'pk':self.object.pk})
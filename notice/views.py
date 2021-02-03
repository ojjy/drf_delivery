from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Notice
from .models import Image
from django.utils.timezone import now
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.forms import modelformset_factory
from datetime import datetime
from .forms import ImageForm, NoticeForm

# Create your views here.
#다중이미지 업로드를 위한 view
def post(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
    if request.method == 'POST':
        noticeForm = NoticeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
        if noticeForm.is_valid() and formset.is_valid():
            notice_form = noticeForm.save(commit=False)
            notice_form.save()
            for form in formset.cleaned_data:
                if form:
                    img = form['img']
                    photo = Image(notice=notice_form, img=img)
                    photo.save()
            messages.success(request, "success")
            # return redirect("notice_create_fbv")
            return redirect('/detail/' + str(Notice.pk))

        else:
            print(noticeForm.errors, formset.errors)
    else:
        noticeForm = NoticeForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'notice_create_fbv.html',
                  {'noticeForm': noticeForm, 'formset': formset})


class NoticeCreateView(CreateView):
    model = Notice
    fields = ['title', 'content']
    template_name = 'notice_create.html'

    def get_success_url(self):
        return reverse('notice_detail', kwargs={'pk':self.object.pk})

class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice_detail.html'

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_date'] = now()
        return context

class NoticeUpdateView(UpdateView):
    model = Notice
    fields = ['title', 'content', 'img']
    template_name = 'notice_update.html'

    def get_success_url(self):
        return reverse('notice_detail', kwargs={'pk':self.object.pk})

class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = 'notice_delete.html'
    success_url = reverse_lazy('index')



# 검색관련 template수정 필요
class NoticeListView(ListView):
    model = Notice
    paginate_by = 10
    template_name = 'notice_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        notice_fixed = Notice.objects.filter(top_fixed=True).order_by('-registered_date')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type
        context['notice_fixed'] = notice_fixed

        return context

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get(type, '')
        notice_list = Notice.objects.order_by('-id')
        search_notice_list = None
        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_notice_list = notice_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_notice_list = notice_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_notice_list = notice_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_notice_list = notice_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_notice_list = notice_list.filter(writer__user_id__icontains=search_keyword)

                return search_notice_list
            else:
                messages.error(self.request, '검색어 2글자 이상')
        return notice_list

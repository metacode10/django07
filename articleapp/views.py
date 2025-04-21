from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from articleapp.forms import AritcleCreationForm
from articleapp.models import Article


# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AritcleCreateView(CreateView):
    model = Article
    form_class = AritcleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reversed('articleapp:detail', kwargs={'pk': self.object.pk})



class AritcleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
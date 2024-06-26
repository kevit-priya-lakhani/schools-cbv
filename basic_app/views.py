from typing import Any
from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,CreateView,UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

# Create your views here.
def index(request):
    return render(request,'index.html')

class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based View!!")
    
class IndexView(TemplateView):

    template_name='index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['content']='Basic Injection'
        return context
    
class SchoolListView(ListView):
    model= models.School # creates a list object_list that stores all the objects in the model
    context_object_name='school_list' # renames object_list to friendlier template context
    template_name='basic_app/school_list.html'

class SchoolDetailView(DetailView):
    slug_url_kwarg = "id"
    slug_field = "id"
    model=models.School
    context_object_name='school_detail'
    template_name='basic_app/school_detail.html' #set up template next

class SchoolCreateView(CreateView):
    model=models.School
    fields=('name','principal','location')
    # template_name='basic_app/school_form.html' # if you dont specify template name CreateView will default to modelname_form.html

class SchoolUpdateView(UpdateView):
    slug_url_kwarg = "id"
    slug_field = "id"
    fields=('name','principal')
    model=models.School #defaults to modelname_form.html

class SchoolDeleteView(DeleteView):
    slug_url_kwarg = "id"
    slug_field = "id"
    model=models.School
    success_url=reverse_lazy("basic_app:list")  #will default to modelname_confirm_delete.html
    
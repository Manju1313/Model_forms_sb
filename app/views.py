from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *
def djangoforms(request):
    NF=NameForm()
    d={'form':NF}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            #return HttpResponse(str(form_data.cleaned_data))
            n=form_data.cleaned_data['name']
            a=form_data.cleaned_data['age']
            g=form_data.cleaned_data['gender']
            
            c=form_data.cleaned_data['course']
            d1={'n':n,'a':a,'g':g,'c':c}
            return render(request,'data.html',d1)
    return render(request,'djangoforms.html',d)

def insert_topic(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            nt=form_data.cleaned_data['topic']
            dt=form_data.cleaned_data['date']
            #T=Topic.objects.get_or_create(topic_name=nt,date=dt)[0]
            #T.save()
            return HttpResponse('Inserted')
    return render(request,'insert.html',d)


from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import Topic

def listing(request):
    contact_list = Topic.objects.all()
    paginator = Paginator(contact_list, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '.html', {'page_obj': page_obj})

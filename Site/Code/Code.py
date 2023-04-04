from django.forms import Textarea
from Site.models import *

def post_Method(request,pageName,sectionName,sectionContextName,myForm ):
    form = myForm(request.POST, None)
    if form.is_valid():
        cd = form.cleaned_data
        item = Page.objects.get(name=pageName, section=sectionName, contextName=sectionContextName)
        item.context = cd
        item.save()

def get_Method(request,pageName,sectionName,sectionContextName,myForm ):
    form = myForm()
    try:
        item = Page.objects.get(name=pageName, section=sectionName, contextName=sectionContextName)
        if item:
            for i in item.context:
                form.fields[i].initial = item.context[i]
    except:
        context = {}
        for i in form.fields:
            try:
                if isinstance(form.fields[i].widget, Textarea):
                    context[i] = 'لورم چند خطه'
                    form.fields[i].initial = context[i]
                else:
                    if form.fields[i].required == True:
                        context[i] = 'home'
                        form.fields[i].initial = 'home'
                    else:
                        context[i] = i
                        form.fields[i].initial = context[i]
            except:
                pass
        item = Page()
        item.name = pageName
        item.section = sectionName
        item.contextName = sectionContextName
        item.context = context
        item.save()
    return form







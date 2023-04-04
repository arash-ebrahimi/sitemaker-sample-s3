from Site.models import *

def getParent(pk):
    model = dirUploadedImages.objects.get(pk=pk)
    context={}
    try:
        parentmodel = dirUploadedImages.objects.get(pk=model.rootID)
        context['parentName'] = parentmodel.name
        context['parentpk'] = parentmodel.pk
    except:
        context['parentpk']=1
        context['parentName'] = 'ریشه'
    return context

def getChild(pk):
    retmodel=  dirUploadedImages.objects.filter(rootID=pk)
    ret=[]
    for i in retmodel:
        if i.name != 'ریشه':
            context ={}
            context['childName'] = i.name
            context['childtpk'] = i.pk
            ret.append(context)
    return ret

def getDirImages(pk):
    model = Picture.objects.filter(dir=pk).order_by('-pk')
    ret=[]
    for i in model:
        context = {}
        context['id'] = i.pk
        context['pictureAddress'] = i.picture_addr
        context['width'] = i.width
        context['height'] = i.height
        ret.append(context)
    ret.reverse()
    return ret


def getDirInfo(pk):
    ret=[]
    index=pk
    while True:
        get = getParent(index)
        ret.append(get)
        index = get['parentpk']
        if index == 1:
            break
    context = {}
    ret.reverse()


    model = dirUploadedImages.objects.get(pk=pk)
    if model.name != 'ریشه' :
        item = {}
        item['parentName']=model.name
        item['parentpk']=model.pk
        ret.append(item)

    context['parents'] = ret
    context['childs'] = getChild(pk)
    context['images'] = getDirImages(pk)
    context['pk'] = pk
    if len(context['childs']) == 0 and len(context['images']) == 0:
        if len(ret) == 1 and ret[0]['parentpk'] ==1:
            context['canDelete'] = False
        else:
            context['canDelete'] = True
    else:
        context['canDelete'] = False
    context['canEdit'] = True
    if pk == 1: context['canEdit'] = False
    return context

import json
import os
from datetime import datetime

from django.core.files.images import get_image_dimensions
from django.shortcuts import render, redirect
from minio import Minio

from Site.forms import *
from Site.models import *
from Site.Code.ImageDir import *
from Site.Code.SQLServerDB import *
from Site.Code.MACAddress import *



def dashboard(request):
    return render(request, './Main/home.html')


def showUploadImage(request, pk):
    if request.method == 'POST':
        checkbx_state = "unchecked"
        if 'id_chkcbox' in request.POST:
            if request.POST.get('id_chkcbox') == 'on':
                checkbx_state = "checked"

        arr = request.session.get('checkedItems', None)
        if arr:
            if pk in arr:
                arr.remove(pk)
            if checkbx_state == "checked":
                arr.append(pk)
        else:
            arr = []
            if checkbx_state == "checked":
                arr.append(pk)
        request.session['checkedItems'] = arr
        return redirect('showUploadImage', pk=pk)
    else:
        model = Picture.objects.get(pk=pk)
        arr = request.session.get('checkedItems', None)
        state = False
        if arr:
            if pk in arr:
                state = True
        roo_pk = model.dir
        images = Picture.objects.filter(dir=roo_pk)
        images_arr = []
        for i in images:
            images_arr.append({'pk': i.pk, 'img_address': i.picture_addr})
        nextImage = -1
        prevImage = -1
        for i in range(len(images_arr)):
            if images_arr[i]['pk'] == pk:
                try:
                    nextImage = images_arr[i + 1]['pk']
                except:
                    nextImage = images_arr[0]['pk']
                try:
                    prevImage = images_arr[i - 1]['pk']
                except:
                    pass
        nextImage_Address = ''
        prevImage_Address = ''
        for i in images_arr:
            if i['pk'] == nextImage:
                nextImage_Address = i['pk']
            if i['pk'] == prevImage:
                prevImage_Address = i['pk']
        return render(request,
                      './Upload/showUploadedImage.html',
                      {'img_address': model.picture_addr,
                       'checked': state,
                       'next_address': nextImage_Address,
                       'prev_address': prevImage_Address,
                       'rootID': model.dir,
                       'width': model.width,
                       'height': model.height,
                       'imagePK': model.pk,
                       }
                      )


def addDirectory(request, pk):
    if request.method == 'POST':
        if 'add' in request.POST:
            ret = request.POST.get('adddirectory').strip()
            if ret != '':
                try:
                    check = dirUploadedImages.objects.get(rootID=pk, name=ret)
                except:
                    model = dirUploadedImages()
                    model.name = ret
                    model.rootID = pk
                    model.save()
        return redirect("imageDirManager", pk=pk)
    model = dirUploadedImages.objects.get(pk=pk)
    return render(request, './Upload/addDirectory.html', {'name': model.name})


def editDirectory(request, pk):
    if request.method == 'POST':
        if 'update' in request.POST:
            ret = request.POST.get('editdirectory').strip()
            if ret != '':
                arr = dirUploadedImages.objects.filter(rootID=dirUploadedImages.objects.get(pk=pk).rootID, name=ret)
                if len(arr) == 0:
                    model = dirUploadedImages.objects.get(pk=pk)
                    model.name = ret
                    model.save()
                else:
                    pass
        return redirect("imageDirManager", pk=pk)
    model = dirUploadedImages.objects.get(pk=pk)
    return render(request, './Upload/editDirectory.html', {'name': model.name})


def deleteDirectory(request, pk):
    if request.method == 'POST':
        if 'delete' in request.POST:
            model = dirUploadedImages.objects.get(pk=pk)
            parentID = model.rootID
            model.delete()
            return redirect("imageDirManager", pk=parentID)
        return redirect("imageDirManager", pk=pk)
    model = dirUploadedImages.objects.get(pk=pk)
    return render(request, './Upload/deleteDirectory.html', {'name': model.name})


def imageDirManager(request, pk):
    context = getDirInfo(pk)
    if request.method == 'POST':
        sec = []
        for i in context['images']:
            if request.POST.get('id_' + str(i['id'])) == 'on':
                sec.append(i['id'])
        data = {}
        if 'copy' in request.POST:
            data['type'] = 'copy'
            data['items'] = sec
            request.session['clipboard'] = data
            request.session['checkedItems'] = []
            request.session.set_expiry(0)
        if 'cut' in request.POST:
            data['type'] = 'cut'
            data['items'] = sec
            request.session['clipboard'] = data
            request.session['checkedItems'] = []
            request.session.set_expiry(0)
        if 'paste' in request.POST:
            val = request.session.get('clipboard', '')
            if val != '':
                type = val['type']
                items = val['items']
                if type == 'cut':
                    for i in items:
                        picture = Picture.objects.get(pk=i)
                        picture.dir = pk
                        picture.save()
                if type == 'copy':
                    for i in items:
                        picture = Picture.objects.get(pk=i)
                        newPicture = Picture()
                        newPicture.dir = pk
                        newPicture.picture_addr = picture.picture_addr
                        newPicture.width = picture.width
                        newPicture.height = picture.height
                        newPicture.save()
                request.session['clipboard'] = ''
                request.session['checkedItems'] = []
                request.session.set_expiry(0)
        if 'delete' in request.POST:
            for i in sec:
                picture = Picture.objects.get(pk=i)
                picture.delete()
            request.session['clipboard'] = ''
            request.session.set_expiry(0)
        return redirect("imageDirManager", pk=pk)
    else:
        pass
    context['checkedItems'] = request.session.get('checkedItems', None)
    return render(request, "./Upload/ImageDirManager.html", context)


def UPLOADImages(request):
    if request.method == 'POST':
        picture_addr = request.FILES.getlist('images')
        for image in picture_addr:
            picture = Picture.objects.create(picture_addr=image)
            w, h = get_image_dimensions(image)
            picture.width = w
            picture.height = h
            picture.save()
        return redirect("imageDirManager", pk=1)
    else:
        form = PictureForm()
    return render(request, './Upload/Images.html', {
        'form': form})


def home(request):
    client = Minio('minio-z1zgcp.chbk.run',
                   access_key='KErFxoers4dpySO8Fd8d88pqjfxwtzgp',
                   secret_key='CxRKxgTcAhNCDG6zHFkQesxpL0ccAqHa')

    buckets = client.list_buckets()

    for bucket in buckets:
        print(bucket.name, bucket.creation_date)

        # policy_read_only = {
        #     "Version": "2012-10-17",
        #     "Statement": [
        #         {
        #             "Sid": "",
        #             "Effect": "Allow",
        #             "Principal": {"AWS": "*"},
        #             "Action": "s3:GetBucketLocation",
        #             "Resource": "arn:aws:s3:::new-bucket-5bb74c23"
        #         },
        #         {
        #             "Sid": "",
        #             "Effect": "Allow",
        #             "Principal": {"AWS": "*"},
        #             "Action": "s3:ListBucket",
        #             "Resource": "arn:aws:s3:::new-bucket-5bb74c23"
        #         },
        #         {
        #             "Sid": "",
        #             "Effect": "Allow",
        #             "Principal": {"AWS": "*"},
        #             "Action": "s3:GetObject",
        #             "Resource": "arn:aws:s3:::new-bucket-5bb74c23/*"
        #         }
        #     ]
        # }
        # client.set_bucket_policy('new-bucket-5bb74c23', json.dumps(policy_read_only))
# pip install minio
        policy_read_write = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": ["s3:GetBucketLocation"],
                    "Sid": "",
                    "Resource": ["arn:aws:s3:::new-bucket-5bb74c23"],
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"}
                },
                {
                    "Action": ["s3:ListBucket"],
                    "Sid": "",
                    "Resource": ["arn:aws:s3:::new-bucket-5bb74c23"],
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"}
                },
                {
                    "Action": ["s3:ListBucketMultipartUploads"],
                    "Sid": "",
                    "Resource": ["arn:aws:s3:::new-bucket-5bb74c23"],
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"}
                },
                {
                    "Action": ["s3:ListMultipartUploadParts",
                               "s3:GetObject",
                               "s3:AbortMultipartUpload",
                               "s3:DeleteObject",
                               "s3:PutObject"],
                    "Sid": "",
                    "Resource": ["arn:aws:s3:::new-bucket-5bb74c23/*"],
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"}
                }
            ]
        }
        client.set_bucket_policy('new-bucket-5bb74c23', json.dumps(policy_read_write))
    return render(request, "./pages/Page1.html")


def page2(request):
    Context = {}

    pageName = 'Page2'
    sectionName = 'Cases1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page2'
    sectionName = 'Cases2'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page2'
    sectionName = 'Counter1'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page2'
    sectionName = 'Detail1'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page2'
    sectionName = 'Detail2'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page2'
    sectionName = 'Experience1'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Page2.html", Context)


def page4(request):
    Context = {}

    pageName = 'Page4'
    sectionName = 'About1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'About1'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'About4'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'Featured1'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'About2'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'Callaction1'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page4'
    sectionName = 'Callaction2'
    sectionContextName = 'VAL007'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Page4.html", Context)


def page5(request):
    Context = {}

    pageName = 'Page5'
    sectionName = 'faq1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'Fluid1'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'Header1'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'Header2'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'Header3'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'Header4'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page5'
    sectionName = 'News1'
    sectionContextName = 'VAL007'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Page5.html", Context)


def page6(request):
    Context = {}

    pageName = 'Page6'
    sectionName = 'Pricing1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Process1'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Services1'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context
    pageName = 'Page6'
    sectionName = 'Services2'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Services3'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Shop1'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Shop2'
    sectionContextName = 'VAL007'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page6'
    sectionName = 'Shop3'
    sectionContextName = 'VAL008'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Page6.html", Context)


def page7(request):
    Context = {}

    pageName = 'Page7'
    sectionName = 'Sponsors1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Sponsors2'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Team1'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Team2'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Technology1'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Technology2'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Testimonial1'
    sectionContextName = 'VAL007'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Testimonial2'
    sectionContextName = 'VAL008'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Title1'
    sectionContextName = 'VAL009'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'Page7'
    sectionName = 'Title2'
    sectionContextName = 'VAL010'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Page7.html", Context)


def P00001(request):
    Context = {}

    pageName = 'P00001'
    sectionName = 'Header1'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Title1'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'News2'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Fluid2'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Cases1'
    sectionContextName = 'VAL006'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Technology2'
    sectionContextName = 'VAL007'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Team2'
    sectionContextName = 'VAL008'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Testimonial1'
    sectionContextName = 'VAL009'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Sponsors2'
    sectionContextName = 'VAL010'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00001'
    sectionName = 'Counter1'
    sectionContextName = 'VAL011'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Site/P00001.html", Context)


def P00002(request):
    Context = {}

    pageName = 'P00002'
    sectionName = 'Detail3'
    sectionContextName = 'VAL001'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00002'
    sectionName = 'Testimonial3'
    sectionContextName = 'VAL002'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00002'
    sectionName = 'Testimonial3'
    sectionContextName = 'VAL003'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00002'
    sectionName = 'Testimonial3'
    sectionContextName = 'VAL004'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    pageName = 'P00002'
    sectionName = 'Testimonial4'
    sectionContextName = 'VAL005'
    Context[sectionContextName] = Page.objects.get(name=pageName, section=sectionName,
                                                   contextName=sectionContextName).context

    return render(request, "./pages/Site/P00002.html", Context)


def P00004(request, pk):
    Context={}
    tbl = DBExec("Select * From Posts Where id =" + str(pk), 'Posts')
    if tbl:
        if len(tbl) == 1:
            data = tbl[0]['PostBody']
            if data:
                jsonData = json.loads(data)
                Context = jsonData
    return render(request, "./Posts/Models/Model1.html", Context)

def AddPostDB(request):
    if request.method == 'POST':
        form = PostsHeaderModel1(request.POST, None)
        if form.is_valid():
            cd = form.cleaned_data
            strCommand = "INSERT INTO Posts (SiteID, PostTitle) Values (N'"+"1234"+"',N'"+cd['PostTitle']+"')"
            DBExecCommand(strCommand, 'Posts')
            return redirect(AddPostDB)
            pass
    else:
        form = PostsHeaderModel1()
        Context={}
        Context['form'] = form
        return render(request, "./test.html", Context)

def EditPostDB(request, pk):
    if request.method == 'POST':
        form = PostsModel1(request.POST, None)
        if form.is_valid():
            cd = form.cleaned_data
            Context = {}
            Context['Items'] = {}
            Context['Items']['BG_IMG'] = cd['BG_IMG']
            Context['Items']['H1'] = cd['H1']
            Context['Items']['H2'] = cd['H2']
            Context['Items']['Title'] = cd['Title']
            Context['Items']['IMG'] = cd['IMG']
            strData = json.dumps(Context, indent=4)
            strCommand = "Update Posts Set PostBody =N'"+strData+"' where id = "+str(pk)
            DBExecCommand (strCommand, 'Posts')
            return redirect(EditPostDB, pk = pk)
    else:
        form = PostsModel1()
        tbl = DBExec("Select * From Posts Where id =" + str(pk), 'Posts')
        if tbl:
            if len(tbl) == 1:
                data = tbl[0]['PostBody']
                if data:
                    jsonData = json.loads(data)
                    form.fields['BG_IMG'].initial = jsonData['Items']['BG_IMG']
                    form.fields['H1'].initial = jsonData['Items']['H1']
                    form.fields['H2'].initial = jsonData['Items']['H2']
                    form.fields['Title'].initial = jsonData['Items']['Title']
                    form.fields['IMG'].initial = jsonData['Items']['IMG']
                else:
                    form.fields['H1'].initial = tbl[0]['PostTitle']
        else:
            pass
        Context={}
        Context['form'] = form
        return render(request, "./test.html", Context)

def AddPostDBItems(request, pk):
    if request.method == 'POST':
        form = PostsModel1_Items(request.POST, None)
        if form.is_valid():
            cd = form.cleaned_data
            tbl = DBExec("Select * From Posts Where id =" + str(pk), 'Posts')
            if tbl:
                if len(tbl) == 1:
                    data = tbl[0]['PostBody']
                    if data:
                        jsonData = json.loads(data)
                        try:
                            items = jsonData['Items']['Items']
                            item = {}
                            item['Header'] = cd['Header']
                            item['Text'] = cd['Text']
                            item['IMG'] = cd['IMG']
                            item['REFTEXT'] = cd['REFTEXT']
                            item['REFTEXT_REF'] = cd['REFTEXT_REF']
                            dt = datetime.now()
                            key = '{:04d}'.format(dt.year) + '{:02d}'.format(dt.month) + '{:02d}'.format(
                                dt.day) + '{:02d}'.format(dt.hour) + '{:02d}'.format(dt.minute) + '{:2d}'.format(
                                dt.second) + '{:06d}'.format(dt.microsecond)
                            pocketItem = {}
                            pocketItem['Key'] = key
                            pocketItem['Value'] = item
                            items.append(pocketItem)
                            strData = json.dumps(jsonData, indent=4)
                            strCommand = "Update Posts Set PostBody =N'" + strData + "' where id = " + str(pk)
                            DBExecCommand(strCommand, 'Posts')
                        except:
                            item = {}
                            item['Header'] = cd['Header']
                            item['Text'] = cd['Text']
                            item['IMG'] =  cd['IMG']
                            item['REFTEXT'] = cd['REFTEXT']
                            item['REFTEXT_REF'] = cd['REFTEXT_REF']
                            jsonData['Items']['Items'] = []
                            dt = datetime.now()
                            key = '{:04d}'.format(dt.year)+'{:02d}'.format(dt.month)+'{:02d}'.format(dt.day)+'{:02d}'.format(dt.hour)+'{:02d}'.format(dt.minute)+'{:2d}'.format(dt.second)+'{:06d}'.format(dt.microsecond)
                            pocketItem={}
                            pocketItem['Key'] = key
                            pocketItem['Value'] = item
                            jsonData['Items']['Items'].append(pocketItem)
                            strData = json.dumps(jsonData, indent=4)
                            strCommand = "Update Posts Set PostBody =N'" + strData + "' where id = " + str(pk)
                            DBExecCommand(strCommand, 'Posts')
                    else:
                        pass
        return redirect(AddPostDBItems, pk=pk)
    else:
        Context = {}
        Context['form']=PostsModel1_Items
        return render(request, "./test.html", Context)

def EditPostDBItems(request, pk, key):
    if request.method == 'POST':
        form = PostsModel1_Items(request.POST, None)
        if form.is_valid():
            cd = form.cleaned_data
            tbl = DBExec("Select * From Posts Where id =" + str(pk), 'Posts')
            if tbl:
                if len(tbl) == 1:
                    data = tbl[0]['PostBody']
                    if data:
                        jsonData = json.loads(data)
                        try:
                            Items = jsonData['Items']['Items']
                            for i in Items:
                                if i['Key'] == key:
                                    pocketItem = i['Value']
                                    pocketItem['Header'] = cd['Header']
                                    pocketItem['Text'] = cd['Text']
                                    pocketItem['IMG'] = cd['IMG']
                                    pocketItem['REFTEXT'] = cd['REFTEXT']
                                    pocketItem['REFTEXT_REF'] = cd['REFTEXT_REF']
                                    strData = json.dumps(jsonData, indent=4)
                                    strCommand = "Update Posts Set PostBody =N'" + strData + "' where id = " + str(pk)
                                    DBExecCommand(strCommand, 'Posts')
                                    return redirect(EditPostDBItems, pk=pk, key = key)
                                    break
                        except:
                            pass
        return redirect(EditPostDBItems, pk=pk, key=key)
    else:
        Context = {}
        Context['form']=PostsModel1_Items
        tbl = DBExec("Select * From Posts Where id =" + str(pk), 'Posts')
        if tbl:
            if len(tbl) == 1:
                data = tbl[0]['PostBody']
                if data:
                    jsonData = json.loads(data)
                    try:
                        Items = jsonData['Items']['Items']
                        for i in Items:
                            if i['Key'] == key:
                                form = PostsModel1_Items()
                                form.fields['Header'].initial = i['Value']['Header']
                                form.fields['Text'].initial = i['Value']['Text']
                                form.fields['IMG'].initial = i['Value']['IMG']
                                form.fields['REFTEXT'].initial = i['Value']['REFTEXT']
                                form.fields['REFTEXT_REF'].initial = i['Value']['REFTEXT_REF']
                                Context['form']=form
                                return render(request, "./test.html", Context)
                                break
                    except:
                        pass
        # show error page!!!!!
        print('err')
        return render(request, "./test.html", Context)



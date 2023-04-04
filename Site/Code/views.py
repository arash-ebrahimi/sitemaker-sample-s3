from django.shortcuts import redirect, render
from Site.Code.Code import *
from Site.Code.forms import *

def Page4_About1_VAL001(request):
    pageName = "Page4"
    sectionName = "About1"
    sectionContextName = "VAL001"
    myForm = About1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page4_About1_VAL002(request):
    pageName = "Page4"
    sectionName = "About1"
    sectionContextName = "VAL002"
    myForm = About1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page4_About4_VAL003(request):
    pageName = "Page4"
    sectionName = "About4"
    sectionContextName = "VAL003"
    myForm = About4

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})


def Page4_Featured1_VAL004(request):
    pageName = "Page4"
    sectionName = "Featured1"
    sectionContextName = "VAL004"
    myForm = Featured1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page4_About2_VAL005(request):
    pageName = "Page4"
    sectionName = "About2"
    sectionContextName = "VAL005"
    myForm = About2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page4_Callaction1_VAL006(request):
    pageName = "Page4"
    sectionName = "Callaction1"
    sectionContextName = "VAL006"
    myForm = Callaction1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page4_Callaction2_VAL007(request):
    pageName = "Page4"
    sectionName = "Callaction2"
    sectionContextName = "VAL007"
    myForm = Callaction1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Cases1_VAL001(request):
    pageName = "Page2"
    sectionName = "Cases1"
    sectionContextName = "VAL001"
    myForm = Cases1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Cases2_VAL002(request):
    pageName = "Page2"
    sectionName = "Cases2"
    sectionContextName = "VAL002"
    myForm = Cases1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Counter1_VAL003(request):
    pageName = "Page2"
    sectionName = "Counter1"
    sectionContextName = "VAL003"
    myForm = Counter1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Detail1_VAL004(request):
    pageName = "Page2"
    sectionName = "Detail1"
    sectionContextName = "VAL004"
    myForm = Detail1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Detail2_VAL005(request):
    pageName = "Page2"
    sectionName = "Detail2"
    sectionContextName = "VAL005"
    myForm = Detail2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page2_Experience1_VAL006(request):
    pageName = "Page2"
    sectionName = "Experience1"
    sectionContextName = "VAL006"
    myForm = Experience1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_faq1_VAL001(request):
    pageName = "Page5"
    sectionName = "faq1"
    sectionContextName = "VAL001"
    myForm = faq1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_Fluid1_VAL002(request):
    pageName = "Page5"
    sectionName = "Fluid1"
    sectionContextName = "VAL002"
    myForm = Fluid1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_Header1_VAL003(request):
    pageName = "Page5"
    sectionName = "Header1"
    sectionContextName = "VAL003"
    myForm = Header1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_Header2_VAL004(request):
    pageName = "Page5"
    sectionName = "Header2"
    sectionContextName = "VAL004"
    myForm = Header1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_Header3_VAL005(request):
    pageName = "Page5"
    sectionName = "Header3"
    sectionContextName = "VAL005"
    myForm = Header3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_Header4_VAL006(request):
    pageName = "Page5"
    sectionName = "Header4"
    sectionContextName = "VAL006"
    myForm = Header4

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page5_News1_VAL007(request):
    pageName = "Page5"
    sectionName = "News1"
    sectionContextName = "VAL007"
    myForm = News1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Pricing1_VAL001(request):
    pageName = "Page6"
    sectionName = "Pricing1"
    sectionContextName = "VAL001"
    myForm = Pricing1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Process1_VAL002(request):
    pageName = "Page6"
    sectionName = "Process1"
    sectionContextName = "VAL002"
    myForm = Process1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Services1_VAL003(request):
    pageName = "Page6"
    sectionName = "Services1"
    sectionContextName = "VAL003"
    myForm = Services1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Services2_VAL004(request):
    pageName = "Page6"
    sectionName = "Services2"
    sectionContextName = "VAL004"
    myForm = Services2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Services3_VAL005(request):
    pageName = "Page6"
    sectionName = "Services3"
    sectionContextName = "VAL005"
    myForm = Services3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Shop1_VAL006(request):
    pageName = "Page6"
    sectionName = "Shop1"
    sectionContextName = "VAL006"
    myForm = Shop1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Shop2_VAL007(request):
    pageName = "Page6"
    sectionName = "Shop2"
    sectionContextName = "VAL007"
    myForm = Shop2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page6_Shop3_VAL008(request):
    pageName = "Page6"
    sectionName = "Shop3"
    sectionContextName = "VAL008"
    myForm = Shop3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Sponsors1_VAL001(request):
    pageName = "Page7"
    sectionName = "Sponsors1"
    sectionContextName = "VAL001"
    myForm = Sponsors1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Sponsors2_VAL002(request):
    pageName = "Page7"
    sectionName = "Sponsors2"
    sectionContextName = "VAL002"
    myForm = Sponsors1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Team1_VAL003(request):
    pageName = "Page7"
    sectionName = "Team1"
    sectionContextName = "VAL003"
    myForm = Team1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Team2_VAL004(request):
    pageName = "Page7"
    sectionName = "Team2"
    sectionContextName = "VAL004"
    myForm = Team2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Technology1_VAL005(request):
    pageName = "Page7"
    sectionName = "Technology1"
    sectionContextName = "VAL005"
    myForm = Technology1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Technology2_VAL006(request):
    pageName = "Page7"
    sectionName = "Technology2"
    sectionContextName = "VAL006"
    myForm = Technology2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Testimonial1_VAL007(request):
    pageName = "Page7"
    sectionName = "Testimonial1"
    sectionContextName = "VAL007"
    myForm = Testimonial1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Testimonial2_VAL008(request):
    pageName = "Page7"
    sectionName = "Testimonial2"
    sectionContextName = "VAL008"
    myForm = Testimonial2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Title1_VAL009(request):
    pageName = "Page7"
    sectionName = "Title1"
    sectionContextName = "VAL009"
    myForm = Title1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def Page7_Title2_VAL010(request):
    pageName = "Page7"
    sectionName = "Title2"
    sectionContextName = "VAL010"
    myForm = Title2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './componentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Header1_VAL001(request):
    pageName = "P00001"
    sectionName = "Header1"
    sectionContextName = "VAL001"
    myForm = Header1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Title1_VAL002(request):
    pageName = "P00001"
    sectionName = "Title1"
    sectionContextName = "VAL002"
    myForm = Title1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_News2_VAL004(request):
    pageName = "P00001"
    sectionName = "News2"
    sectionContextName = "VAL004"
    myForm = News2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Fluid2_VAL005(request):
    pageName = "P00001"
    sectionName = "Fluid2"
    sectionContextName = "VAL005"
    myForm = Fluid2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Cases1_VAL006(request):
    pageName = "P00001"
    sectionName = "Cases1"
    sectionContextName = "VAL006"
    myForm = Cases1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Technology2_VAL007(request):
    pageName = "P00001"
    sectionName = "Technology2"
    sectionContextName = "VAL007"
    myForm = Technology2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Team2_VAL008(request):
    pageName = "P00001"
    sectionName = "Team2"
    sectionContextName = "VAL008"
    myForm = Team2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Testimonial1_VAL009(request):
    pageName = "P00001"
    sectionName = "Testimonial1"
    sectionContextName = "VAL009"
    myForm = Testimonial1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00001_Sponsors2_VAL010(request):
    pageName = "P00001"
    sectionName = "Sponsors2"
    sectionContextName = "VAL010"
    myForm = Sponsors2

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})


def P00001_Counter1_VAL011(request):
    pageName = "P00001"
    sectionName = "Counter1"
    sectionContextName = "VAL011"
    myForm = Counter1

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})


def P00002_Detail3_VAL001(request):
    pageName = "P00002"
    sectionName = "Detail3"
    sectionContextName = "VAL001"
    myForm = Detail3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})


def P00002_Testimonial3_VAL002(request):
    pageName = "P00002"
    sectionName = "Testimonial3"
    sectionContextName = "VAL002"
    myForm = Testimonial3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00002_Testimonial3_VAL003(request):
    pageName = "P00002"
    sectionName = "Testimonial3"
    sectionContextName = "VAL003"
    myForm = Testimonial3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00002_Testimonial3_VAL004(request):
    pageName = "P00002"
    sectionName = "Testimonial3"
    sectionContextName = "VAL004"
    myForm = Testimonial3

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})

def P00002_Testimonial4_VAL005(request):
    pageName = "P00002"
    sectionName = "Testimonial4"
    sectionContextName = "VAL005"
    myForm = Testimonial4

    if request.method == 'POST':
        post_Method(request,pageName,sectionName,sectionContextName,myForm)
        return redirect(pageName + "_" + sectionName + "_" + sectionContextName)
    else:
        return render(request, './PagesComponentsDEF/def.html', {
            'form': get_Method(request,pageName,sectionName,sectionContextName,myForm)})


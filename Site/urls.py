from . import views
from .Code.views import *
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home1"),
    path('Page2', views.page2, name="Page2"),
    path('Page4', views.page4, name="Page4"),
    path('Page5', views.page5, name="Page5"),
    path('Page6', views.page6, name="Page6"),
    path('Page7', views.page7, name="Page7"),


    path('Page2_Cases1_VAL001', Page2_Cases1_VAL001, name="Page2_Cases1_VAL001"),
    path('Page2_Cases2_VAL002', Page2_Cases2_VAL002, name="Page2_Cases2_VAL002"),
    path('Page2_Counter1_VAL003', Page2_Counter1_VAL003, name="Page2_Counter1_VAL003"),
    path('Page2_Detail1_VAL004', Page2_Detail1_VAL004, name="Page2_Detail1_VAL004"),
    path('Page2_Detail2_VAL005', Page2_Detail2_VAL005, name="Page2_Detail2_VAL005"),
    path('Page2_Experience1_VAL006', Page2_Experience1_VAL006, name="Page2_Experience1_VAL006"),

    path('Page4_About1_VAL001', Page4_About1_VAL001, name="Page4_About1_VAL001"),
    path('Page4_About1_VAL002', Page4_About1_VAL002, name="Page4_About1_VAL002"),
    path('Page4_About4_VAL003', Page4_About4_VAL003, name="Page4_About4_VAL003"),
    path('Page4_Featured1_VAL004', Page4_Featured1_VAL004, name="Page4_Featured1_VAL004"),
    path('Page4_About2_VAL005', Page4_About2_VAL005, name="Page4_About2_VAL005"),
    path('Page4_Callaction1_VAL006', Page4_Callaction1_VAL006, name="Page4_Callaction1_VAL006"),
    path('Page4_Callaction2_VAL007', Page4_Callaction2_VAL007, name="Page4_Callaction2_VAL007"),

    path('Page5_faq1_VAL001', Page5_faq1_VAL001, name="Page5_faq1_VAL001"),
    path('Page5_Fluid1_VAL002', Page5_Fluid1_VAL002, name="Page5_Fluid1_VAL002"),
    path('Page5_Header1_VAL003', Page5_Header1_VAL003, name="Page5_Header1_VAL003"),
    path('Page5_Header2_VAL004', Page5_Header2_VAL004, name="Page5_Header2_VAL004"),
    path('Page5_Header3_VAL005', Page5_Header3_VAL005, name="Page5_Header3_VAL005"),
    path('Page5_Header4_VAL006', Page5_Header4_VAL006, name="Page5_Header4_VAL006"),
    path('Page5_News1_VAL007', Page5_News1_VAL007, name="Page5_News1_VAL007"),

    path('Page6_Pricing1_VAL001', Page6_Pricing1_VAL001, name="Page6_Pricing1_VAL001"),
    path('Page6_Process1_VAL002', Page6_Process1_VAL002, name="Page6_Process1_VAL002"),
    path('Page6_Services1_VAL003', Page6_Services1_VAL003, name="Page6_Services1_VAL003"),
    path('Page6_Services2_VAL004', Page6_Services2_VAL004, name="Page6_Services2_VAL004"),
    path('Page6_Services3_VAL005', Page6_Services3_VAL005, name="Page6_Services3_VAL005"),
    path('Page6_Shop1_VAL006', Page6_Shop1_VAL006, name="Page6_Shop1_VAL006"),
    path('Page6_Shop2_VAL007', Page6_Shop2_VAL007, name="Page6_Shop2_VAL007"),
    path('Page6_Shop3_VAL008', Page6_Shop3_VAL008, name="Page6_Shop3_VAL008"),

    path('Page7_Sponsors1_VAL001', Page7_Sponsors1_VAL001, name="Page7_Sponsors1_VAL001"),
    path('Page7_Sponsors2_VAL002', Page7_Sponsors2_VAL002, name="Page7_Sponsors2_VAL002"),
    path('Page7_Team1_VAL003', Page7_Team1_VAL003, name="Page7_Team1_VAL003"),
    path('Page7_Team2_VAL004', Page7_Team2_VAL004, name="Page7_Team2_VAL004"),
    path('Page7_Technology1_VAL005', Page7_Technology1_VAL005, name="Page7_Technology1_VAL005"),
    path('Page7_Technology2_VAL006', Page7_Technology2_VAL006, name="Page7_Technology2_VAL006"),
    path('Page7_Testimonial1_VAL007', Page7_Testimonial1_VAL007, name="Page7_Testimonial1_VAL007"),
    path('Page7_Testimonial2_VAL008', Page7_Testimonial2_VAL008, name="Page7_Testimonial2_VAL008"),
    path('Page7_Title1_VAL009', Page7_Title1_VAL009, name="Page7_Title1_VAL009"),
    path('Page7_Title2_VAL010', Page7_Title2_VAL010, name="Page7_Title2_VAL010"),


    path('uploadimages', views.UPLOADImages, name="uploadimages"),
    path('imageDirManager/<int:pk>/', views.imageDirManager, name="imageDirManager"),
    path('addDirectory/<int:pk>/', views.addDirectory, name="addDirectory"),
    path('editDirectory/<int:pk>/', views.editDirectory, name="editDirectory"),
    path('deleteDirectory/<int:pk>/', views.deleteDirectory, name="deleteDirectory"),
    path('showUploadImage/<int:pk>', views.showUploadImage, name="showUploadImage"),

    path('P00001', views.P00001, name="P00001"),
    path('P00001_Header1_VAL001', P00001_Header1_VAL001, name="P00001_Header1_VAL001"),
    path('P00001_Title1_VAL002', P00001_Title1_VAL002, name="P00001_Title1_VAL002"),
    path('P00001_News2_VAL004', P00001_News2_VAL004, name="P00001_News2_VAL004"),
    path('P00001_Fluid2_VAL005', P00001_Fluid2_VAL005, name="P00001_Fluid2_VAL005"),
    path('P00001_Cases1_VAL006', P00001_Cases1_VAL006, name="P00001_Cases1_VAL006"),
    path('P00001_Technology2_VAL007', P00001_Technology2_VAL007, name="P00001_Technology2_VAL007"),
    path('P00001_Team2_VAL008', P00001_Team2_VAL008, name="P00001_Team2_VAL008"),
    path('P00001_Testimonial1_VAL009', P00001_Testimonial1_VAL009, name="P00001_Testimonial1_VAL009"),
    path('P00001_Sponsors2_VAL010', P00001_Sponsors2_VAL010, name="P00001_Sponsors2_VAL010"),
    path('P00001_Counter1_VAL011', P00001_Counter1_VAL011, name="P00001_Counter1_VAL011"),

    path('P00002', views.P00002, name="P00002"),
    path('P00002_Detail3_VAL001', P00002_Detail3_VAL001, name="P00002_Detail3_VAL001"),
    path('P00002_Testimonial3_VAL002', P00002_Testimonial3_VAL002, name="P00002_Testimonial3_VAL002"),
    path('P00002_Testimonial3_VAL003', P00002_Testimonial3_VAL003, name="P00002_Testimonial3_VAL003"),
    path('P00002_Testimonial3_VAL004', P00002_Testimonial3_VAL004, name="P00002_Testimonial3_VAL004"),
    path('P00002_Testimonial4_VAL005', P00002_Testimonial4_VAL005, name="P00002_Testimonial4_VAL005"),


    path('P00004/<int:pk>', views.P00004, name="P00004"),
    path('AddPostDB', views.AddPostDB, name="AddPostDB"),
    path('EditPostDB/<int:pk>', views.EditPostDB, name="EditPostDB"),
    path('AddPostDBItems/<int:pk>', views.AddPostDBItems, name="AddPostDBItems"),
    path('EditPostDBItems/<int:pk>/<str:key>', views.EditPostDBItems, name="EditPostDBItems"),

    path('dashboard', views.dashboard, name="dashboard"),

]
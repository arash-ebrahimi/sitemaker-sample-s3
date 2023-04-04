from django import forms
from Site.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('picture_addr',)

class PostsHeaderModel1(forms.Form):
    PostTitle = forms.CharField(required=True)

class PostsModel1(forms.Form):
    BG_IMG = forms.CharField(required=False)
    H1 = forms.CharField(required=True)
    H2 = forms.CharField(required=False)
    Title = forms.CharField(widget=forms.Textarea,   required=False)
    IMG = forms.CharField(required=False)

class PostsModel1_Items(forms.Form):
    Header = forms.CharField(required=True)
    Text =  forms.CharField(widget=forms.Textarea,   required=False)
    IMG = forms.CharField(required=False)
    REFTEXT =forms.CharField(required=False)
    REFTEXT_REF = forms.CharField(required=False)


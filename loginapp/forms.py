from django import forms


class UploadFileForm(forms.Form):
    object = forms.CharField(max_length=50)
    thumbnail = forms.ImageField()
    video = forms.FileField()
    userId = forms.FileField()
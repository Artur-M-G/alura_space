from django import forms
from photography_api.models import Photography

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published', 'date', ]
        labels = {
            'name': 'Nome',
            'subtitle': 'Subtitle',
            'category': 'Category',
            'description': 'Description',
            'photo': 'Photo',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'subtitle' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'photo' : forms.FileInput(attrs={'class':'form-control'}),
        }

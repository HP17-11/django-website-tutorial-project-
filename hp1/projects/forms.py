from django.forms import ModelForm, widgets 
from django import forms 
from .models import Project

class Projectform(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demolink','sourcecode','tags']
        widgets = { 
                'tags' : forms.CheckboxSelectMultiple(),
                    }
        
        
    def __init__( self, *args, **kwargs):
        super(Projectform,self).__init__(*args,**kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

'''     self.fields['title'].widget.attrs.update(
            {"class": 'input', "placeholder" : "add title"}
        )

        self.fields['description'].widget.attrs.update(
            {"class": 'input'}
        ) '''
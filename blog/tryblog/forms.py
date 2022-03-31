from unicodedata import category
from django import forms
from .models import Post,Category
# harcode (static) 
# choices = [('coding','coding'), ('sports','sports'), ('entertainment','entertainment')]
# add it in category (choices = choices ,attrs...)
#.. ,'placeholder':choices in title(textbox to check what is returning from database)
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title','title_tag','author','category','body','snippet','header_image')
# Form la using ModelFrom method it ca be changed to normal form also if don't have an model,
# widegts used to put attributes or fields 
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices = choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            
            'snippet':forms.Textarea(attrs={'class':'form-control'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title','title_tag','body','snippet','header_image')
# Form la using ModelFrom method it ca be changed to normal form also if don't have an model,
# widegts used to put attributes or fields 
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),

            

        }

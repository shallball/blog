from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
	class Meta:
		model=BlogPost
		fields=['title','text']
		labels={'title':'标题',"text":''}		
		widgets={'text':forms.Textarea(attrs={'cols':80})}

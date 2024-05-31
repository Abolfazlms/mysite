from django import forms
from blog.models import Comments

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['post', 'name','email','subject','message']
        # fields = ['name','email']
        #exclude = ['name]

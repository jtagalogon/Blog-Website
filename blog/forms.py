from django import forms

class NewPost(forms.Form):
    new_title = forms.CharField(label='Title', max_length=100)
    new_body = forms.CharField(label='Body')

# Needed to save the user input when creating posts.

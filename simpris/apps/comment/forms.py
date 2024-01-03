__author__ = 'Graham'

from django import forms

class CommentForm(forms.Form):
    frmTextComment = forms.CharField(label='Comment text', max_length=5000)
    hidParentID = forms.CharField(label='Parent ID')
    hidParentType = forms.CharField(label='Parent Type')
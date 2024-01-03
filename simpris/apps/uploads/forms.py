__author__ = 'Graham'


from django import forms

class DocumentForm(forms.Form):
    frmUserFile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    hidItemType = forms.CharField(label='Item type')
    hidItemID = forms.CharField(label='Item ID')
    hidParentID = forms.CharField(label='Item Parent ID',required=False)
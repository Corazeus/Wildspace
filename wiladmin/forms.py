from django import forms


class BookGuest(forms.Form):
    userid = forms.CharField(label="userid", max_length=100)
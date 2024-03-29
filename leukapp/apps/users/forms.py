from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first name')
    last_name = forms.CharField(max_length=30, label='last name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

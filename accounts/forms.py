from django import forms
from .models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        
    
    ''' clean method== django model forms by default calls the clean method behind the scenes whenever the form is triggered
    this will actually make your data clean by using some inbuilt functions such as to_python(), validate(),and run_validaters() '''
    # here we are overwritting the cleaned method for checking the password as matching
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(      # this validation error is called non field errors
                "Password does not match!"
            )
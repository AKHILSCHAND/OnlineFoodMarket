from django import forms
from .models import User,UserProfile
from .validators import allow_only_images_validator



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
            

class UserProfileForm(forms.ModelForm):

    # profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}))
    # cover_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}))
    
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Start typing...', 'required': 'required'}))
    # if we are using custom validator, change the ImageField to FileField otherwise it wont work
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    
    # making read only form for latitude and longitude
    
    # latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude']
        
    # another way of making read only form for latitude and longitude    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'latitude' or field == 'longitude':
                self.fields[field].widget.attrs['readonly'] = 'readonly'
from django.forms import ModelForm
from django import forms
from .models import Review, Restaurant
from django import forms
from .models import Restaurant, Facility, DayOpen, Image
from django.forms import ModelForm, TimeInput
from .models import Restaurant


class ReviewAdd(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'value']

    def __init__(self, *args, **kwargs):
        super(ReviewAdd, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': str(name).capitalize()})


# forms.py

# forms.py

from django import forms
from .models import Restaurant, Image  # Import Image model
from users.models import Profile


class RestaurantAddForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'small_description', 'website', 'main_image', 'seats', 'open_from', 'open_to',
                  'large_description']

    def __init__(self, *args, **kwargs):
        super(RestaurantAddForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': str(name).capitalize()})


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': str(name).capitalize()})


class CustomFacilityForm(forms.Form):
    facility_name = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(CustomFacilityForm, self).__init__(*args, **kwargs)
        self.fields['facility_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Facility Name'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': str(name).capitalize()})



class RestaurantFilterForm(forms.Form):
    facilities = forms.ModelMultipleChoiceField(queryset=Facility.objects.all(), required=False,
                                                widget=forms.CheckboxSelectMultiple)
    open_days = forms.ModelMultipleChoiceField(queryset=DayOpen.objects.all(), required=False,
                                               widget=forms.CheckboxSelectMultiple)
    # Add fields for open and close times or any other criteria you want to filter by

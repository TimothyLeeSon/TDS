from django import forms
from django.forms import ModelForm
from .models import Person

from django.core.validators import RegexValidator

# Create your forms
class InputForm(ModelForm):
    class Meta:
        # Name of model for form
        model = Person

        # Custom fields
        fields = ["first_name", "last_name", "date_of_birth"]

    # Validation function
    def clean(self):
        # Super function retrieves data from the form
        super(InputForm, self).clean()

        # Retrieve the firstname and lastname
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        # Conditions
        if first_name.isalpha() != True:
            self._errors["first_name"] = self.error_class(["Only letters allowed in a first name"])

        if last_name.isalpha() != True:
            self._errors["last_name"] = self.error_class(["Only letters allowed in a last name"])
        
        # Return any errors found
        return self.cleaned_data

    #year_range = [x for x in range(1940, 2021)]
    #date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=year_range))
    date_of_birth = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))




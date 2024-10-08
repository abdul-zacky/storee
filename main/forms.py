from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        cleaned_name = strip_tags(name)  # Strip any HTML tags from the input

        if not cleaned_name.strip():
            raise ValidationError('Name cannot be blank or contain only invalid content.')

        return cleaned_name
    
    def clean_desc(self):
        description = self.cleaned_data["description"]
        cleaned_description = strip_tags(description)

        if not cleaned_description.strip():
            raise ValidationError('Description cannot be blank or contain only invalid content.')

        return cleaned_description
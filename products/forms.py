from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    """Form for admin adding flowers to website"""
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    avgRating = forms.FloatField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-corners'


class ReviewForm(forms.ModelForm):
    """Form for product reviews"""
    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels.
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Write a review..',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['title'] = 'Review content'
            self.fields[field].label = False

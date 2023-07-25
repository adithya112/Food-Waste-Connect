from django.forms import ModelForm
from .models import Food

class FoodModelForm(ModelForm):
    class Meta:
        model = Food
        fields = [
            'food_name',
            'contact',
            'description',
            'feed',
            'food_type',
            'cooked_time',
            'address',
            'user'
        ]
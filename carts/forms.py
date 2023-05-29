from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_option']
        labels = {
            'delivery_option': 'Método de entrega',
        }
        
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '') 
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': ''}
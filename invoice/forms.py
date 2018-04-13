from django import forms
from django.forms.models import inlineformset_factory

from .models import Invoice, InvoiceDetail


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'


InvoiceDetailFormSet = inlineformset_factory(Invoice, InvoiceDetail, extra=0, min_num=1, fields='__all__')

from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import Select

from .models import Item, Invoice, InvoiceDetail


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('customer',)


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = ('item', 'quantity',)

    def __init__(self, *args, **kwargs):
        super(InvoiceDetailForm, self).__init__(*args, **kwargs)

        self.fields['item'].choices = lambda: [('', '-- 商品 --')] + [
            (item.id, '%s %s円' % (item.name.ljust(10, '　'), item.unit_price)) for item in
            Item.objects.order_by('order')]

        choices_number = [('', '-- 個数 --')] + [(str(i), str(i)) for i in range(1, 10)]
        self.fields['quantity'].widget = Select(choices=choices_number)


InvoiceDetailFormSet = inlineformset_factory(
    parent_model=Invoice,
    model=InvoiceDetail,
    form=InvoiceDetailForm,
    extra=1,
    min_num=1,
    validate_min=True,
)

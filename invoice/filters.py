from django.contrib.auth.models import User
from django_filters import FilterSet
from django_filters import filters

from .models import Invoice


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class InvoiceFilter(FilterSet):
    customer = filters.CharFilter(name='customer', label='顧客名', lookup_expr='contains')
    created_by = filters.ChoiceFilter(name='created_by', label='担当者',
                                      choices=
                                      lambda: [(user.id, user.get_full_name()) for user in
                                               User.objects.all()])

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('created_at', 'created_at'),
        ),
        field_labels={
            'created_at': '登録時間',
        },
        label='並び順'
    )

    class Meta:
        model = Invoice
        fields = ('customer', 'created_by',)

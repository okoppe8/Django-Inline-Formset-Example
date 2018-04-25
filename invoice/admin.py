from django.contrib import admin

from .models import Item, Invoice, InvoiceDetail


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'order',)
    list_editable = ('unit_price', 'order',)
    ordering = ('order',)


class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]

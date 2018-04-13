from django.contrib import admin

from .models import ItemGroup, Item, Invoice, InvoiceDetail


@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 3


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]

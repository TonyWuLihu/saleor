from django import forms
from django.utils.translation import pgettext_lazy

from ...site.models import SiteSettings


class TaxesConfigurationForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = (
            'include_taxes_in_prices', 'display_gross_prices',
            'charge_taxes_on_shipping')
        labels = {
            'include_taxes_in_prices': pgettext_lazy(
                'Include taxes in prices',
                'All taxes are included in my prices'),
            'display_gross_prices': pgettext_lazy(
                'Display gross prices',
                'Show customers gross prices in storefront'),
            'charge_taxes_on_shipping': pgettext_lazy(
                'Charge taxes on shipping rates',
                'Charge taxes on shipping rates')}

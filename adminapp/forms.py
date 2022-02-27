from django import forms

from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = (
            "avatar",
            "username",
            "first_name",
            "last_name",
            "email",
            "age",
            "activation_key",
            "activation_key_expires",
            "last_login",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
        )


class ProductCategoryEditForm(forms.ModelForm):
    discount = forms.IntegerField(label="скидка", required=False, min_value=0, max_value=90, initial=0)
    extra_charge = forms.IntegerField(label="наценка", required=False, min_value=0, max_value=90, initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = Product
        fields = "__all__"

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django.forms import ModelChoiceField, ModelForm, ValidationError

from PIL import Image


class LaptopAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Минимальное разрешение для изображения {}x{}</span>'.format(
                *Product.min_resolution
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.min_resolution
        max_height, max_width = Product.max_resolution
        if image.size > Product.max_image_size:
            raise ValidationError('Размер изображения не должен превышать 3мб')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображения больше максимального')
        return image


class LaptopAdmin(admin.ModelAdmin):

    form = LaptopAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
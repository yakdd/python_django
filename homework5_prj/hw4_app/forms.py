from django import forms


class ProductEditForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена')
    product_count = forms.IntegerField(label='Количество на складе')
    added_at = forms.DateField(widget=forms.DateInput, label='Дата добавления')


class ImageForm(forms.Form):
    image = forms.ImageField()

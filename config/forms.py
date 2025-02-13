from django import forms
from django.forms.fields import Field


class StyleFormMixin:
    fields: dict[str, Field]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

            if isinstance(field.widget, forms.widgets.DateTimeInput):
                field.widget.input_type = 'datetime-local'

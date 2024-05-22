# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from tlp.admin import widgets as admin_widgets
from django.db import models

from tinymce import widgets as tinymce_widgets


class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """
    def __init__(self, *args, **kwargs):
        self.tinymce_config = kwargs.pop("tinymce_config", None)
        super(HTMLField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'widget': tinymce_widgets.TinyMCE,
            'form_class': self._get_form_class(),
        }
        if self.tinymce_config:
            defaults["tinymce_config"] = self.tinymce_config.copy()
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE

        return super().formfield(**defaults)

    @staticmethod
    def _get_form_class():
        return HTMLFormField


class HTMLFormField(forms.fields.CharField):

    def __init__(
        self,
        tinymce_config=None,
        *args,
        **kwargs
    ):
        kwargs.update(
            {
                "widget": kwargs["widget"](mce_attrs=tinymce_config)
            }
        )
        super().__init__(*args, **kwargs)

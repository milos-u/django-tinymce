import os
from django.conf import settings

DEFAULT_CONFIG = getattr(
    settings,
    "TINYMCE_DEFAULT_CONFIG",
    {
        "theme": "silver",
        "height": 500,
        "menubar": False,
        "browser_spellcheck": True,
        "plugins": "advlist,autolink,lists,link,image,charmap,preview,anchor,"
        "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,"
        "help,wordcount",
        "toolbar": "undo redo | formatselect | "
        "bold italic backcolor | alignleft aligncenter "
        "alignright alignjustify | bullist numlist outdent indent | "
        "removeformat | help",
    },
)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_EXTRA_MEDIA = getattr(settings, 'TINYMCE_EXTRA_MEDIA', None)

USE_FILEBROWSER = getattr(
    settings, "TINYMCE_FILEBROWSER", "filebrowser" in settings.INSTALLED_APPS
)

JS_URL = getattr(settings, 'TINYMCE_JS_URL', os.path.join(settings.STATIC_URL, 'tinymce/tinymce.min.js'))

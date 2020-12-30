import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe
from django_jinja import library

from cabins import __version__


@library.filter
def dump(obj, id, var):
    data = mark_safe(json.dumps(obj))
    return mark_safe(f"<script type='text/javascript' id={id}>var {var} = {data}</script>")


@library.global_function
def static_version(path):
    file, extension = path.split(".")
    path = f"{file}.{__version__}.{extension}"
    return staticfiles_storage.url(path)

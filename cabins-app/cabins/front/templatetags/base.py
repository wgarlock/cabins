import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe
from django_jinja import library

from cabins import __version__


@library.global_function
def context_dump(var, *args):
    data = dict()
    [data.update(arg) for arg in args]
    data = mark_safe(json.dumps(data))
    return mark_safe(f"<script type='text/javascript'>var {var} = {data}</script>")


@library.global_function
def static_version(path):
    file, extension = path.split(".")
    path = f"{file}.{__version__}.{extension}"
    return staticfiles_storage.url(path)

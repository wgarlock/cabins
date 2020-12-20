import json
from django.utils.safestring import mark_safe
from django_jinja import library


@library.filter
def dump(obj, id, var):
    data = mark_safe(json.dumps(obj))
    return mark_safe(f"<script type='text/javascript' id={id}>var {var} = {data}</script>")

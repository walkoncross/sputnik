import shutil
import json
import io
import os


def is_enough_space(path, size):
    if hasattr(shutil, "disk_usage"):  # python >= 3.3
        free = shutil.disk_usage(path).free
        return free >= size
    return True


def archive_filename(name, version, suffix=False):
    res = "%s-%s" % (name, version)
    if suffix:
        res += ".shuttle"
    return res


def json_dump(obj):
    defaults = {'sort_keys': True, 'indent': 2, 'separators': (',', ': ')}
    return json.dumps(obj, **defaults).encode('utf8')


def json_load(path):
    with io.open(path, "rb") as f:
        return json.loads(f.read().decode('utf8'))


def json_print(obj):
    defaults = {'sort_keys': True, 'indent': 2, 'separators': (',', ': ')}
    print(json.dumps(obj, **defaults))


def makedirs(path):
    path = os.path.dirname(path)
    if path and not os.path.exists(path):
        os.makedirs(path)


def unquote(s):
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

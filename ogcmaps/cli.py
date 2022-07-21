import importlib

import click

from ogcmaps.utils.components import get_funcs

"""
class Context(object):

    def __init__(self):
        self.pretty_print = False

pass_context = click.make_pass_decorator(Context, ensure=True)
"""


class OGCmapsCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = get_funcs(["collections", "conformance", "map", "styles", "landing"])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = importlib.import_module("ogcmaps.utils.commands")
            return getattr(mod, name)
        except Exception:
            return ctx.fail(f"No such command: {name}")


@click.command(cls=OGCmapsCLI)
@click.option("-p", "--prettify", is_flag=True, help="Pretty print the JSON response")
@click.pass_context
def cli(ctx, prettify):
    """
    Python client for OGC Maps API.
    Read more at https://github.com/52North/api-maps-client
    """
    if ctx.obj is None:
        ctx.obj = dict()
    ctx.obj["pretty_print"] = prettify

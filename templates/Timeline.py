# coding=utf-8
from pychroner import PluginMeta, PluginType

@PluginMeta(PluginType.Timeline, account="UniqueName")
def do(pluginApi, stream):
    """
    :param pluginApi: pluginApi object.
    :param stream: Twitter UserStream Json Dict.
    """
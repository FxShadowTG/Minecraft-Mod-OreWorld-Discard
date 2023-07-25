# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModH7JazwDS", version="0.0.1")
class Script_NeteaseModH7JazwDS(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModH7JazwDSServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModH7JazwDSServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModH7JazwDSClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModH7JazwDSClientDestroy(self):
        pass

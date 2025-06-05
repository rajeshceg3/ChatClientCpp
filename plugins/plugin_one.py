from plugin_interface import AppPlugin

class PluginOne(AppPlugin):
    def execute(self):
        print("Executing PluginOne: Hello from the first plugin!")

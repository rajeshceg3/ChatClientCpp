from plugin_interface import AppPlugin

class PluginTwo(AppPlugin):
    def execute(self):
        print("Executing PluginTwo: Greetings from the second plugin!")

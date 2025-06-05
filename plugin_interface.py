from abc import ABC, abstractmethod

class AppPlugin(ABC):
    """
    Base class for all plugins.
    Plugins should inherit from this class and implement the execute method.
    """

    @abstractmethod
    def execute(self):
        """
        The main execution method for the plugin.
        This method will be called by the application when the plugin is loaded.
        """
        pass

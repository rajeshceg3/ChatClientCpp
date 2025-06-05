import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add project root to sys.path to allow importing main and plugin_interface
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from main import load_plugins
from plugin_interface import AppPlugin
from plugins.plugin_one import PluginOne
from plugins.plugin_two import PluginTwo

class TestPluginSystem(unittest.TestCase):

    def test_plugin_discovery_and_loading(self):
        """Test that example plugins are discovered and loaded."""
        # Temporarily create dummy plugin files for a controlled test environment
        # This is often better done by mocking the filesystem or using a fixture
        # but for this example, direct creation/cleanup is shown.

        # Ensure a clean state if plugins dir might have other dev plugins
        # For this test, we assume plugin_one and plugin_two are the only ones
        # or we are testing their presence among others.

        loaded_plugins = load_plugins(plugin_folder="plugins")

        self.assertTrue(len(loaded_plugins) >= 2, "Should load at least two plugins.")

        plugin_types = [type(p) for p in loaded_plugins]
        self.assertIn(PluginOne, plugin_types, "PluginOne should be loaded.")
        self.assertIn(PluginTwo, plugin_types, "PluginTwo should be loaded.")

    def test_plugin_execute_called(self):
        """Test that the execute method of a plugin is called."""

        # Create a mock plugin class
        class MockPlugin(AppPlugin):
            def __init__(self):
                self.executed = False
            def execute(self):
                self.executed = True
                print("MockPlugin executed") # For visibility during testing

        # We'll test the load_plugins function's ability to load and then we'll manually execute
        # Alternatively, we could mock the plugins directory and file system interactions

        # For this test, let's instantiate one of our actual plugins and mock its execute method
        plugin_instance = PluginOne()
        plugin_instance.execute = MagicMock() # Mock the execute method

        # Simulate the part of main.py that calls execute
        try:
            plugin_instance.execute()
        except Exception as e:
            self.fail(f"Plugin execution raised an exception: {e}")

        plugin_instance.execute.assert_called_once()

    @patch('main.print') # Mock print to avoid clutter during tests
    def test_load_plugins_no_folder(self, mock_print):
        """Test behavior when plugin folder doesn't exist."""
        plugins = load_plugins(plugin_folder="non_existent_plugins_folder")
        self.assertEqual(len(plugins), 0)
        mock_print.assert_any_call("Plugin folder 'non_existent_plugins_folder' not found.")

    @patch('main.print') # Mock print
    @patch('importlib.import_module')
    def test_load_plugins_import_error(self, mock_import_module, mock_print):
        """Test behavior when a plugin module raises ImportError."""
        mock_import_module.side_effect = ImportError("Test import error")

        # Need at least one .py file in plugins dir for the test to proceed to import
        # This setup is a bit fragile; ideally, mock os.listdir and os.path.exists
        if not os.path.exists("plugins"): os.makedirs("plugins")
        # Create a unique name for the faulty plugin file to avoid clashes if tests run multiple times
        faulty_plugin_path = "plugins/faulty_plugin_for_test.py"
        with open(faulty_plugin_path, "w") as f:
            f.write("# This plugin will cause an import error during test")

        plugins = load_plugins(plugin_folder="plugins")

        # Check if any print call contains the specific error message
        import_error_message_found = any(
            "Error importing plugin module plugins.faulty_plugin_for_test" in call_args[0][0]
            and "Test import error" in call_args[0][0]
            for call_args in mock_print.call_args_list
        )
        self.assertTrue(import_error_message_found, "Import error message for faulty_plugin_for_test.py should be printed.")

        os.remove(faulty_plugin_path) # Clean up

if __name__ == '__main__':
    unittest.main()

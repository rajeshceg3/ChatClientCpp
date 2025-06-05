import os
import importlib
import inspect
from plugin_interface import AppPlugin

def load_plugins(plugin_folder="plugins"):
    """
    Discovers, imports, and instantiates plugins from the given folder.
    """
    plugins = []
    if not os.path.exists(plugin_folder):
        print(f"Plugin folder '{plugin_folder}' not found.")
        return plugins

    # Ensure the plugin folder is in the Python path to allow relative imports within plugins if needed
    # import sys
    # if plugin_folder not in sys.path:
    #     sys.path.insert(0, plugin_folder)

    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{plugin_folder}.{filename[:-3]}"
            try:
                # Invalidate caches to ensure fresh imports, useful for development
                importlib.invalidate_caches()
                module = importlib.import_module(module_name)
                # Reload module if it was already imported, useful for development
                # importlib.reload(module)

                for name, cls in inspect.getmembers(module, inspect.isclass):
                    if issubclass(cls, AppPlugin) and cls is not AppPlugin:
                        try:
                            instance = cls()
                            plugins.append(instance)
                            print(f"Successfully loaded plugin: {name} from {filename}")
                        except Exception as e:
                            print(f"Error instantiating plugin {name} from {filename}: {e}")
            except ImportError as e:
                print(f"Error importing plugin module {module_name}: {e}")
            except Exception as e:
                print(f"Error loading plugin from {filename}: {e}")
    return plugins

if __name__ == "__main__":
    print("Starting application...")
    loaded_plugins = load_plugins()

    if loaded_plugins:
        print(f"\n{len(loaded_plugins)} plugin(s) loaded. Executing them now...")
        for plugin in loaded_plugins:
            try:
                plugin.execute()
            except Exception as e:
                print(f"Error executing plugin {plugin.__class__.__name__}: {e}")
    else:
        print("\nNo plugins were loaded or an error occurred during loading.")

    print("\nApplication finished.")

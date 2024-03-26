"""app/__init__.py
This module provides an interactive command-line interface (CLI) for performing arithmetic operations
and other actions through a plug-and-play command system. The App class orchestrates the loading of
command plugins, registering them for use, and handling user input to execute commands dynamically.
"""
import os
import pkgutil
import importlib
from app.commands import Command, CommandHandler

class App:
    """
    The main application class for the CLI tool. It handles the initialization of the command environment,
    loading of plugins, and the main application REPL for processing user input.
    """

    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """
        Loads command plugins from the designated plugins directory, registering each discovered command
        with the command handler.
        """
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            print(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module)
                except ImportError as e:
                    print(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module):
        """
        Registers commands found within a plugin module with the command handler.

        Args:
            plugin_module: The module object representing a plugin, from which commands will be extracted
                           and registered.

        Notes:
            This method looks for classes within the module that are subclasses of the Command base class
            (but not Command itself) and instantiates and registers each as a command with the CommandHandler.
            It prints a message upon successful registration of each command.
        """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_instance = item()
                self.command_handler.register_command(command_instance)
                print(f"Command '{command_instance.name}' from plugin '{command_instance.name}' registered.")

    def start(self):
        """
        Starts the application's REPL loop, dynamically loading plugins and awaiting user commands.

        This method first loads available command plugins, then enters a loop to process user input,
        invoking commands based on the input provided. Special commands include 'exit' to terminate the application
        and 'show_menu' to display available commands.
        """
        self.load_plugins()
        # Dynamically generate and register the menu command
        dynamic_menu_command = DynamicMenuCommand(self.command_handler)
        self.command_handler.register_command(dynamic_menu_command)

        print("Application started. Type 'show_menu' to see the menu or 'exit' to exit.\n")
        while True:
            cmd_input = input(">>> ")
            if cmd_input.lower() == "exit":
                print("Exiting...")
                break
            elif cmd_input == '':
                # If the input is empty, show the dynamic menu of commands
                self.command_handler.execute_command("show_menu") # Execute the show_menu command
            else:
                try:
                    cmd_name, *args = cmd_input.split()
                    self.command_handler.execute_command(cmd_name, *args)
                except KeyError:
                    print(f"Unknown command: {cmd_input}")
                    self.command_handler.execute_command("show_menu") # Show menu if unknown command
                except Exception as e:
                    print(f"Error executing command: {e}")

class DynamicMenuCommand(Command):
    """
    A special command for displaying a dynamic menu of all registered commands, providing users with
    information about available operations and their descriptions.
    """
    def __init__(self, command_handler):
        super().__init__()
        self.name = "show_menu"
        self.description = "Show the dynamic menu of all commands."
        self.command_handler = command_handler

    def execute(self, *args, **kwargs):
        """
        Executes the command to display a dynamic menu listing all registered commands and their descriptions.

        Args:
            *args: Ignored for this command.
            **kwargs: Ignored for this command.

        Outputs:
            Prints a formatted list of command names and their descriptions to the console.
        """
        commands = self.command_handler.get_commands()
        menu = "Application Menu:\n"
        for name, description in commands:
            menu += f"\t{name}: {description}\n"
        print(menu)

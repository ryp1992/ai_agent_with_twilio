import json
import importlib, os

"""
Tools Class: Dynamically Loads and Manages AI Tools

This module provides the 'Tools' class, which dynamically loads Python modules from a specified directory
and maps functions defined in those modules to tool definitions from a JSON file.
This allows for flexible and extensible AI tool management, where new tools can be added simply by 
placing their Python modules in the 'tools' directory and defining them in the 'tools.json' file.

The class initializes by:
1. Loading the tool definitions from 'tools.json'.
2. Iterating through Python files in the 'tools' directory.
3. Dynamically importing each Python module.
4. Matching function names within the modules to the tool names defined in 'tools.json'.
5. Creating a mapping of tool names to their corresponding functions and definitions.

The class provides methods to retrieve the function and its definition based on the tool name.
"""


class Tools:
    def __init__(self, tools_def_file, tools_dir):
        self.tools_defs = None
        self.tool_function_map = {}

        with open(tools_def_file, "r") as file:
            self.tools_defs = json.load(file)

        for filename in os.listdir(tools_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove ".py" extension
                module_path = os.path.join(tools_dir, filename)

                # Dynamically load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Process each tool from tools.json
                for tool in self.tools_defs:
                    if tool["name"] in dir(module):  # Check if function exists in the module
                        func = getattr(module, tool["name"])
                        self.tool_function_map[tool["name"]] = [func, tool]

        print("Dynamically loading all tools available for AI to use.")
        print(self.tool_function_map)

    def get_function(self, function_name):
        return self.tool_function_map.get(function_name, None)[0]

    def get_function_def(self, function_name):
        return self.tool_function_map.get(function_name, None)[1]


tools = Tools("tools.json", "tools")

import json
import importlib, os


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

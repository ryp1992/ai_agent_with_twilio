Procedure to Add New Tool to the Codebase
1> Add Tool definition to the tools.json file. It should follow the openai function_calling format.
2> Add Tool api to /tools directory. It should be a python file. It should be as the same name as per the tool definition added in step 1.
3> Tool definition will be added to AI agent session.
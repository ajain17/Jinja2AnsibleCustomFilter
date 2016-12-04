# Jinja2AnsibleCustomFilter
A simple custom filter to extract url from a response object

Plugins are automatically loaded when you have one of the following subfolders adjacent to your playbook or inside a role:
* action_plugins
* lookup_plugins
* callback_plugins
* connection_plugins
* filter_plugins
* strategy_plugins
* cache_plugins
* test_plugins
* shell_plugins

Here, we are making use of filter_plugins subfolder to store our custom filter plugin that takes a string param and extracts the url from that string. 
After adding the filter_plugin dir, you can use the filter by its name as you would use any other Jinja2 Filter. 

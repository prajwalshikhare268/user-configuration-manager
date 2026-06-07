import __main__
from pprint import pprint


test_settings={
    "theme":"dark",
    "notifications":"enabled",
    "volume":"high"
}
def add_setting(settings,setting):
    key,value=setting
    key=key.lower()
    value=value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key]=value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings,setting):
    key,value=setting
    key=key.lower()
    value=value.lower()
    
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key]=value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings,key):
    
    key=str(key).lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    output ="Current User Settings:\n"
    for key,value in settings.items():
        
        output += f"{key.capitalize()}: {value}\n"

    return output.strip()

if __main__==__main__:
    print(view_settings(test_settings))
    print(add_setting(test_settings,("Language", "English")))
    pprint(update_setting(test_settings,("theme", "Light")))
    print(delete_setting(test_settings,"volume"))
    print(view_settings(test_settings))

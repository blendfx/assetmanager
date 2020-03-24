import bpy
import os
from pathlib import Path
import subprocess

def get_selected_col_file(context):
    ob = context.active_object
    linked_collection = ob.instance_collection
    original_link_file = linked_collection.library.filepath
    
    return original_link_file, linked_collection


def localize():
    context = bpy.context
    original_link_file, collection = get_selected_col_file(context)
    this_script = Path(os.path.abspath(__file__))
    remote_file_script = this_script.parent / "remote_file_script.py"
    executable = os.path.abspath(bpy.app.binary_path)
    localizer = context.object.localizer

    if localizer.lib_path:
        new_path = bpy.path.abspath(localizer.lib_path)
    else:
        new_path = str(Path(bpy.data.filepath).parent / "lib")


    original_link_file = bpy.path.abspath(original_link_file) 
    print(remote_file_script)
    command = [executable, "--background", original_link_file, "--python", remote_file_script, "--", collection.name, str(new_path)]
    print(command)
    subprocess.call(command)
    collection.library.filepath = bpy.path.relpath(str(Path(new_path) / (Path(original_link_file).stem + ".blend")))
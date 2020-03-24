import bpy
import sys
from pathlib import Path

def main():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    collection = argv[0]
    new_path = argv[1]
    old_path = Path(bpy.data.filepath)
    filename = old_path.stem + ".blend"
    bpy.ops.file.pack_all()
    
    bpy.ops.wm.save_as_mainfile(filepath=str(Path(new_path) / filename))

main()
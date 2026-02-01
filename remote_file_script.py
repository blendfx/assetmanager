import sys
from pathlib import Path

import bpy


def main():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    collection = argv[0]
    new_path = argv[1]
    old_path = Path(bpy.data.filepath)
    filename = old_path.stem + ".blend"

    try:
        bpy.ops.file.pack_all()
    except RuntimeError as ex:
        error_report = "\n".join(ex.args)
        print("Caught error:", error_report)

    bpy.ops.wm.save_as_mainfile(filepath=str(Path(new_path) / filename))


main()


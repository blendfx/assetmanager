bl_info = {
    "name": "Asset Localizer",
    "description": "",
    "author": "Jonas Dichelle, BlendFx",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Object",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}


import bpy
from .localize import localize

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

class LocalizerProperties(PropertyGroup):

    lib_path: StringProperty(
        name = "Local Library Path",
        description="Local Library Path:",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
        )

class WM_OT_Localize(Operator):
    bl_label = "Localize"
    bl_idname = "wm.localize"

    def execute(self, context):
        localize()
        return {'FINISHED'}

def ui_draw(self, context):
    layout = self.layout
    localizer = context.object.localizer

    layout.prop(localizer, "lib_path")
    layout.operator("wm.localize")
    layout.separator()

class OBJECT_PT_LocalizePanel(Panel):
    bl_label = "Localizer"
    bl_idname = "OBJECT_PT_localize_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        ui_draw(self, context)

class OBJECT_PT_LocalizePanel3D(Panel):
    bl_label = "Localizer"
    bl_idname = "OBJECT_PT_localize_panel_3d"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Item"
    bl_context = "objectmode"   

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        ui_draw(self, context)

classes = (
    LocalizerProperties,
    WM_OT_Localize,
    OBJECT_PT_LocalizePanel,
    OBJECT_PT_LocalizePanel3D,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Object.localizer = PointerProperty(type=LocalizerProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Object.localizer


if __name__ == "__main__":
    register()
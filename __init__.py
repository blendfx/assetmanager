bl_info = {
    "name": "Asset Localizer",
    "description": "Save a packed version of a linked collection file locally.",
    "author": "Jonas Dichelle, BlendFx",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Object",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}

from pathlib import Path

import bpy
from bpy.props import PointerProperty, StringProperty
from bpy.types import AddonPreferences, Operator, Panel, PropertyGroup

from .localize import localize


def path_update(self, context, origin):
    if not getattr(self, origin):
        preferences = bpy.context.preferences
        addon_prefs = preferences.addons[__name__].preferences
        path = bpy.path.relpath(str(Path(bpy.data.filepath).parent / addon_prefs.default_lib_path))
        setattr(self, origin, path)


def update_lib_path(self, context, origin):
    if not getattr(self, origin):
        setattr(self, origin, "//lib/")


class LocalizerPreferences(AddonPreferences):
    bl_idname = __name__

    default_lib_path: bpy.props.StringProperty(
        name="Default relative lib path:",
        description="Default path to save assets to locally, relative to the blendfile",
        default="//lib/",
        maxlen=1024,
        subtype='DIR_PATH',
        update=lambda self, context: update_lib_path(self, context, 'default_lib_path')
    )

    def draw(self, context):
        self.layout.prop(self, "default_lib_path")


bpy.utils.register_class(LocalizerPreferences)


class LocalizerProperties(PropertyGroup):
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[__name__].preferences

    lib_path: StringProperty(
        name="Local Library Path",
        description="Path to save asset to.",
        default=addon_prefs.default_lib_path,
        maxlen=1024,
        subtype='DIR_PATH',
        update=lambda self, context: path_update(self, context, 'lib_path')
    )


class WM_OT_Localize(Operator):
    """Save a packed version of the linked file, to the specified lib location"""
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


def ui_poll(self, context):
    poll_true = False
    if context.object:
        if context.object.instance_collection:
            poll_true = True

    return poll_true


class OBJECT_PT_LocalizePanel(Panel):
    bl_label = "Localizer"
    bl_idname = "OBJECT_PT_localize_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    @classmethod
    def poll(self, context):
        return ui_poll(self, context)

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
    def poll(self, context):
        return ui_poll(self, context)

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
    bpy.utils.unregister_class(LocalizerPreferences)
    del bpy.types.Object.localizer


if __name__ == "__main__":
    register()


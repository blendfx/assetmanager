import bpy
from pathlib import Path
from bpy.types import Operator

from . bl_ui_label import *
from . bl_ui_button import *
from . bl_ui_checkbox import *
from . bl_ui_slider import *
from . bl_ui_up_down import *
from . bl_ui_drag_panel import *
from . bl_ui_draw_op import *

class DP_OT_draw_operator(BL_UI_OT_draw_operator):

    bl_idname = "object.dp_ot_draw_operator"
    bl_label = "bl ui widgets custom operator"
    bl_description = "Demo operator for bl ui widgets"
    bl_options = {'REGISTER'}

    def __init__(self):

        super().__init__()

        self.panel = BL_UI_Drag_Panel(-1000, -1000, 1000, 290)
        self.panel.bg_color = (0.2, 0.2, 0.2, 0.9)

        self.label = BL_UI_Label(20, 10, 100, 15)
        self.label.text = "Assets:"
        self.label.text_size = 14
        self.label.text_color = (0.2, 0.9, 0.9, 1.0)

        dir = Path("/home/jonas/Desktop/assets/icons")
        self.widgets_panel = []
        self.widgets_panel.append(self.label)
        for idx, f in enumerate(dir.iterdir()):
            button = BL_UI_Button(20 + idx * 100, 100, 120, 30)
            button.bg_color = (0.2, 0.8, 0.8, 0.8)
            button.hover_bg_color = (0.2, 0.9, 0.9, 1.0)
            button.text = "Scale"
            button.set_image("scale.png")
            button.set_image_size((100,100))
            button.set_image_position((4,2))
            button.set_mouse_down(self.button1_press)
            self.widgets_panel.append(button)

    def on_invoke(self, context, event):

        # Add new widgets here (TODO: perhaps a better, more automated solution?)
        widgets_panel = self.widgets_panel
        widgets =       [self.panel]

        widgets += widgets_panel

        self.init_widgets(context, widgets)

        self.panel.add_widgets(widgets_panel)

        # Open the panel at the mouse location
        self.panel.set_location(event.mouse_x,
                                context.area.height - event.mouse_y + 20)




    # Button press handlers
    def button1_press(self, widget):
        self.slider.set_value(3.0)
        print("Button '{0}' is pressed".format(widget.text))

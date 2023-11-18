import bpy
def context_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        return {'window': window, 'screen': screen, 'area': area, 'region': region, 'scene': bpy.context.scene} 

bpy.ops.object.mode_set(mode='TEXTURE_PAINT') 
bpy.data.objects['RASPBERRY_PI_5 - PLATE_RASPBERRY_PI_5-2'].select_set(True)
bpy.ops.paint.brush_select(image_tool='DRAW')
 
strokes = [{
    "name": "",
    "location": (5, 0.80102, 0.3949),
    "mouse": (0, 0),
    "mouse_event": (0,0),
    "x_tilt": 0,
    "y_tilt": 0,
    "size": 1,
    "pressure": 1,
    "pen_flip": False,
    "time": 0,
    "is_start": True
    },
    {
    "name": "",
    "location": (-32, 0.80102, 0.3949),
    "mouse": (500, 500),
    "mouse_event": (500,500),
    "x_tilt": 0,
    "y_tilt": 0,
    "size": 1,
    "pressure": 1,
    "pen_flip": False,
    "time": 3,
    "is_start": False
    }]


bpy.ops.paint.image_paint(**context_override(), stroke=strokes)
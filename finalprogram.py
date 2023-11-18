"""Final Program

Generates a random camera angel and lighting postions to create
a varitey of diffrent photos for the models """

#Imports Blender Python and other python libaries
import bpy
import math
import random
from mathutils import Vector

# Defines the camera and the object the camera will face in blender
camera = bpy.data.objects['MainCamera'] 
target_object = bpy.data.objects['RASPBERRY_PI_5 - BROADCOM_1-1']

#sets the postion of the camera randomly
z = camera.location[2]
radius = Vector((camera.location[0], camera.location[1], 0)).length
angle = 2 * math.pi * random.random()

# calculates the random postion of the camera
new_camera_pos = Vector((radius * math.cos(angle), radius * math.sin(angle), z))

# places camera in the new calculated postion
bpy.ops.object.camera_add(enter_editmode=False, location=new_camera_pos)

# sets the camera angel to track the target object
track_to = bpy.context.object.constraints.new('TRACK_TO')
track_to.target = target_object
track_to.track_axis = 'TRACK_NEGATIVE_Z'
track_to.up_axis = 'UP_Y'


bpy.context.scene.camera = bpy.context.object

# Creates a lamp in blender and randomly places it above the model 
lamp_data = bpy.data.lights.new(name="Lamp", type='POINT')
lamp_data.energy = 2000
lamp_object = bpy.data.objects.new(name="Lamp", object_data=lamp_data)
bpy.context.collection.objects.link(lamp_object)
lamp_object.location = ((random.randint(-6,6)),(random.randint(-6,6)),5)

#Takes a picture of the scene and saves it 
scene = bpy.context.scene
bpy.context.scene.render.resolution_x = 500
bpy.context.scene.render.resolution_y = 500
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "C:\\Users\\Callum\\OneDrive\\Documents\\Coding\\Python\\SyntheticDataGen\\RaspberryPi-Defect-GAN\\image.png"
bpy.ops.render.render(write_still = 1)
bpy.data.images['Render Result'].save_render(filepath=bpy.context.scene.render.filepath)

# Then deltes the camera and the light to start over again 
bpy.ops.object.select_by_type(type='LIGHT')
bpy.ops.object.delete(use_global=False)

object_to_delete = bpy.data.objects['Camera']
bpy.data.objects.remove(object_to_delete, do_unlink=True)
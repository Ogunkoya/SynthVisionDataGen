import bpy
from random import randint



lamp_data = bpy.data.lights.new(name="Lamp", type='POINT')
lamp_data.energy = 1000
lamp_object = bpy.data.objects.new(name="Lamp", object_data=lamp_data)
bpy.context.collection.objects.link(lamp_object)
lamp_object.location = ((randint(-6,6)),(randint(-6,6)),5)


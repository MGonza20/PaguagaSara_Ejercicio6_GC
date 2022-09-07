from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3))
stone = Material(diffuse = (0.4, 0.4, 0.4))
grass = Material(diffuse = (0.3, 1, 0.3))
snow = Material(diffuse = (1, 0.98039215686, 0.98039215686))
button = Material(diffuse = (0.2, 0.2, 0.2))
button2 = Material(diffuse = (0.3, 0.3, 0.3))
carrot = Material(diffuse=(252/255, 75/255, 45/255))

rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))


# Nose
rtx.scene.append( Sphere(V3(0, 1.8, -7.7), 0.3, carrot))


# Mouth
# Dot 1
rtx.scene.append( Sphere(V3(-0.35, 1.5-0.1, -7.7), 0.08, button))

# Dot 2
rtx.scene.append( Sphere(V3(-0.35+0.2, 1.5-0.2-0.1, -7.7), 0.08, button))

# Dot 3
rtx.scene.append( Sphere(V3(0.35-0.2, 1.5-0.25-0.1, -7.4), 0.08, button2))

#Dot 4
rtx.scene.append( Sphere(V3(0.35, 1.44-0.1, -7.4), 0.08, button2))


# Body

# # Button 3
# rtx.scene.append( Sphere(V3(0, -1.3, -7.7), 0.4, button))
# # Ball 3
# rtx.scene.append( Sphere(V3(0, -2, -9.5), 1.75, snow))

# # Button 1
# rtx.scene.append( Sphere(V3(0, 0.5, -8.3), 0.3, button))
# Ball 1 
rtx.scene.append( Sphere(V3(0, 2, -10), 1.25, snow))

# # Button 2
# rtx.scene.append( Sphere(V3(0, -0.3, -8.3), 0.3, button))
# Ball 2
rtx.scene.append( Sphere(V3(0, 0, -10), 1.5, snow))



rtx.glRender()

rtx.glFinish("output.bmp")

##
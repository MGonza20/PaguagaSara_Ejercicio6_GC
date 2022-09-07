from gl import Raytracer, V3
from figures import *
from lights import *
from texture import Texture



width = 1024
height = 1024



# Materiales
snow = Material(diffuse = (1, 0.98039215686, 0.98039215686))
button = Material(diffuse = (0.2, 0.2, 0.2))
button2 = Material(diffuse = (0.3, 0.3, 0.3))
carrot = Material(diffuse=(252/255, 75/255, 45/255))
eyes = Material(diffuse=(222/255, 215/255, 217/255))

rtx = Raytracer(width, height)

rtx.background = Texture("background.bmp")
rtx.glClearBackground()

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))


# Eyes 
rtx.scene.append( Sphere(V3(-0.32, 2.4, -9.1), 0.3, eyes))
rtx.scene.append( Sphere(V3(-0.305, 2.5, -8.9), 0.125, button))
rtx.scene.append( Sphere(V3(0.32, 2.4, -9.1), 0.3, eyes))
rtx.scene.append( Sphere(V3(0.38, 2.5, -8.9), 0.125, button))

# Nose
rtx.scene.append( Sphere(V3(0, 1.85, -8.2), 0.25, carrot))


# Mouth
# Dot 1
rtx.scene.append( Sphere(V3(-0.35, 1.5+.1, -8.5), 0.08, button))

# Dot 2
rtx.scene.append( Sphere(V3(-0.35+0.2, 1.5-0.2+.1, -8.7), 0.08, button))

# Dot 3
rtx.scene.append( Sphere(V3(0.35-0.2, 1.5-0.2+.1, -8.7), 0.08, button2))

#Dot 4
rtx.scene.append( Sphere(V3(0.35, 1.5+.1, -8.5), 0.08, button2))


# Body

# Button 3
rtx.scene.append( Sphere(V3(0, -1.3, -7.7), 0.4, button))
# Ball 3
rtx.scene.append( Sphere(V3(0, -2, -9.5), 1.75, snow))

# Button 1
rtx.scene.append( Sphere(V3(0, 0.5, -8.3), 0.3, button))
# Ball 1 
rtx.scene.append( Sphere(V3(0, 2, -10), 1.25, snow))

# Button 2
rtx.scene.append( Sphere(V3(0, -0.3, -8.3), 0.3, button))
# Ball 2
rtx.scene.append( Sphere(V3(0, 0, -10), 1.5, snow))



rtx.glRender()

rtx.glFinish("output.bmp")

##
from gl import Raytracer, V3
from figures import *


width = 960
height = 540

rtx = Raytracer(width, height)

rtx.scene.append( Sphere(V3(0,0,-5), 0.5)  )
rtx.scene.append( Sphere(V3(5,0,-15), 1)  )
rtx.scene.append( Sphere(V3(-4,3,-10), 0.2)  )
rtx.scene.append( Sphere(V3(0,0,10), 0.5)  )


rtx.glRender()

rtx.glFinish("output.bmp")
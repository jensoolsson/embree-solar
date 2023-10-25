import sys
sys.path.insert(0, './build')
import py_embree_solar

embree_solar = py_embree_solar.PyEmbreeSolar()

# setup analysis
embree_solar.createDevice()
embree_solar.createScene()
embree_solar.createGeomPlane()
embree_solar.createGridRays()
embree_solar.bundleRays()

# run analysis
embree_solar.raytrace_int1()
embree_solar.raytrace_occ1()
embree_solar.raytrace_occ4()
embree_solar.raytrace_occ8()
embree_solar.raytrace_occ16()







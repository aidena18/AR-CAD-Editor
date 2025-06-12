import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # Get only custom args

stl_path = argv[0]
fbx_path = argv[1]

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Try to import STL using the built-in operator name (manually registered in some versions)
try:
    bpy.ops.wm.stl_import(filepath=stl_path)
except:
    print("❌ Failed to import STL using 'bpy.ops.wm.stl_import'")
    raise

# Export to FBX
bpy.ops.export_scene.fbx(filepath=fbx_path)

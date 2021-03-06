import code, sys, threading, importlib, time
sys.path.append('../fbt-resize')
import fbt_resize

def reload_thread(golist):
    while golist[0] == 1:
        time.sleep(1)
        importlib.reload(fbt_resize)

def console_thread():
    golist=[1] # ok I know it isn't threadsafe but there's no real way
               # this can break
    t = threading.Thread(target=reload_thread, args=(golist,))
    t.start()
    code.interact(local=locals())
    golist[0]=0
    t.join()

threading.Thread(target = console_thread).start()

sys.exit()


# Docs on what to add to the blender console to reload this
fullpath="c:/Users/adam/projects/vrc avatars/avatar_resize/"

import sys
import importlib
sys.path.append(fullpath)
import fbt_resize

# Then, in a loop
importlib.reload(fbt_resize); fbt_resize.main(bpy)

# In emacs, get path with
#default-directory
"c:/Users/adam/projects/vrc avatars/avatar_resize/"

fbt_resize.scale_legs_to_floor(bpy)
fbt_resize.move_to_floor(bpy)
fbt_resize.scale_to_height(bpy, 1.58)

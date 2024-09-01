# Installation

## Installing pygame over conda

* Add conda-forge channel to the config
* Install pygame via conda

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install pygame
```

### MESA-LOADER Error failed to open iris ...

The following error occurred when I installed pygame via pip within a conda environment.

```log
pygame 2.5.2 (SDL 2.28.2, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
X Error of failed request:  BadValue (integer parameter out of range for operation)
  Major opcode of failed request:  152 (GLX)
  Minor opcode of failed request:  3 (X_GLXCreateContext)
  Value in failed request:  0x0
  Serial number of failed request:  179
  Current serial number in output stream:  180
```

The solution is to install as documented above.
This is what helped: https://github.com/conda-forge/pygame-feedstock

### Helpful commands regarding pygame OpenGL

```
cabbage@MSI-ubuntu:~$ glxinfo | grep OpenGL
OpenGL vendor string: Intel
OpenGL renderer string: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL core profile version string: 4.6 (Core Profile) Mesa 24.0.5-1ubuntu1
OpenGL core profile shading language version string: 4.60
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
OpenGL version string: 4.6 (Compatibility Profile) Mesa 24.0.5-1ubuntu1
OpenGL shading language version string: 4.60
OpenGL context flags: (none)
OpenGL profile mask: compatibility profile
OpenGL extensions:
OpenGL ES profile version string: OpenGL ES 3.2 Mesa 24.0.5-1ubuntu1
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20
OpenGL ES profile extensions:
cabbage@MSI-ubuntu:~$ 
```



# Videos I followed with this

| Content | Link | 
| -- | -- |
| Intro | https://www.youtube.com/watch?v=3a--b-QbEcw&t=0s |
| Canvas | https://www.youtube.com/watch?v=cFq3dKa6q0o |
| Movement | https://www.youtube.com/watch?v=H8Pk8O3SNes |
| Boundaries | https://www.youtube.com/watch?v=NjLka-ZxNs4 |
| Jumping | https://www.youtube.com/watch?v=am2Tb_tj8zM |
| Scrolling background | https://www.youtube.com/watch?v=ZlgNM1pALrI |
| Animated characters | https://www.youtube.com/watch?v=9Kh9s9__ywo |
| Sprites & Sprite-Groups | https://youtu.be/4TfZjhw0J-8 |


# Resources I used
| Content | Link | 
| -- | -- | 
| Player | https://opengameart.org/content/flappy-dragon-sprite-sheets | 

# Great resource links

| Content | Link |
| -- | -- | 
| Open Game Resources | https://opengameart.org/ | 


# Possible Schema

* get_background()
* def draw()
* def main(window)

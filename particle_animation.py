from moderngl_window import WindowConfig
import moderngl
import sys
import numpy as np
from particle import Particle


class Animation(WindowConfig):
    gl_version = (3, 3)
    title = "Particle Animation"
    window_size = (960, 960)
    aspect_ratio = None
    resizable = False
    vsync = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctx.enable(moderngl.PROGRAM_POINT_SIZE)
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE



        # Für Erweiterung auf 3D siehe Notion 
        self.num_particles = 5000
        center_x = np.random.uniform(-1, 1, self.num_particles).astype('f4') # Position der Partikel
        center_y = np.random.uniform(-1, 1, self.num_particles).astype('f4') # Position der Partikel
        #center_z = np.random.uniform(-1, 1, self.num_particles).astype('f4') # Position der Partikel später 3D

        velocity_x = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Geschwindigkeit in x-Richtung
        velocity_y = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Geschwindigkeit in y-Richtung
        #velocity_z = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Geschwindigkeit in z-Richtung später 3D
        
        acceleration_x = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Beschleunigung in x-Richtung
        acceleration_y = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Beschleunigung in y-Richtung
        #acceleration_z = np.random.uniform(-0.001, 0.001, self.num_particles).astype('f4') # Beschleunigung in z-Richtung später 3D

        point_size = np.random.uniform(5, 7, self.num_particles).astype('f4') # Größe der Partikel

        color_r = np.full(self.num_particles, 25/255.0).astype('f4') # Farbe der Partikel (Rot)
        color_g = np.full(self.num_particles, 146/255.0).astype('f4') # Farbe der Partikel (Grün)
        color_b = np.full(self.num_particles, 223/255.0).astype('f4') # Farbe der Partikel (Blau)
        color_a = np.full(self.num_particles, 255/255.0).astype('f4') # Farbe der Partikel (Alpha)
        
# Erstelle die Partikel
        self.particles = Particle(center_x=center_x,
        center_y=center_y,
        velocity_x=velocity_x,
        velocity_y=velocity_y,
        acceleration_x=acceleration_x,
        acceleration_y=acceleration_y,
        point_size=point_size,
        color_r=color_r,
        color_g=color_g,
        color_b=color_b,
        color_a=color_a,
        ctx=self.ctx,
        resolution=self.window_size,
        vertex_shader="Shaders/particle.vert",
        fragment_shader="Shaders/particle.frag",
        )

    def update_buffers(self):
        self.particles.update_buffers() #kann das weg?

    def logic(self):
        self.particles.transition()

    def on_render(self, time: float, frame_time: float) -> None:
        self.ctx.clear()
        self.logic()
        self.update_buffers()
        self.particles.vao.render(moderngl.POINTS)
    


if __name__ == "__main__":
    # Run the animation.
    Animation.run()
    sys.exit()

import numpy as np

class Particle():
    def __init__(self, **configs):
        self.center_x   = configs.get('center_x', [0.0])
        self.center_y   = configs.get('center_y', [0.0])
        self.velocity_x = configs.get('velocity_x', [0.0])
        self.velocity_y = configs.get('velocity_y', [0.0])
        self.point_size = configs.get('point_size', [1.0])
        self.color_r    = configs.get('color_r', [1.0])
        self.color_g    = configs.get('color_g', [1.0])
        self.color_b    = configs.get('color_b', [1.0])
        self.color_a    = configs.get('color_a', [1.0])
        self.acceleration_x = configs.get('acceleration_x', [0.0])
        self.acceleration_y = configs.get('acceleration_y', [0.0])
        self.resolution = configs.get('resolution', [960, 960])
        self.ctx        = configs.get('ctx', None)
        self.vertex_shader   = configs.get('vertex_shader', None)
        self.fragment_shader = configs.get('fragment_shader', None)
        self.numpy_the_values()
        self.num_particles = len(self.center_x)
        self.generate_shader_program()
        self.vbo_center_x = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_center_y = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_velocity_x = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_velocity_y = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_point_size = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_color_r = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_color_g = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_color_b = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_color_a = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_acceleration_x = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vbo_acceleration_y = self.ctx.buffer(reserve=self.num_particles * 4)
        self.vao = None
        self.generate_vao()
        self.update_buffers()

    def numpy_the_values(self):
        if type(self.center_x) is not np.ndarray:
            self.center_x = np.array(self.center_x, dtype='f4')
        if type(self.center_y) is not np.ndarray:
            self.center_y = np.array(self.center_y, dtype='f4')
        if type(self.velocity_x) is not np.ndarray:
            self.velocity_x = np.array(self.velocity_x, dtype='f4')
        if type(self.velocity_y) is not np.ndarray:
            self.velocity_y = np.array(self.velocity_y, dtype='f4')
        if type(self.point_size) is not np.ndarray:
            self.point_size = np.array(self.point_size, dtype='f4')
        if type(self.color_r) is not np.ndarray:
            self.color_r = np.array(self.color_r, dtype='f4')
        if type(self.color_g) is not np.ndarray:
            self.color_g = np.array(self.color_g, dtype='f4')
        if type(self.color_b) is not np.ndarray:
            self.color_b = np.array(self.color_b, dtype='f4')
        if type(self.color_a) is not np.ndarray:
            self.color_a = np.array(self.color_a, dtype='f4')
        if type(self.resolution) is not np.ndarray:
            self.resolution = np.array(self.resolution, dtype='f4')
        if type(self.acceleration_x) is not np.ndarray:
            self.acceleration_x = np.array(self.acceleration_x, dtype='f4')
        if type(self.acceleration_y) is not np.ndarray:
            self.acceleration_y = np.array(self.acceleration_y, dtype='f4')

    def generate_shader_program(self):
        if self.vertex_shader and self.fragment_shader:
            with open(self.vertex_shader) as f:
                vertex_shader = f.read()
            with open(self.fragment_shader) as f:
                fragment_shader = f.read()
            print("Vertex Shader:")
            print(vertex_shader)
            print("Fragment Shader:")
            print(fragment_shader)
            self.shader_program = self.ctx.program(
                vertex_shader=vertex_shader,
                fragment_shader=fragment_shader
            )
            print("Shader attributes:", [attr for attr in dir(self.shader_program) if not attr.startswith('_')])

    def generate_vao(self):
        self.vao = self.ctx.vertex_array(
            self.shader_program,
            [
                (self.vbo_center_x, '1f', 'in_center_x'),
                (self.vbo_center_y, '1f', 'in_center_y'),
                #(self.vbo_velocity_x, '1f', 'in_velocity_x'),
                #(self.vbo_velocity_y, '1f', 'in_velocity_y'),
                #(self.vbo_acceleration_x, '1f', 'in_acceleration_x'),
                #(self.vbo_acceleration_y, '1f', 'in_acceleration_y'),
                (self.vbo_color_r, '1f', 'in_color_r'),
                (self.vbo_color_g, '1f', 'in_color_g'),
                (self.vbo_color_b, '1f', 'in_color_b'),
                (self.vbo_color_a, '1f', 'in_color_a'),
                (self.vbo_point_size, '1f', 'in_point_size')
            ]
        )

    def update_buffers(self):
        self.vbo_center_x.write(self.center_x)
        self.vbo_center_y.write(self.center_y)
        self.vbo_velocity_x.write(self.velocity_x)
        self.vbo_velocity_y.write(self.velocity_y)
        self.vbo_point_size.write(self.point_size)
        self.vbo_color_r.write(self.color_r)
        self.vbo_color_g.write(self.color_g)
        self.vbo_color_b.write(self.color_b)
        self.vbo_color_a.write(self.color_a)
        self.vbo_acceleration_x.write(self.acceleration_x)
        self.vbo_acceleration_y.write(self.acceleration_y)
        #self.shader_program['resolution'] = self.resolution

    def transition(self):
        pass

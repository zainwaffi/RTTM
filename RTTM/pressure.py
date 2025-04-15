from manim import *


class pressuretransfer(Scene):
    def construct(self):
        points= VGroup()
        x_min, x_max = -5, 5.5
        y_min, y_max = -2, 2.5

        # the rectangle of points with gradient color
        for i in np.arange(x_min,x_max,0.5):
            for j in np.arange(y_min, y_max,0.5):

                alpha =(i - x_min) / (x_max - x_min)
                color = interpolate_color(BLUE, RED, alpha)
                point = Dot([i,j,0], color=color, radius=0.1)
                points.add(point)

        self.add(points)
        pressure= MathTex(r'P', color=WHITE).scale(2)
        pressure.to_edge(UP)
        self.add(pressure)

        arrow= Arrow(start=2*RIGHT, end=2*LEFT, color=WHITE).scale(1.2)
        self.play(GrowFromEdge(arrow, RIGHT),rate_func= linear, run_time=5)
        self.wait()




        # Gradient vector field

class pressuregradient(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-120*DEGREES)

        # Axes
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, 2, 1))

        # Surface function
        func = lambda u, v: axes.c2p(u, v, 2 * np.sin(u) * np.cos(v))

        surface = Surface(
            func,
            resolution=30,
            v_range=[-1.5, 1.5],
            u_range=[-1.5, 1.5],
        ).fade(0.5)

        # Gradient in (u, v) space
        def gradient(u, v):
            dx = 2 * np.cos(u) * np.cos(v)
            dy = -2 * np.sin(u) * np.sin(v)
            return np.array([dx, dy])

        # Initial position in (u, v)
        u_val = ValueTracker(0.5)
        v_val = ValueTracker(0)
        
        pressure = MathTex(r' - \nabla P ')
        pressure.scale(2).to_corner(UL)
        self.add_fixed_in_frame_mobjects(pressure)
        # Dot on the surface
        dot = always_redraw(lambda: Dot3D(func(u_val.get_value(), v_val.get_value()), color=RED))

        
        arrow= always_redraw( lambda: Arrow(start=dot.get_center(), end=dot.get_center()-[1,1,0], color=RED))

        # Update function to simulate gradient descent in (u, v) space
        def update_uv(mob, dt):
            u = u_val.get_value()
            v = v_val.get_value()
            grad = gradient(u, v)
            step_size = 0.1 * dt  # adjust for smoothness
            u_val.set_value(u - step_size * grad[0])
            v_val.set_value(v - step_size * grad[1])


        dot.add_updater(update_uv)

        surface.set_fill_by_value(axes, colorscale= [(BLUE,0), (RED,0)],axis=2)


        self.add(axes, surface, dot, arrow)

        self.wait(10)
        dot.clear_updaters()

        self.wait()


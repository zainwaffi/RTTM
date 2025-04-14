from manim import *


def div_field(p):
    epsilon=1
    x , y , z =  p
    # Source-like terms
    fx1 = (x - 2) / ((x - 2)**2 + (y - 2)**2 + epsilon)
    fy1 = (y - 2) / ((x - 2)**2 + (y - 2)**2 + epsilon)

    fx2 = (x + 2) / ((x + 2)**2 + (y + 2)**2 + epsilon)
    fy2 = (y + 2) / ((x + 2)**2 + (y + 2)**2 + epsilon)

    # Sink-like terms
    fx3 = (x - 2) / ((x - 2)**2 + (y + 2)**2 + epsilon)
    fy3 = (y + 2) / ((x - 2)**2 + (y + 2)**2 + epsilon)

    fx4 = (x + 2) / ((x + 2)**2 + (y - 2)**2 + epsilon)
    fy4 = (y - 2) / ((x + 2)**2 + (y - 2)**2 + epsilon)

    # Net vector
    fx = fx1 + fx2 - fx3 - fx4
    fy = fy1 + fy2 - fy3 - fy4

    return np.array([fx, fy,0])


def pointers(p, n=5, radius=0.5,sign=1):
    terminal_point = p
    vectors=VGroup()
    for i in range(n):
            angle = 2 * PI * i / n
            origin = terminal_point + radius * np.array([np.cos(angle), np.sin(angle), 0])
            new_terminal = terminal_point + 1.2*np.array([np.cos(angle), np.sin(angle), 0])
            vector = Arrow(start=origin, end=new_terminal , buff=0, color=BLUE)
            if sign == 1:
                vector.rotate(PI)
            vectors.add(vector)
    return vectors


def stokes_flow(v,R=0.3,U=1.0):
    
    x,y , z = v
    """
    Creeping flow (Re << 1) around a cylinder of radius R
    in 2D at uniform flow speed U.
    """
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    
    if r < R:
        return np.array([0.0, 0.0,0.0])  # inside the cylinder, no flow

    # Radial and angular velocity components (u_r, u_theta)
    ur = U * (1 - (R**2 / r**2)) * np.cos(theta)
    ut = -U * (1 + (R**2 / r**2)) * np.sin(theta)

    # Convert to Cartesian
    u = ur * np.cos(theta) - ut * np.sin(theta)
    v = ur * np.sin(theta) + ut * np.cos(theta)

    return np.array([u, v, 0.0])



class compressible(Scene):
    def construct(self):   
        divP=MathTex(r'\nabla \cdot \textbf{u} < 0', color=WHITE)
        divN=MathTex(r'\nabla \cdot \textbf{u} > 0', color=WHITE)

        
        st=StreamLines(div_field, stroke_width=2,x_range=[-10, 10, 0.5], y_range=[-6, 6, 0.5])
        vf= ArrowVectorField(div_field, x_range=[-10, 10, 0.5], y_range=[-6, 6, 0.5])
        self.add(vf)

        v1= pointers([-2.3,2.2,0], n=10, radius=0.5)
        v2= pointers([-2.3,-2.2,0], n=10, radius=0.5, sign=-1)
        v3= pointers([2.3,2.2,0], n=10, radius=0.5, sign=-1)
        v4= pointers([2.3,-2.2,0], n=10, radius=0.5)
        vg=VGroup(v1,v2,v3,v4)

        self.add(st)
        st.start_animation(warm_up=True, flow_speed=1)
        self.wait(5)
        self.play(LaggedStartMap(Create, vg, run_time=2, lag_ratio=0.1))
        self.wait(2)
        divP.next_to(v1, DOWN)
        divN.next_to(v2, UP)
        self.play(Write(divP), run_time=1)
        self.play(Write(divN), run_time=1)
        self.wait(2)
        self.play(LaggedStartMap(FadeOut, vg, run_time=2, lag_ratio=0.1))





class incompressible(Scene):
    def construct(self):   
        st=StreamLines(stokes_flow, stroke_width=2,x_range=[-10, 10, 0.5], y_range=[-6, 6, 0.5])
        vf= ArrowVectorField(stokes_flow, x_range=[-10, 10, 0.5], y_range=[-6, 6, 0.5])
        self.add(vf, st)
        div=MathTex(r'\nabla \cdot \textbf{u} = 0', color=WHITE).scale(2)
        self.add(div)
        
        st.start_animation(warm_up=False, flow_speed=.75)
        self.wait(5)


from manim import *


def f3(x,y):
 
    f= np.cos(x) + np.sin(y) 
    return np.array([x,y,f])

def grad(x,y):
    dx = -np.sin(x)
    dy = np.cos(y)
    return np.array([dx,dy, f3(x,y)[2]])


class Viscosityslide(Scene):
    def construct(self):
        #sign object
        fluid=VGroup()
        
        x_min, x_max = -6*4, 6*4
        y_min, y_max = -3, 3

        for j in range(y_min, y_max, 1):
            for i in range(x_min, x_max, 1):
                point = Dot([i, j, 0],radius=0.5, color=BLUE)
                fluid.add(point)

        fluid.shift(LEFT*4)
        fluid.fade(0.5)
        

        gs=VGroup(*[ fluid[i:i+12*4] for i in range(0, len(fluid), 12*4)])
        


    
        # self.add(fluid)
        self.add(gs)
        
        rec= SurroundingRectangle(fluid, color=WHITE, buff=0.1)
        

    
        
        self.add(rec)
        
        def shift(mob, alpha):
            mob.shift(RIGHT*alpha/10)

        anim=[]
        for i in range(0, len(gs)):
            animation= UpdateFromAlphaFunc(gs[i], shift, run_time=10, rate_func=linear)
            anim.append(animation)

        anim.reverse()
        viscosity= MathTex(r'\tau = \mu \frac{du}{dy}', color=WHITE).scale(4)
        self.add_foreground_mobject(viscosity)

        self.play(LaggedStart(*anim, lag_ratio=0.05))
        self.wait(2)
            
        
        


class Viscositylayers(ThreeDScene):
    def construct(self):
        points=PGroup()
        # ax=ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-1, 1], axis_config={"color": WHITE})
        # self.add(ax)
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        for j in np.linspace(-5, 5, 70):
            for i in np.linspace(-2.5, 2.5, 70):
                point = Point(f3(i,j), color=WHITE)
                point.set_color(BLUE)
                points.add(point)

        
        
     
        self.play(FadeIn(points), run_time=3)
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES,run_time=3)
        self.wait(2)
      
        max_p= (PI/4,PI/4)

        
        dot= Dot3D(f3(*max_p), color=RED)
        
        t= Arrow3D(start=f3(*max_p), end=f3(*max_p)+0.5*grad(*max_p), color=WHITE)
        b= t.copy().rotate(PI/2,about_point=dot.get_center(), axis=RIGHT)
        n= t.copy().rotate(PI/2,about_point=dot.get_center(), axis=OUT)
        vg= VGroup(t,n,b,dot)
        
  
        self.play(LaggedStartMap(Create,vg, run_time=1))
        diff= MathTex(r'\nabla \cdot \nabla u = \nabla ^2 u', color=WHITE).to_corner(UL)
     
        self.add_fixed_in_frame_mobjects(diff)
        self.play(Write(diff), run_time=2)
        self.wait(2)
        
            
        
        

        

    



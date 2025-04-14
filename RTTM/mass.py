from manim import *





# newton to navier stokes reasoning

class object(Scene):
    def construct(self):

        #object
        obj = Circle(radius=0.3, color=RED,fill_opacity=1).scale(2)
        surface = Line(start=2*LEFT + obj.get_bottom(), end=2*RIGHT + obj.get_bottom(), color=BLUE)

        #forces
        weight = Arrow(start=2*DOWN , end=obj.get_center(), max_tip_length_to_length_ratio=0.2 , buff=0).rotate(PI)
        weight.scale(0.8,about_point=weight.get_start())
        force = Arrow(start=2*RIGHT , end=obj.get_center(), max_tip_length_to_length_ratio=0.2 , buff=0).rotate(PI)
        force.scale(0.8,about_point=force.get_start())
        friction= Arrow(start=surface.get_start() -0.8*LEFT, end=obj.get_bottom(), max_tip_length_to_length_ratio=0.2 , buff=0)

        #text
        sym= MathTex(r'\textbf{F}',r'W', r'f', color=WHITE)
        sym[0].next_to(force, RIGHT)
        sym[1].next_to(weight, DOWN)
        sym[2].next_to(friction, DOWN)
        vg=VGroup(obj, surface, force, weight, friction)
        self.play(Create(vg), run_time=2, rate_func=linear)
        self.play(Write(sym),run_time=2)
        self.wait(2)






class setup(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3, # scale of zoomed_camera camera
            zoomed_display_height=2,
            zoomed_display_width=3,
            zoomed_camera_config={
                "default_frame_stroke_width": 2, # frame border
            },
            **kwargs
        )

    def setup(self):
        # Call ZoomedScene.setup(self)
        super().setup()
        # Define zoom mobs
        zoomed_display        = self.zoomed_display
        zoomed_display_border = zoomed_display.display_frame
        frame                 = self.zoomed_camera.frame
        # set zoom mobs props
        
        self.zoomed_objs = [zoomed_display, zoomed_display_border, frame]




# newton to navier stokes reasoning

class desnity(setup):
    def construct(self):

        #part of the camera
        zoomed_display, zoomed_display_border, frame = self.zoomed_objs
        zoomed_display.scale(0.85)


        #the water
        fluid=VGroup()
        
        x_min, x_max = -2, 2
        y_min, y_max = -2, 1

        for j in np.linspace(y_min, y_max, 40):
            for i in np.linspace(x_min, x_max, 40):
                point = Dot([i, j, 0],radius=0.04, color=BLUE)
                fluid.add(point)

        bottom_left = [x_min-0.1, y_min-0.1, 0]
        bottom_right = [x_max+0.1, y_min-0.1, 0]
        top_right = [x_max+0.1, y_max+0.1, 0]
        top_left = [x_min-0.1, y_max+0.1, 0]

        # Create lines (skip the top line)
        left_edge = Line(bottom_left, top_left, color=WHITE)
        bottom_edge = Line(bottom_left, bottom_right, color=WHITE)
        right_edge = Line(bottom_right, top_right, color=WHITE)
        box = VGroup(left_edge, bottom_edge, right_edge)

        vg=VGroup(fluid, box).shift(DOWN)
        self.add(vg)
        vgc=vg.copy().scale(0.5)
        
        line= Line(start=LEFT, end=RIGHT, color=WHITE).scale(1.2)
        line.next_to(zoomed_display.get_bottom(),DOWN)
        frame.shift(vg.get_center())
        

        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation())
        self.play(Create(line))
        self.play(vgc.animate.next_to(line.get_center(),DOWN), run_time=2)

        rho= MathTex(r'\rho =', color=WHITE).scale(2)
        rho.next_to(line, LEFT,buff= 1)
        self.play(Write(rho))
        density= MathTex(r'm',r'V', color=WHITE).scale(2)
        density[0].next_to(zoomed_display, UP,buff=0.1)
        density[1].move_to(vgc.get_center())
        
        self.play(LaggedStart(Write(density[0]),Write(density[1]), run_time=2, lag_ratio=0.5))
        self.wait(3)


   

        
        
       
        

       
      

        
        
    
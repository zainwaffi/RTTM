from manim import *




#acceleration to vector field
class projectile(Scene):
    def construct(self):

        # set up axes and graph
        axes = Axes(
            x_range=[0, 4],
            y_range=[-1, 3],
            axis_config={"color": WHITE}, 
        )

        t_label = MathTex("t").next_to(axes.x_axis, RIGHT)
        s_label = MathTex("s(t)").next_to(axes.y_axis, UP)
        labels= VGroup(t_label, s_label)
        self.add(axes,labels)
        f= lambda x: -3/4 *(x-2)**2 +3
        graph = axes.plot(f, color=RED)
        self.add(graph)

        # set up point and vector

        def get_tangent_vector(proportion, curve, scale=1):
            coord_i = curve.point_from_proportion(proportion if proportion <0.999 else proportion - 0.001)
            coord_f = curve.point_from_proportion(proportion + 0.001 if proportion <0.999 else proportion ) 
            reference_line = Line(coord_i,coord_f)
            unit_vector = reference_line.get_unit_vector() * scale
            vector = Arrow(coord_i, coord_i + unit_vector,color= YELLOW, buff=0)
            return vector

        vector = get_tangent_vector(0, graph, scale=1.5)

        dot = Dot(graph.point_from_proportion(0), color=YELLOW)
        dot.add_updater(lambda d: d.move_to(vector.get_start()))
        #make the arrow follow the dot
        def tan(mob, alpha):
            mob.become(
                    get_tangent_vector(alpha,graph,scale=2))

    

        self.add(dot, vector)
        u= MathTex(r'u(t)', color=YELLOW)
        u.add_updater(lambda l: l.next_to(dot.get_center(), UP))
        self.add(u)


        self.play(UpdateFromAlphaFunc(vector, tan), run_time=8, rate_func=linear)
    
    
        
        
        self.wait(2)



       



class flowfield(Scene):
    def construct(self):
        # Set x_range and y_range to start at 0 
        plane = NumberPlane().fade(1)
        self.add(plane)


        points= VGroup()
        for i in np.arange(-7,7.5,0.5):
            for j in np.arange(-4, 4.5,0.5):
                point = Dot(plane.c2p(i,j), color=BLUE, radius=0.05)
                points.add(point)

        points.fade(0.5)


        func = lambda p: np.array([p[1],p[0],0])
        gradf= lambda p: np.array([1.,1.,0])
        # add the field and hide them 
        gradient_field = ArrowVectorField(gradf, color=BLUE)
        vector_field= ArrowVectorField(func)
        gradient_field.fade(1)
        vector_field.fade(1)
        self.add(gradient_field,vector_field)
        

        self.play(LaggedStartMap(FadeIn, points, run_time=2, lag_ratio=0.1))
        self.play(plane.animate.set_opacity(0.3))
        self.play(vector_field.animate.set_opacity(1))

        u= MathTex(r'u \cdot \nabla u', color=WHITE).scale(2).to_edge(UP)
        self.play(Write(u))
        self.add_foreground_mobject(u)

        self.play(LaggedStart(gradient_field.animate.set_opacity(1),vector_field.animate.fade(0.7), run_time=3, lag_ratio=0))
        self.wait(2)
        self.play(vector_field.animate.set_opacity(1))
        self.wait(2)

        vg=VGroup(vector_field, gradient_field)
        self.play(vg.animate.set_opacity(0.7))
        
        







        # streamlines
        stream_lines = StreamLines(func, stroke_width=2).fade(0.3)
        self.add(stream_lines)
        
       
        stream_lines.start_animation(warm_up=True, flow_speed=0.75)
        self.wait(5)

        
        
       
        

       
      

        
        
    
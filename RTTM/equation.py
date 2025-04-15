from manim import *



#navier-stokes equations 
class Equations(Scene):
    def construct(self):
        T1= Text('Continunity equation')
        T2= Text('momentum equation')
        
        ns=MathTex(r'\rho', r'\frac{D\textbf{u}}{Dt}', r'=', r'-\nabla P', r'+ \mu \nabla^2\textbf{u}', r'+ \textbf{f}', color=WHITE).scale(1.5)
      
        ce_ns= MathTex(r' \nabla \cdot \textbf{u} =0',color=WHITE).scale(2.5)
        

        vg=VGroup(T1,ce_ns,T2,ns).shift(DOWN)
        vg.arrange(DOWN)
        vg[:2].shift(0.5*UP)
        vg[2:].shift(0.3*DOWN)
        self.add(vg)
        material_d=MathTex(r'\rho', r'( \frac{\partial u}{ \partial t} + u \cdot \nabla u)',
                 r'=', r'-\nabla P', r'+ \mu \nabla^2\textbf{u}', r'+ \textbf{f}', color=WHITE).scale(1.5).move_to(vg[3].get_center())
        
        self.play(TransformMatchingTex(vg[3],material_d), run_time=2, rate_func=smooth)
        self.wait(2)



#newton to navier-stokes equation 

class Equation(Scene):
    def construct(self):
        ns=MathTex(r'\rho', r'\frac{D\textbf{u}}{Dt}', r'=', r'-\nabla P', r'+ \mu \nabla^2\textbf{u}', r'+ \textbf{f}', color=WHITE).scale(1.5)
        nw=MathTex( r'm', r'\textbf{a}',r'=',r'\Sigma \textbf{F}',color=WHITE).scale_to_fit_width(ns.width)
        nw.fade(0.5)
        self.add(ns)
        material_d=MathTex(r'\rho', r'( \frac{\partial u}{ \partial t} + u \cdot \nabla u)',
                 r'=', r'-\nabla P', r'+ \mu \nabla^2\textbf{u}', r'+ \textbf{f}', color=WHITE).scale(1.5)
        self.play(TransformMatchingTex(ns,material_d), run_time=2, rate_func=linear)

        
        self.wait(2)
        self.play(FadeIn(nw), run_time=3,rate_func=linear)

        self.wait(2)
        self.play(LaggedStart(FadeOut(material_d),nw.animate.set_opacity(1), run_time=1,lag_ratio=0.5, rate_func=linear))
        self.wait(2)
        
        
# external is equal to gravity 
class Gravity(Scene):
    def construct(self):
        material_d=MathTex(r'\textbf{f}',color=WHITE).scale(4)

        self.add(material_d)
        self.play(material_d.animate.shift(LEFT),run_time=1,rate_func=smooth)
        g=MathTex(r'=\rho g',color= WHITE).scale(4).next_to(material_d,RIGHT)

        self.play(Write(g))
        self.wait(3)



from manim import *



# part 1 of presentation 

class Example(Scene):
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
        
        
       
        



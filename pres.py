from manim import *

class continuity(Scene):
    def construct(self):
        ms=Text('Mass Conservation').scale(1.5)
       
        cty= Text('Continutiy Equation').scale(1.5)
        
        

        mc=MathTex(r'\frac{\partial \rho}{\partial t}+' ,r'\nabla \cdot (\rho u) = 0 ').scale(2)
        mc_=MathTex(r'\rho \nabla \cdot u = 0 ').scale(2)
        
        ce=MathTex(r' \nabla \cdot \textbf{u} =0').scale(2.5)
        cauchy= MathTex(r'\rho ',r'\frac{Du}{Dt}',r'= \nabla \cdot \sigma + \textbf{f} ').scale(2)
        stress= MathTex(r' \sigma = - PI + \tau').scale(3)
        tau= MathTex(r' \tau = \mu (\nabla u + (\nabla u)^T)', r'+ \lambda (\nabla \cdot u)I').scale(2)
        
        gradsigma= MathTex(r' \nabla \sigma = - \nabla P I + \mu \nabla(\nabla u + (\nabla u)^T)').scale(2)
        gradsigma= MathTex(r' \nabla \sigma = - \nabla P I + \mu ',r'\nabla(\nabla u + (\nabla u)^T)').scale(2)
        sub= MathTex(r' \nabla \cdot \sigma = - \nabla P  + \mu \nabla^2 u ').scale(2)
        nv=MathTex(r'\rho', r'\frac{Du}{Dt}  = -\nabla P + \mu \nabla^2\textbf{u} + \textbf{f}').scale(2)
        vg=VGroup(mc,ce,cauchy,stress,tau,gradsigma,sub,nv)

        ms.to_edge(UP,buff=2)
        cty.move_to(ms.get_center())
        self.play(FadeIn(ms,shift=DOWN))
        mc.next_to(ms,DOWN)
        self.play(Write(mc,run_time=2 ))
        rec=SurroundingRectangle(mc[0])
        line=Line(rec.get_corner(DL),rec.get_corner(UR))
        self.play((Write(line)))
        self.play(LaggedStartMap(FadeOut, VGroup(line,mc[0]),lag_ratio=0))
        self.play(mc[1].animate.shift(LEFT))
        self.wait()
        mc_.move_to(mc.get_center())
        self.play(TransformMatchingShapes(mc[1],mc_,run_time=1.5))
        ce.move_to(mc.get_center())
        
        self.play(TransformMatchingShapes(mc_,ce))
        self.play(TransformMatchingShapes(ms,cty))
        self.wait(2)





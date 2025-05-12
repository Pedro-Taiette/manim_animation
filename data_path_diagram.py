from manim import *

class DataPathDiagram(Scene):
    def construct(self):
        # Cores das etapas
        COLOR_FETCH = PURPLE
        COLOR_DECODE = ORANGE
        COLOR_EXECUTE_AX = BLUE
        COLOR_EXECUTE_BX = RED
        COLOR_STORE = GREEN

        # Título
        title = Text("Caminho dos Dados no Processador", font_size=32, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Componentes fixos
        mem = Rectangle(width=2, height=2.4, fill_color=GREY_B, fill_opacity=0.6).move_to(LEFT * 5)
        mem_label = Text("Memória\nPrincipal", font_size=16).next_to(mem, DOWN, buff=0.15)

        reg_ax = Rectangle(width=1.4, height=0.6, fill_color=BLUE_E, fill_opacity=0.7).move_to(LEFT * 2.5 + UP * 1.4)
        reg_bx = Rectangle(width=1.4, height=0.6, fill_color=BLUE_E, fill_opacity=0.7).move_to(LEFT * 2.5 + DOWN * 1.4)
        label_ax = Text("Reg. AX", font_size=16).next_to(reg_ax, DOWN, buff=0.1)
        label_bx = Text("Reg. BX", font_size=16).next_to(reg_bx, DOWN, buff=0.1)

        alu_box = Rectangle(width=3, height=2, fill_color=YELLOW, fill_opacity=0.2, color=YELLOW_D).move_to(RIGHT * 2.3)
        alu_label = Text("ULA", font_size=20, weight=BOLD).next_to(alu_box, UP, buff=0.15)
        adder = Text("Somador", font_size=14).move_to(alu_box.get_center() + UP * 0.6 + LEFT * 0.8)
        logic = Text("Lógica", font_size=14).move_to(alu_box.get_center() + RIGHT * 0.8)
        temp_reg = Text("Reg. Temp", font_size=12).move_to(alu_box.get_center() + DOWN * 0.6)

        control_unit = Rectangle(width=2, height=1, fill_color=GREEN, fill_opacity=0.5).move_to(DOWN * 2.5 + RIGHT * 2.3)
        control_label = Text("Controle", font_size=16).move_to(control_unit.get_center())

        mem_out = Rectangle(width=2, height=1.2, fill_color=GREY_C, fill_opacity=0.5).move_to(RIGHT * 5.3)
        mem_out_label = Text("Memória Final", font_size=16).next_to(mem_out, DOWN, buff=0.15)

        # Aparecem juntos
        self.play(
            FadeIn(mem), Write(mem_label),
            FadeIn(reg_ax), FadeIn(reg_bx), Write(label_ax), Write(label_bx),
            FadeIn(alu_box), Write(alu_label), Write(adder), Write(logic), Write(temp_reg),
            FadeIn(control_unit), Write(control_label),
            FadeIn(mem_out), Write(mem_out_label),
        )
        self.wait(0.5)

        # Função auxiliar para mostrar etapa
        def mostrar_etapa(etapa, cor, desc):
            step = Text(f"Etapa: {etapa}", font_size=22, color=cor).next_to(title, DOWN, buff=0.3)
            descricao = Text(desc, font_size=16).next_to(step, DOWN, buff=0.1)
            self.play(FadeIn(step), FadeIn(descricao))
            return step, descricao

        # FETCH
        step_fetch, desc_fetch = mostrar_etapa("FETCH", COLOR_FETCH, "Busca a instrução na memória principal")
        arrow1 = Arrow(mem.get_right(), reg_ax.get_left(), buff=0.1, color=COLOR_FETCH)
        arrow2 = Arrow(mem.get_right(), reg_bx.get_left(), buff=0.1, color=COLOR_FETCH)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(1)
        self.play(FadeOut(step_fetch), FadeOut(desc_fetch))

        # DECODE
        step_decode, desc_decode = mostrar_etapa("DECODE", COLOR_DECODE, "A unidade de controle decodifica a instrução")
        ctrl_arrows = VGroup(
            Arrow(control_unit.get_top(), alu_box.get_bottom(), buff=0.1, color=COLOR_DECODE),
            Arrow(control_unit.get_left(), reg_ax.get_bottom(), buff=0.1, color=COLOR_DECODE),
            Arrow(control_unit.get_left(), reg_bx.get_bottom(), buff=0.1, color=COLOR_DECODE),
            Arrow(control_unit.get_left(), mem.get_bottom(), buff=0.1, color=COLOR_DECODE)
        )
        self.play(*[GrowArrow(a) for a in ctrl_arrows])
        self.wait(1)
        self.play(FadeOut(step_decode), FadeOut(desc_decode))

        # EXECUTE
        step_exec, desc_exec = mostrar_etapa("EXECUTE", YELLOW_D, "Execução da operação na ULA")
        arrow3 = Arrow(reg_ax.get_right(), alu_box.get_left(), buff=0.1, color=COLOR_EXECUTE_AX)
        arrow4 = Arrow(reg_bx.get_right(), alu_box.get_left(), buff=0.1, color=COLOR_EXECUTE_BX)
        self.play(GrowArrow(arrow3), GrowArrow(arrow4))
        self.wait(1)
        arrow5 = Arrow(alu_box.get_right(), reg_ax.get_left(), buff=0.1, color=YELLOW_D)
        self.play(GrowArrow(arrow5))
        self.wait(0.5)
        self.play(FadeOut(step_exec), FadeOut(desc_exec))

        # STORE
        step_store, desc_store = mostrar_etapa("STORE", COLOR_STORE, "O resultado é armazenado na memória final")
        arrow6 = Arrow(reg_ax.get_right(), mem_out.get_left(), buff=0.1, color=COLOR_STORE)
        self.play(GrowArrow(arrow6))
        self.wait(1)
        self.play(FadeOut(step_store), FadeOut(desc_store))

        # Mensagem final
        final_msg = Text("Demonstração do Fluxo de Dados Concluída", font_size=20)
        final_msg.to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(2)

        self.play(FadeOut(*self.mobjects))

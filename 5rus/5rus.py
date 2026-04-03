from manim import *

config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 8
config.frame_height = 8


class s7(Scene):
    def construct(self):
        # ================= STYLE =================
        self.camera.background_color = "#fbfbf8"
        text_color = "#1f3a5f"
        accent_color = "#e63946"
        font_name = "Segoe Print"
        grid_color = LIGHT_GRAY
        cell = 0.2
        fw = BOLD

        # ================= GRID =================
        grid = NumberPlane(
            x_range=[-10, 10, cell],
            y_range=[-10, 10, cell],
            background_line_style={
                "stroke_color": grid_color,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)

        # ================= RED LINE =================
        margin_x = config.frame_width / 2 - cell * 4
        red_line = Line(
            UP * config.frame_height / 2,
            DOWN * config.frame_height / 2,
            color=RED,
            stroke_width=4,
        ).move_to(RIGHT * margin_x)
        self.add(red_line)

        # ================= TITLE =================
        intro_text = Text(
             "А что, если у нас не одно число,\nа целый пример?",
             font=font_name,color=text_color, weight=fw
        ).scale(0.55).move_to(UP * 0.2)
        self.play(Write(intro_text))
        self.wait(2)
        
        image = ImageMobject("images/Thinking.png")  
        image.scale(0.9)
        image.next_to(intro_text, DOWN, buff=0.4)
        image.shift(RIGHT * 1)
        self.play(FadeIn(image, scale=0.8))
        self.wait(3)
        self.play(FadeOut(image),FadeOut(intro_text))

        title = Text(
            "Работаем только с последними цифрами",
            font=font_name, weight=fw, color=accent_color
        ).scale(0.42).to_edge(UP)

        self.play(Write(title))

        # ================= MAIN ADDITION =================
        a = Text("1234", font=font_name, weight=fw, color=text_color).scale(1)
        plus = Text("+", font=font_name, weight=fw, color=text_color).scale(1)
        b = Text("5678", font=font_name, weight=fw, color=text_color).scale(1)

        expr = VGroup(a, plus, b).arrange(RIGHT, buff=0.4).shift(UP * 0.8)

        self.play(Write(expr))

        idea = Text(
            "Смотрим только на последние цифры",
            font=font_name, color=text_color,weight=fw
        ).scale(0.37).next_to(title, DOWN, buff=0.15)

        self.play(Write(idea))

        # ================= HIGHLIGHT LAST DIGITS =================
        tail_a = Text("4", font=font_name, weight=fw, color=accent_color).scale(1.2)
        tail_b = Text("8", font=font_name, weight=fw, color=accent_color).scale(1.2)
        plus2 = Text("+", font=font_name, weight=fw, color=accent_color).scale(1.2)

        tails = VGroup(tail_a, plus2, tail_b).arrange(RIGHT, buff=0.25)
        tails.next_to(expr, DOWN, buff=0.6)

        self.play(
            TransformFromCopy(a[-1], tail_a),
            TransformFromCopy(b[-1], tail_b),
            Write(plus2),
            run_time=1
        )

        calc = VGroup(
            Text("4", font=font_name, weight=fw, color=text_color),
            Text("+", font=font_name, weight=fw, color=text_color),
            Text("8", font=font_name, weight=fw, color=text_color),
            Text("=", font=font_name, weight=fw, color=text_color),
            Text("12", font=font_name, weight=fw, color=text_color),
        ).arrange(RIGHT, buff=0.2).scale(1)
        calc.next_to(tails, DOWN, buff=0.4)

        self.play(Write(calc))

        # ================= TRANSITION =================
        self.play(
            FadeOut(tails),
            FadeOut(calc),
        )

        transition = Text(
            "А если происходит вычитание?",
            font=font_name, color=text_color,weight=fw
        ).scale(0.5)

        self.play(Write(transition))
        self.wait(0.5)
        self.play(FadeOut(transition))

        # ================= SECOND EXAMPLE =================
        num1 = Text("1243", font=font_name, weight=fw, color=text_color).scale(1)
        minus = Text("-", font=font_name, weight=fw, color=text_color).scale(1)
        num2 = Text("5687", font=font_name, weight=fw, color=text_color).scale(1)

        expr2 = VGroup(num1, minus, num2).arrange(RIGHT, buff=0.4).shift(UP * 0.8)

        self.play(Transform(expr, expr2))  

        # ================= LAST DIGITS STEP =================
        step_title = Text(
            "Берём хвосты",
            font=font_name, color=text_color, weight=fw
        ).scale(0.4).next_to(expr2, DOWN, buff=0.5)

        self.play(Write(step_title))

        t1 = Text("3", font=font_name, weight=fw, color=accent_color).scale(1.2)
        t_minus = Text("-", font=font_name, weight=fw, color=accent_color).scale(1.2)
        t2 = Text("7", font=font_name, weight=fw, color=accent_color).scale(1.2)

        tails2 = VGroup(t1, t_minus, t2).arrange(RIGHT, buff=0.25)
        tails2.next_to(step_title, DOWN, buff=0.3)

        box_small = SurroundingRectangle(
            tails2,
            color=accent_color,
            buff=0.18,
            stroke_width=2.5
        )

        self.play(
            TransformFromCopy(num1[-1], t1),
            TransformFromCopy(num2[-1], t2),
            Write(t_minus),
            Create(box_small)
        )

        # ================= BORROW IDEA =================
        borrow_text = Text(
            "3 меньше 7 → занимаем десяток",
            font=font_name, color=text_color, weight=fw
        ).scale(0.39).next_to(tails2, DOWN, buff=0.3)

        self.play(Write(borrow_text))

        # ================= TRANSFORM TO 13 - 7 =================
        new_expr = Text("13 - 7", font=font_name, weight=fw, color=text_color).scale(1.1)
        new_expr.move_to(tails2)

        box_big = SurroundingRectangle(
            new_expr,
            color=accent_color,
            buff=0.18,
            stroke_width=2.5
        )

        self.play(
            Transform(tails2, new_expr),
            Transform(box_small, box_big),
            run_time=1.2
        )
        result = Text("= 6", font=font_name, weight=fw, color=accent_color).scale(1.1)
        result.next_to(new_expr, RIGHT)

        self.play(Write(result))
        self.wait(3)

        # ================= CLEAN =================
        self.play(
            FadeOut(expr),
            FadeOut(expr2),
            FadeOut(result),
            FadeOut(box_small),
            FadeOut(title),
            FadeOut(idea),
            FadeOut(step_title),
            FadeOut(borrow_text),
            FadeOut(tails2),
        )

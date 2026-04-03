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
        font_name = "Caveat"
        grid_color = LIGHT_GRAY
        cell = 0.2
        fw=BOLD 

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
        title = MarkupText("Тапқырларға арналған қақпан", font=font_name, color=accent_color, line_spacing=1,weight=fw)\
            .scale(0.68).to_edge(UP)

        self.play(Write(title), run_time=2)
        self.wait(1.5)

        # ================= EXAMPLE =================
        example = MarkupText(
            "13×17×25×19×42×11=…?",
            font=font_name,
            color=text_color, 
            line_spacing=1, weight=fw
        ).scale(0.8)

        example.next_to(title, DOWN, buff=0.5)
        self.play(Write(example), run_time=3)

        # ================= SECRET =================
        secret = MarkupText(
            "Құпия: 5 пен жұп санды ізде",
            font=font_name,
            color=text_color, 
            line_spacing=1, weight=fw
        ).scale(0.8)

        secret.next_to(example, DOWN, buff=0.5)
        self.play(Write(secret), run_time=5)
        self.wait(2.5)

        # ================= CENTER =================
        t25 = MarkupText("25", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.6)
        t42 = MarkupText("42", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.6)
        mult = MarkupText("×", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.6)

        group = VGroup(t25, mult, t42).arrange(RIGHT, buff=0.15)
        group.next_to(secret, DOWN, buff=0.4)

        self.play(
            TransformFromCopy(example[6:8], t25),
            TransformFromCopy(example[12:14], t42),
            Write(mult)
        )
        self.wait(3)
        # ================= TRANSFORM =================
        t5 = MarkupText("5", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.9)
        t2 = MarkupText("2", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.9)
        mult2 = MarkupText("×", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.9)

        new_group = VGroup(t5, mult2, t2).arrange(RIGHT, buff=0.15)
        new_group.move_to(group)

        self.play(Transform(group, new_group))

        result10 = MarkupText("= 10", font=font_name, color=text_color, line_spacing=1, weight=fw).scale(0.9)
        result10.next_to(group, RIGHT, buff=0.2)

        self.play(Write(result10))

        zero_box = SurroundingRectangle(result10[-1], color=accent_color, buff=0.04)
        self.play(Create(zero_box))
        self.wait(2)

        # ================= ANSWER 0 =================
        answer0 = Text("Жауап: 0", font=font_name, color=accent_color, line_spacing=1, weight=fw).scale(0.8)
        answer0.next_to(group, DOWN, buff=0.45)

        box0 = SurroundingRectangle(answer0, color=accent_color, buff=0.15)

        self.play(Write(answer0), run_time=2)
        self.play(Create(box0))
        self.wait(2.5)

        # ================= SECOND BLOCK =================
        rule2 = MarkupText(
            "Егер жұп сан болмаса →",
            font="Caveat",
            color=text_color, 
            line_spacing=1, weight=fw
        ).scale(0.8)

        rule2.next_to(answer0, DOWN, buff=0.7)

        self.play(Write(rule2))

        example2 = MarkupText(
            "11×13×15×17×19=…?",
            font=font_name,
            color=text_color, 
            line_spacing=1, weight=fw
        ).scale(0.8)

        example2.next_to(rule2, DOWN, buff=0.5)
        self.play(Write(example2))

        # 🔥 ВЫДЕЛЕНИЕ 5 В 15
        five_box = SurroundingRectangle(example2[7], color=accent_color, buff=0.06)
        self.play(Create(five_box))

        # ================= ANSWER 5 =================
        answer5 = MarkupText("Жауап: 5", font="Caveat", color=accent_color, line_spacing=1, weight=fw).scale(0.8)
        answer5.next_to(example2, DOWN, buff=0.7)

        box5 = SurroundingRectangle(answer5, color=accent_color, buff=0.15)

        self.play(Write(answer5))
        self.play(Create(box5))

        self.wait(2)
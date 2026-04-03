from manim import *

# =========================
# FRAME CONFIG
# =========================
config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 8
config.frame_height = 8


class s7(Scene):
    def construct(self):
        # =============================
        # ЦВЕТА И СТИЛЬ
        # =============================
        self.camera.background_color = "#fbfbf8"
        text_color = "#1f3a5f"
        accent_color = "#e63946"
        font_name = 'Caveat'
        grid_color = LIGHT_GRAY
        cell = 0.2
        fw = BOLD 

        # =============================
        # СЕТКА
        # =============================
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

        # =============================
        # КРАСНАЯ ЛИНИЯ
        # =============================
        margin_x = config.frame_width / 2 - cell * 4
        red_line = Line(
            UP * config.frame_height / 2,
            DOWN * config.frame_height / 2,
            color=RED,
            stroke_width=4
        ).move_to(RIGHT * margin_x)
        self.add(red_line)

        # =============================CONTENT====================================

        title = Text(
            "Соңғы цифрды тап",
            font=font_name,
            color=accent_color,
            line_spacing=1, weight=fw
        ).scale(0.85).to_edge(UP)

        base = Text("2024", font=font_name, color=text_color, weight=fw)
        expo = Text("2025", font=font_name, color=text_color, weight=fw).scale(0.6)
        expo.next_to(base, UP + RIGHT, buff=0.1)
        expr = VGroup(base, expo)

        self.play(Write(title))
        self.play(Write(expr))
        self.wait(2)

        panic = Text(
            "Бұл өте үлкен сан!",
            font=font_name,
            color=text_color,
            line_spacing=1, weight=fw
        ).scale(0.75).shift(DOWN * 1)

        self.play(Write(panic))
        self.wait(1.5)

        cross = Cross(expr, color=accent_color, stroke_width=5)

        no_calc = Text(
            "Калькулятор мұны есептей алмайды",
            font=font_name,
            color=text_color,
            line_spacing=1, weight=fw
        ).scale(0.7).shift(DOWN * 1.8)

        self.play(FadeIn(cross))
        self.play(Write(no_calc))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(panic), FadeOut(no_calc), FadeOut(cross), FadeOut(expr))

        people = VGroup()
        for i in range(5):
            p = Circle(radius=0.2, color=text_color, fill_opacity=1)
            p.move_to(LEFT * (1.5 - i * 0.6))
            people.add(p)

        queue_text = Text(
            "Сандар кезек сияқты",
            font=font_name,
            color=text_color,
            line_spacing=1, weight=fw
        ).scale(0.75).shift(UP * 0.8)

        self.play(FadeIn(people))
        self.play(Write(queue_text))
        self.wait(2)

        last_highlight = people[-1].copy().set_color(accent_color)

        self.play(Transform(people[-1], last_highlight))
        self.wait(2)

        self.play(FadeOut(people), FadeOut(queue_text))

        base2 = Text("2024", font=font_name, color=text_color, weight=fw)
        expo2 = Text("2025", font=font_name, color=text_color, weight=fw).scale(0.6)
        expo2.next_to(base2, UP + RIGHT, buff=0.1)
        expr2 = VGroup(base2, expo2)
        self.play(Write(expr2))

        last_digit_box = SurroundingRectangle(
            base2[-1],
            color=accent_color,
            buff=0.08
        )

        tail_text = Text(
            "Тек соңғы цифрға қараймыз",
            font=font_name,
            color=text_color,
            line_spacing=1, weight=fw
        ).scale(0.75).shift(DOWN * 1.2)

        self.play(FadeIn(last_digit_box))
        self.play(Write(tail_text))
        self.wait(1)

        final = Text(
            "Бұл — қарапайым ойын!",
            font=font_name,
            color=accent_color,
            line_spacing=1, weight=fw
        ).scale(0.75).shift(DOWN * 0.5)

        self.play(FadeOut(expr2), FadeOut(last_digit_box), FadeOut(tail_text))
        self.play(Write(final))
        self.play(FadeOut(final))
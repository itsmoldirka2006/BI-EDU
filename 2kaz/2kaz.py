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
        fw = BOLD
        cell = 0.2

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
            stroke_width=4
        ).move_to(RIGHT * margin_x)
        self.add(red_line)

        # ================= FUNCTION =================
        def make_power(base, exp, result, shift_y):
            b = Text(str(base), font=font_name, color=text_color,weight=fw).scale(0.9)
            e = Text(str(exp), font=font_name, color=text_color,weight=fw).scale(0.5)

            e.next_to(b, UP + RIGHT, buff=0.05)

            power = VGroup(b, e)

            eq = Text(f" = {result}", font=font_name, color=text_color,weight=fw).scale(0.9)
            eq.align_to(b, DOWN)
            eq.shift(DOWN * 0.30)
            return VGroup(power, eq).arrange(RIGHT, buff=0.15).shift(shift_y)

        # ================= CONTENT =================

        ego = Text(
            "Өзіне тым сенімді цифрлар",
            font=font_name,
            color=accent_color,weight=fw
        ).scale(0.7).to_edge(UP)

        digits = Text(
            "0  1  5  6",
            font=font_name,
            color=text_color,weight=fw
        ).scale(1.1)

        self.play(Write(ego, run_time=1.5))
        self.play(Write(digits, run_time=2))
        self.wait(1.5)

        self.play(FadeOut(digits), FadeOut(ego))

        # ================= POWERS =================
        expr1 = make_power(5, 1, "5", UP * 1)
        expr2 = make_power(5, 2, "25", ORIGIN)
        expr3 = make_power(5, 100, "... 5", DOWN * 1)

        self.play(Write(expr1, run_time=1.8))
        self.wait(0.8)

        self.play(Write(expr2, run_time=2.2))
        self.wait(0.5)

        self.play(Write(expr3, run_time=2.8))
        self.wait(2)

        # ================= HIGHLIGHT LAST DIGITS =================
        box1 = SurroundingRectangle(expr1[-1][-1], color=accent_color, buff=0.05)
        box2 = SurroundingRectangle(expr2[-1][-1], color=accent_color, buff=0.05)
        box3 = SurroundingRectangle(expr3[-1][-1], color=accent_color, buff=0.05)

        self.play(FadeIn(box1), FadeIn(box2), FadeIn(box3))
        self.wait(2)

        self.play(
            FadeOut(expr1),
            FadeOut(expr2),
            FadeOut(expr3),
            FadeOut(box1),
            FadeOut(box2),
            FadeOut(box3)
        )

        # ================= FINAL =================
        digits2 = Text(
            "0  1  5  6",
            font=font_name,
            color=text_color,weight=fw
        ).scale(1.1)

        self.play(Write(digits2))
        self.wait(0.5)

        highlight = digits2.copy().set_color(accent_color)
        self.play(Transform(digits2, highlight))
        self.wait(0.5)

        self.play(FadeOut(digits2))

        final = MarkupText(
            "Бұл — оңай балл!",
            font=font_name,
            color=accent_color,weight=fw
        ).scale(0.6)

        self.play(Write(final))
        self.wait(1)

        self.play(FadeOut(final))
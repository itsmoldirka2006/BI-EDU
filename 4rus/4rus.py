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
            stroke_width=4
        ).move_to(RIGHT * margin_x)

        self.add(red_line)

        # ================= TITLE =================
        title = Text(
            "Самые капризные — 2, 3, 7 и 8.",
            font=font_name,
            color=accent_color,
            weight=fw
        ).scale(0.55).to_edge(UP)

        self.play(Write(title), run_time=3)
        self.wait(4)

        # ================= ЦИКЛЫ ПО ОДНОМУ =================
        cycles_data = [
            "2 → 2, 4, 8, 6",
            "3 → 3, 9, 7, 1",
            "7 → 7, 9, 3, 1",
            "8 → 8, 4, 2, 6",
        ]

        prev = None

        cycles_group = VGroup()

        for i, c in enumerate(cycles_data):

            line = Text(
                c,
                font=font_name,
                color=text_color,
                weight=fw
            ).scale(0.55)

            if prev is None:
                line.next_to(title, DOWN, buff=0.4)
            else:
                line.next_to(prev, DOWN, buff=0.25)

            prev = line
            cycles_group.add(line)

            self.play(Write(line), run_time=3)
            self.wait(0.5)

        # ================= ПОДСВЕТКА ПЕРВОГО =================
        box = SurroundingRectangle(cycles_group[0], color=accent_color, buff=0.1)
        self.play(Create(box))

        # ================= ПРАВИЛО =================
        rule = Text(
            "Степень ÷ 4 → ищем остаток",
            font=font_name,
            color=accent_color,
            weight=fw
        ).scale(0.58)

        rule.next_to(cycles_group, DOWN, buff=0.4)

        self.play(Write(rule), run_time=3)
        self.wait(2)

        # ================= ПРИМЕР =================
        example = MarkupText(
             '2<sup>7</sup> → 7 ÷ 4 = 3',
             font=font_name,
             color=text_color
        ).scale(0.8)
        example.next_to(rule, DOWN, buff=0.4)
        self.play(Write(example), run_time=3)
        self.wait(1)

        # ================= ОТВЕТ =================
        answer = Text(
            "Ответ: 8",
            font=font_name,
            color=accent_color,
            weight=fw
        ).scale(0.85)

        answer.next_to(example, DOWN, buff=0.5)

        box2 = SurroundingRectangle(answer, color=accent_color, buff=0.2)

        self.play(FadeIn(answer, scale=1.2))
        self.play(Create(box2))


        # ================= CLEAN =================
        self.play(
            FadeOut(title),
            FadeOut(cycles_group),
            FadeOut(box),
            FadeOut(rule),
            FadeOut(example),
            FadeOut(answer),
            FadeOut(box2),
            FadeOut(grid),
            FadeOut(red_line),
        )
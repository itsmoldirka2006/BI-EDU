from manim import *

# =========================
# CONFIG
# =========================
config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 8
config.frame_height = 8


class s7(Scene):
    def construct(self):
        self.camera.background_color = "#fbfbf8"

        text_color = "#1f3a5f"
        accent_color = "#e63946"
        font_name = "Caveat"
        grid_color = LIGHT_GRAY
        cell = 0.2
        fw = BOLD

        # =========================
        # СЕТКА
        # =========================
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

        # =========================
        # КРАСНАЯ ЛИНИЯ
        # =========================
        margin_x = config.frame_width / 2 - cell * 4
        red_line = Line(
            UP * config.frame_height / 2,
            DOWN * config.frame_height / 2,
            color=RED,
            stroke_width=4,
        ).move_to(RIGHT * margin_x)
        self.add(red_line)

        # ================= TITLE =================
        title = MarkupText(
            "Көбейтумен бәрі одан да оңай!",
            font=font_name,weight=fw,color=accent_color, line_spacing=1
        ).scale(0.75).to_edge(UP)
        self.play(Write(title), run_time = 2)

        # ================= RULE =================
        rule = MarkupText(
            "Соңғы цифр \n = соңғы цифрлардың көбейтіндісі",
            font=font_name,
            weight=fw,
            color=text_color, line_spacing=1
        ).scale(0.65)
        rule.next_to(title, DOWN, buff=0.2)
        self.play(Write(rule), run_time = 4)
        self.wait(0.2)

        # ================= CENTER BLOCK =================
        cond = MarkupText(
            "Егер:",
            font=font_name,
            weight=fw,
            color=text_color, line_spacing=1
        ).scale(0.75)

        example = MarkupText(
            "123 × 456 × 789",
            font=font_name,
            weight=fw,
            color=text_color
        ).scale(0.75)

        top_group = VGroup(cond, example).arrange(RIGHT, buff=0.3)
        top_group.move_to(UP * 1)

        self.play(Write(top_group), time_line= 13)
        self.wait(2)

        # ================= HIGHLIGHT 3 6 9 =================
        d3 = example[2]
        d6 = example[6]
        d9 = example[-1]

        self.play(
            d3.animate.scale(1.4).set_color(accent_color),
            d6.animate.scale(1.4).set_color(accent_color),
            d9.animate.scale(1.4).set_color(accent_color),
            run_time=3
        )
        self.wait(0.2)

        # ================= FIRST STEP =================
        three = MarkupText("3", font=font_name, weight=fw, color=accent_color)
        six = MarkupText("6", font=font_name, weight=fw, color=accent_color)
        mult1 = MarkupText("×", font=font_name, weight=fw, color=accent_color)

        expr1 = VGroup(three, mult1, six).arrange(RIGHT, buff=0.2)

        calc1 = MarkupText(
            "= 18 → 8-ді қалдырамыз",
            font=font_name,
            weight=fw,
            color=text_color
        ).scale(0.7)

        row1 = VGroup(expr1, calc1).arrange(RIGHT, buff=0.3)
        row1.next_to(top_group, DOWN, buff=0.5)

        self.play(
            TransformFromCopy(example[2], three),
            TransformFromCopy(example[6], six),
            Write(mult1)
        )
        self.play(Write(calc1), run_time= 5)
        self.wait(0.3)

        # ================= SECOND STEP =================
        eight = MarkupText("8", font=font_name, weight=fw, color=accent_color)
        nine = MarkupText("9", font=font_name, weight=fw, color=accent_color)
        mult2 = MarkupText("×", font=font_name, weight=fw, color=accent_color)

        expr2 = VGroup(eight, mult2, nine).arrange(RIGHT, buff=0.2)

        calc2 = MarkupText(
            "= 72 → 2-ні қалдырамыз",
            font=font_name,
            weight=fw,
            color=text_color
        ).scale(0.7)

        row2 = VGroup(expr2, calc2).arrange(RIGHT, buff=0.3)

        row2.align_to(row1, LEFT)
        row2.next_to(row1, DOWN, buff=0.4)

        self.play(
            TransformFromCopy(calc1[-1], eight),
            TransformFromCopy(example[-1], nine),
            Write(mult2)
        )
        self.play(Write(calc2), run_time= 3)
        self.wait(0.3)

        # ================= FINAL ANSWER =================
        answer = MarkupText(
            "Жауап: 2",
            font=font_name,
            weight=fw,
            color=accent_color
        ).scale(0.7)

        answer.next_to(row2, DOWN, buff=0.7)

        box = SurroundingRectangle(
            answer,
            color=accent_color,
            buff=0.2,
            stroke_width=3
        )

        self.play(Write(answer), run_time = 2)
        self.play(Create(box), run_time = 2)

        self.wait(3)
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
        font_name = "Caveat"
        grid_color = LIGHT_GRAY
        cell = 0.2
        # В MarkupText лучше использовать числовое значение или оставить по умолчанию
        # Если шрифт Caveat-Bold установлен, Manim его подхватит
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

        # =============================
        # ТЕКСТ (Заменен на MarkupText)
        # =============================

        # Заголовок
        title = MarkupText(
            "Оқушылардың 90%-ы қателеседі.",
            font=font_name,
            weight=fw,
            color=accent_color
        ).scale(0.7).to_edge(UP)

        # Блок 1
        block_text = VGroup(
            MarkupText("4 және 9 цифрлары — бишілер,", font=font_name, weight=fw, color=text_color),
            MarkupText("Оларда бар болғаны екі қимылы бар.", font=font_name, weight=fw, color=text_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.6)

        # Блок 2
        rule_text = VGroup(
            MarkupText("Қара: 9¹ = 9", font=font_name, weight=fw, color=text_color),
            MarkupText("9² = 81", font=font_name, weight=fw, color=text_color),
            MarkupText("9³ → қайтадан 9", font=font_name, weight=fw, color=accent_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.6)

        # 🔥 Лайфхак отдельно
        lifehack_title = MarkupText(
            "Лайфхак:",
            font=font_name,
            weight=fw,
            color=accent_color
        ).scale(0.75)

        math_text = VGroup(
            MarkupText("егер дәреже тақ болса →", font=font_name, weight=fw, color=text_color),
            MarkupText("санның өзі қалады (4 немесе 9)", font=font_name, weight=fw, color=text_color),
            MarkupText("егер жұп болса →", font=font_name, weight=fw, color=text_color),
            MarkupText("4 → 6,   9 → 1", font=font_name, weight=fw, color=accent_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.6)

        # Итог
        tail_text = VGroup(
            MarkupText("Есте сақта:", font=font_name, weight=fw, color=accent_color),
            MarkupText("жұп дәреже — «аударылу»", font=font_name, weight=fw, color=text_color),
            MarkupText("тақ дәреже — «бастапқы қалпы»", font=font_name, weight=fw, color=text_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.6)

        # =============================
        # ПОЗИЦИИ
        # =============================
        block_text.next_to(title, DOWN, buff=0.25)
        rule_text.next_to(block_text, DOWN, buff=0.22)

        lifehack_title.next_to(rule_text, DOWN, buff=0.25)
        math_text.next_to(lifehack_title, DOWN, buff=0.2)

        tail_text.next_to(math_text, DOWN, buff=0.25)

        # =============================
        # АНИМАЦИЯ
        # =============================
        self.play(Write(title), run_time=2.2)
        self.wait(0.8)

        self.play(Write(block_text[0]), run_time=2.0)
        self.play(Write(block_text[1]), run_time=2.0)
        self.wait(0.2)

        for line in rule_text:
            self.play(Write(line), run_time=2.3)
        self.wait(3)

        self.play(Write(lifehack_title), run_time=2)

        for line in math_text:
            self.play(Write(line), run_time=1.8)
            self.wait(0.5)

        self.wait(0.8)

        for line in tail_text:
            self.play(Write(line), run_time=2.0)
            self.wait(0.3)

        self.wait(0.2)
        self.play(
            FadeOut(title),
            FadeOut(block_text),
            FadeOut(rule_text),
            FadeOut(lifehack_title),
            FadeOut(math_text),
            FadeOut(tail_text),
        )
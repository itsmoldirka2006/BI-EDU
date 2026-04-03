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
        font_name = "Segoe Print"
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

        # =============================
        # ТЕКСТ
        # =============================

        # Заголовок
        title = Text(
            "90% учеников валятся.",
            font=font_name,
            weight=fw,
            color=accent_color
        ).scale(0.7).to_edge(UP)

        # Блок 1
        block_text = VGroup(
            Text("Цифры 4 и 9 — это танцоры,", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("у них всего два движения.", font=font_name, weight=fw, color=text_color, line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.5)

        # Блок 2
        rule_text = VGroup(
            Text("Смотри: 9¹ = 9", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("9² = 81", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("9³ → снова 9", font=font_name, weight=fw, color=accent_color, line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.5)

        # 🔥 Лайфхак отдельно
        lifehack_title = Text(
            "Лайфхак:",
            font=font_name,
            weight=fw,
            color=accent_color, 
            line_spacing=1
        ).scale(0.5)

        math_text = VGroup(
            Text("если степень нечётная →", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("на конце само число (4 или 9)", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("если чётная →", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("4 → 6,   9 → 1", font=font_name, weight=fw, color=accent_color, line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.5)

        # Итог
        tail_text = VGroup(
            Text("Запомни:", font=font_name, weight=fw, color=accent_color, line_spacing=1),
            Text("Чётная степень — «переворот»", font=font_name, weight=fw, color=text_color, line_spacing=1),
            Text("Нечётная — «оригинал»", font=font_name, weight=fw, color=text_color, line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.5)

        # =============================
        # ПОЗИЦИИ
        # =============================
        block_text.next_to(title, DOWN, buff=0.25)
        rule_text.next_to(block_text, DOWN, buff=0.22)

        lifehack_title.next_to(rule_text, DOWN, buff=0.25)
        math_text.next_to(lifehack_title, DOWN, buff=0.2)

        tail_text.next_to(math_text, DOWN, buff=0.25)

        # =============================
        # АНИМАЦИЯ (медленная)
        # =============================

        self.play(Write(title), run_time=2.2)
        self.wait(0.8)

        # блок 1
        self.play(Write(block_text[0]), run_time=2.0)
        self.play(Write(block_text[1]), run_time=2.0)

        self.wait(0.2)

        # блок 2
        for line in rule_text:
            self.play(Write(line), run_time=2.3)
        self.wait(3)

        # 🔥 сначала Лайфхак отдельно
        self.play(Write(lifehack_title), run_time=2)

        # потом объяснение
        for line in math_text:
            self.play(Write(line), run_time=1.8)
            self.wait(0.5)

        self.wait(0.8)

        # итог
        for line in tail_text:
            self.play(Write(line), run_time=2.0)
            self.wait(0.3)

        self.wait(1)
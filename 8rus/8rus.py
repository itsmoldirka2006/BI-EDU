from manim import *

config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 8
config.frame_height = 8


class s7(Scene):
    def construct(self):
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
        title = Text(
            "Собираем всё в один мощный алгоритм",
            font=font_name,
            weight=fw,
            color=accent_color,
            line_spacing=1
        ).scale(0.43).to_edge(UP)

        title.shift(DOWN * 0.3)  # 🔥 чуть ниже от края

        self.play(Write(title), run_time = 2)
        self.wait(1)

        # ================= ВСТУПЛЕНИЕ =================
        intro = VGroup(
            Text("Если на экзамене НИШ или РФМШ", font=font_name, color=text_color, weight=fw,line_spacing=1),
            Text("попадётся гигантское число в степени — не паникуй!", font=font_name, color=text_color, weight=fw,line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.33)

        intro.next_to(title, DOWN, buff=0.3)
        intro.to_edge(LEFT, buff=0.6)

        for line in intro:
            self.play(Write(line), run_time=2)
            self.wait(1)

        # ================= ПРАВИЛА (ОДИН СТОЛБЕЦ) =================
        rules = VGroup(
            Text("Смотри на основание:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            Text("0, 1, 5, 6 → ответ та же цифра", font=font_name, color=text_color, weight=fw,line_spacing=1),

            Text("Если 4 или 9:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            Text("смотри чётная или нечётная степень", font=font_name, color=text_color, weight=fw,line_spacing=1),

            Text("Если 2, 3, 7 или 8:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            Text("степень : 4 и смотри остаток", font=font_name, color=text_color, weight=fw,line_spacing=1),

            Text("Если много чисел:", font=font_name, color=accent_color, weight=fw, line_spacing=1),
            Text("5 × чётное число → будет 0 на конце", font=font_name, color=text_color, weight=fw, line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.38)

        rules.next_to(intro, DOWN, buff=0.35)
        rules.to_edge(LEFT, buff=0.6)

        for line in rules:
            self.play(Write(line), run_time=2.5)
            self.wait(0.5)

        all_content = VGroup(title, intro, rules)
        self.play(all_content.animate.shift(UP * 0.5))

        # ================= ФИНАЛ — ФОТО =================
        image = ImageMobject("images/Great.png") 
        image.scale(1.0)
        image.next_to(rules, DOWN, buff=0.1)
        self.play(FadeIn(image, scale=1))
        self.wait(3)
    
        self.play(
            FadeOut(title),
            FadeOut(intro),
            FadeOut(rules),
            FadeOut(image),
        )
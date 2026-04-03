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
        font_name = "Caveat"
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
        title = MarkupText(
            "Барлығын бір қуатты алгоритмге жинайық",
            font=font_name,
            weight=fw,
            color=accent_color,
            line_spacing=1
        ).scale(0.6).to_edge(UP)

        title.shift(DOWN * 0.3)  # 🔥 чуть ниже от края

        self.play(Write(title), run_time = 2)
        self.wait(1)

        # ================= ВСТУПЛЕНИЕ =================
        intro = VGroup(
            MarkupText("Егер НИШ немесе РФМШ емтиханында ", font=font_name, color=text_color, weight="BOLD",line_spacing=1),
            MarkupText("саған дәрежедегі өте үлкен сан түссе, саспа!", font=font_name, color=text_color, weight="BOLD",line_spacing=1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.45)

        intro.next_to(title, DOWN, buff=0.3)
        intro.to_edge(LEFT, buff=0.6)

        for line in intro:
            self.play(Write(line), run_time=2)
            self.wait(1)

        # ================= ПРАВИЛА (ОДИН СТОЛБЕЦ) =================
        rules = VGroup(
            MarkupText("Негізіне қара:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            MarkupText("0, 1, 5, 6 → жауап сол цифрдың өзі", font=font_name, color=text_color, weight=fw,line_spacing=1),

            MarkupText("Егер 4 немесе 9:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            MarkupText("дәреженің жұп немесе тақ екенін қара", font=font_name, color=text_color, weight=fw,line_spacing=1),

            MarkupText("Егер 2, 3, 7 немесе 8:", font=font_name, color=accent_color, weight=fw,line_spacing=1),
            MarkupText("дәрежені : 4 және қалдықты қара", font=font_name, color=text_color, weight=fw,line_spacing=1),

            MarkupText("Егер көп сандар болса:", font=font_name, color=accent_color, weight=fw, line_spacing=1),
            MarkupText("5 × жұп сан → соңында 0 болады", font=font_name, color=text_color, weight=fw),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.45)

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
        image.next_to(rules, DOWN, buff=0.01).to_edge(RIGHT, buff=0.6).shift(UP * 0.5)
        self.play(FadeIn(image, scale=0.1))
        self.wait(3)
    
        self.play(
            FadeOut(title),
            FadeOut(intro),
            FadeOut(rules),
            FadeOut(image),
        )
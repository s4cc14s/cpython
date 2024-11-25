from manim import *

class KhachkarsPresentation(Scene):
    def construct(self):
        # Заголовок с анимацией
        title = Text("Խաչքարեր", font_size=72, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Первый слайд: Введение
        intro_text = Text(
            "Խաչքարերը հայկական մշակույթի յուրահատուկ դրսևորում են։", 
            font_size=36
        )
        self.play(FadeIn(intro_text, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(intro_text))

        # Второй слайд: История
        history_title = Text("Պատմություն", font_size=48, color=YELLOW)
        self.play(Write(history_title))
        self.wait(2)
        self.play(history_title.animate.to_edge(UP))

        history_text = Text(
            "Խաչքարերի ստեղծումը սկիզբ է առել 9-10-րդ դարերում։\n"
            "Դրանք ծառայում էին որպես կրոնական և մշակութային խորհրդանիշեր։",
            font_size=32
        )
        self.play(FadeIn(history_text, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(history_title), FadeOut(history_text))

        # Третий слайд: Декоративные элементы
        elements_title = Text("Դեկորատիվ տարրեր", font_size=48, color=GREEN)
        self.play(Write(elements_title))
        self.wait(2)
        self.play(elements_title.animate.to_edge(UP))

        elements_text = Text(
            "Խաչքարերը զարդարված են բուսական, երկրաչափական և\n"
            "կրոնական թեմատիկայով պատկերներով։",
            font_size=32
        )
        self.play(FadeIn(elements_text, shift=DOWN))
        self.wait(3)

        # Пример изображения (если у вас есть файл)
        image = ImageMobject("khachkar_example.jpg").scale(0.5)
        self.play(FadeIn(image, shift=UP))
        self.wait(3)
        self.play(FadeOut(elements_title), FadeOut(elements_text), FadeOut(image))

        # Завершение
        conclusion = Text("Շնորհակալություն ուշադրության համար։", font_size=40, color=RED)
        self.play(Write(conclusion))
        self.wait(3)

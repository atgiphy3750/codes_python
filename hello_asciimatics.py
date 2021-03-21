from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Stars(screen, 100, pattern=u"⠈⠁⠂⠄⠠⠐"),
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(demo)

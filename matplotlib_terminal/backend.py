import unicodedata
import sys
import logging

import PIL.Image
import numpy as np
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backends.backend_agg import RendererAgg

import img2unicode


class MyRenderer(RendererAgg):
    def __init__(self, *args):
        super().__init__(*args)
        self.texts = []

    def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
        size = prop.get_size_in_points()
        logging.debug("Draw text %s", (gc, x, y, s, prop, angle, ismath, mtext, size, gc.get_rgb()))
        if prop.get_size_in_points() > 18:
            return super().draw_text(gc, x, y, s, prop, angle, ismath, mtext)
        else:
            self.texts.append(
                (x, y, s, size, ismath, np.array(gc.get_rgb()[:3])))

circ_numr = ord('❶')
circ_num = ord('①')

circ_letc = ord('Ⓐ')
circ_let = ord('ⓐ')
par_let = ord('⒜')
par_num = ord('⑴')
serif_num = ord('')
serif_letc = ord('')
num2_0 = ord('')
sup_num_0 = ord('')
sub_num_0 = ord('')
wide_ascii = ord('！')


optimizers = {
    'gamma': img2unicode.GammaRenderer(img2unicode.FastGammaOptimizer(True, 'no_block'), max_h=60, max_w=180, allow_upscale=True),
    'block': img2unicode.Renderer(img2unicode.FastGenericDualOptimizer('block'), max_h=60, max_w=180, allow_upscale=True),
    'braille': img2unicode.GammaRenderer(img2unicode.FastGammaOptimizer(True, 'braille'), max_h=60, max_w=180, allow_upscale=True),
}

class FigureCanvasUnicodeAgg(FigureCanvasBase):
    def __init__(self, figure, *args, **kwargs):
        # print("USING MY CUSTOM FIGURE")
        self.ua_figure = figure
        self.R = optimizers['gamma']
        super().__init__(figure, *args, **kwargs)

    def draw(self, rendering='gamma'):
        self.R = optimizers[rendering]
        w, h = self.get_width_height()
        self.renderer = MyRenderer(w, h, self.ua_figure.dpi)
        with self.renderer.lock:
            self.ua_figure.draw(self.renderer)
            super().draw()

        arr = np.asarray(self.renderer.buffer_rgba())
        img = PIL.Image.fromarray(arr, 'RGBA')
        logging.debug("Max h %s ,w %s", h, w)
        # Hax
        self.R.max_h = h/16
        self.R.max_w = w/8
        # img.save('xxx2.png')
        self.chars, self.fores, self.backs = self.R.render_numpy(img)
        self.substitute_text(max(w/self.R.max_w, h/self.R.max_h/2))

    def substitute_text(self, scale):
        from img2unicode import unicodeit
        for x, y, s, size, ismath, col in self.renderer.texts:
            # print(scale, x, y, x/scale, y/(scale*2))
            xi, yi = int(round(x // scale)), int(round(y // (scale*2) ))
            # print(yi, xi, s, size)
            #     print(max(chrs.keys()))
            if ismath and True:
                s = unicodeit.replace(s[1:-1])
                print(s)
            for i, c in enumerate(s):
                char = ord(c)
                if yi >= self.chars.shape[0] or xi+i >= self.chars.shape[1]:
                    continue
                # if size < 6 and '0' <= c <= '9':
                #     if c == '0':
                #         char -= 9
                #     char += sub_num_0 - ord('0')
                if size < 8:
                    if '0' <= c <= '9':
                        char += serif_num - ord('0')
                    c2 = c.upper()
                    if 'A' <= c2 <= 'Z':
                        char = ord(c2) + serif_letc - ord('A')
                if size > 14:
                    if '!' <= c <= chr(125):
                        char += wide_ascii - ord('!')
                        # print(char)
                    elif c == ' ':
                        char = 0x3000
                    if unicodedata.east_asian_width(chr(char)) == 'F':
                        i *= 2
                        if xi+i+1 >= self.chars.shape[1]:
                            continue
                        self.chars[yi, xi + i + 1] = ord('\N{ZERO WIDTH SPACE}')
                # print("Updating ", yi, xi+i, "with", chr(char))
                self.chars[yi, xi + i] = char
                self.fores[yi, xi + i] = col * 255  # np.array((1, 1, 1))


    def print_terminal(self, rendering='gamma'):
        self.draw(rendering=rendering)
        self.R.print_to_terminal(sys.stdout, self.chars, self.fores, self.backs,
                                 **({'sentinel':''} if rendering == 'block' else {}))

    def get_default_filetype(self):
        return 'txt'

    def print_txt(self, filename_or_obj, *args, rendering='gamma', **kwargs):
        self.draw(rendering=rendering)
        self.R.print_to_terminal(filename_or_obj, self.chars, self.fores, self.backs,
                                 **({'sentinel':''} if rendering == 'block' else {}))


    def get_renderer(self, cleared=False):
        return

def show(rendering='gamma'):
    # print("SHOWING!!!")
    for manager in Gcf.get_all_fig_managers():
        manager.canvas.print_terminal(rendering=rendering)

# Expected by matplotlib.use
FigureCanvas = FigureCanvasUnicodeAgg
show = show

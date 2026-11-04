"""Confirmed scientific-figure fonts and non-cumulative size baseline."""
import matplotlib as mpl
from matplotlib import font_manager

SIZES = {'body': 10, 'axis': 10, 'tick': 9, 'legend': 9, 'panel': 11,
         'note': 9, 'direct': 8.5, 'cell': 8.3}
BORDER_PT = 1.0
BAR_EDGE = '#526475'
FAMILIES = ['Times New Roman', 'SimSun']
PALETTE = ['#42A5F5', '#FFB547', '#38C9A3', '#AC94EA', '#FF8A80', '#4DD0E1']
SEQUENTIAL = ['#F4FAFF', '#B8E1FF', '#54ACED']
DIVERGING = ['#54ACED', '#FFFEFA', '#FFBA66']


def apply_style(font_files=()):
    """Resolve the required fonts, optionally registering supplied font files."""
    for file in font_files:
        font_manager.fontManager.addfont(file)
    fonts = {}
    for name in FAMILIES:
        try:
            fonts[name] = font_manager.findfont(name, fallback_to_default=False)
        except ValueError as exc:
            raise RuntimeError(
                f'Required font unavailable: {name}. Install it for this user '
                'or supply a licensed local font file via apply_style(font_files=...).'
            ) from exc
    mpl.rcParams.update({
        'font.family': FAMILIES, 'font.size': SIZES['body'],
        'axes.labelsize': SIZES['axis'], 'axes.titlesize': SIZES['panel'],
        'xtick.labelsize': SIZES['tick'], 'ytick.labelsize': SIZES['tick'],
        'legend.fontsize': SIZES['legend'], 'legend.frameon': False,
        'axes.linewidth': BORDER_PT, 'axes.grid': False,
        'axes.prop_cycle': mpl.cycler(color=PALETTE),
        'axes.unicode_minus': False, 'mathtext.fontset': 'custom',
        'mathtext.rm': 'Times New Roman', 'mathtext.it': 'Times New Roman:italic',
        'mathtext.bf': 'Times New Roman:bold',
        'pdf.fonttype': 42, 'svg.fonttype': 'none', 'savefig.dpi': 300,
        'figure.facecolor': 'white', 'savefig.facecolor': 'white',
    })
    return fonts


def format_axes(ax):
    """Four-sided 1 pt frame without internal grids."""
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(BORDER_PT)
    ax.tick_params(direction='in', top=True, right=True, length=3.5, width=.8,
                   labelsize=SIZES['tick'])


def format_bars(ax):
    """Separate an opaque 1 pt outline from the existing bright bar fill.

    Call before creating/rebuilding a legend, so its swatches inherit the border.
    """
    from matplotlib.container import BarContainer
    for container in ax.containers:
        if not isinstance(container, BarContainer):
            continue
        for bar in container.patches:
            red, green, blue, alpha = bar.get_facecolor()
            # Bake transparency against the white canvas into the fill only.
            face = [alpha*c+(1-alpha) for c in (red, green, blue)]
            bar.set_alpha(None)
            bar.set_facecolor((*face, 1))
            bar.set_edgecolor(BAR_EDGE)
            bar.set_linewidth(BORDER_PT)
            bar.set_linestyle('solid')


if __name__ == '__main__':
    print(apply_style())

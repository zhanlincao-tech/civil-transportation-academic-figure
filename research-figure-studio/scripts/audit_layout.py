"""Mechanical figure checks, complementary to actual image inspection.

Inspired by the program/visual-review separation in scipilot-figure-skill.
This is an independent, small implementation with the user's current style rules.
It does not infer data validity or certify publication compliance.
"""
import logging
import math
import warnings

from matplotlib.container import BarContainer
from matplotlib.text import Text


class _FontMessages(logging.Handler):
    def __init__(self):
        super().__init__(level=logging.WARNING)
        self.messages=[]

    def emit(self,record):
        self.messages.append(record.getMessage())


def audit_layout(fig, min_font_pt=8.3, border_pt=1.0, target_width_mm=None):
    """Return structured findings without altering figure geometry or style.

    Canvas/tick overlap flags are review candidates, not automatic rejection.
    Text outside axes may be intentional; text outside the canvas is flagged.
    Call after adding annotations and bar styling, before exporting.
    """
    findings=[]

    def add(code,detail,severity='warning'):
        findings.append({'code':code,'severity':severity,'detail':detail})

    handler=_FontMessages(); logger=logging.getLogger('matplotlib')
    logger.addHandler(handler)
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always'); fig.canvas.draw()
        font_messages=handler.messages+[str(w.message) for w in caught]
    finally:
        logger.removeHandler(handler)
    missing=[m for m in font_messages if ('missing' in m.lower() and 'glyph' in m.lower())
             or ('findfont' in m.lower() and 'not found' in m.lower())]
    if missing: add('missing_font_or_glyph',' | '.join(dict.fromkeys(missing))[:500],'error')

    renderer=fig.canvas.get_renderer(); canvas=fig.bbox
    excluded=set()
    for ax in fig.axes:
        for axis,limits in [(ax.xaxis,ax.get_xlim()),(ax.yaxis,ax.get_ylim())]:
            lo,hi=sorted(limits)
            for tick in list(axis.get_major_ticks())+list(axis.get_minor_ticks()):
                if not lo-1e-9<=tick.get_loc()<=hi+1e-9:
                    excluded.update([id(tick.label1),id(tick.label2)])
    for text in fig.findobj(Text):
        if not text.get_visible() or not text.get_text().strip() or id(text) in excluded: continue
        content=text.get_text().replace('\n',' ')[:80]
        if text.get_fontsize()<min_font_pt-1e-6: add('small_text',content,'error')
        bb=text.get_window_extent(renderer)
        if bb.x0<canvas.x0-2 or bb.y0<canvas.y0-2 or bb.x1>canvas.x1+2 or bb.y1>canvas.y1+2:
            add('canvas_clipping',content)
    for i,ax in enumerate(fig.axes):
        if ax.axison:
            for side,spine in ax.spines.items():
                if spine.get_visible() and not math.isclose(spine.get_linewidth(),border_pt,abs_tol=1e-6):
                    add('frame_width',f'axes {i}, {side}: {spine.get_linewidth()} pt','error')
        for direction,labels in [('x',ax.get_xticklabels()),('y',ax.get_yticklabels())]:
            boxes=[t.get_window_extent(renderer) for t in labels if t.get_visible() and t.get_text().strip() and id(t) not in excluded]
            boxes.sort(key=lambda b:b.x0 if direction=='x' else b.y0)
            for left,right in zip(boxes,boxes[1:]):
                width=min(left.x1,right.x1)-max(left.x0,right.x0)
                height=min(left.y1,right.y1)-max(left.y0,right.y0)
                if width>1 and height>1:
                    add('tick_overlap',f'axes {i}, {direction}'); break
        for container in ax.containers:
            if not isinstance(container,BarContainer): continue
            for bar in container.patches:
                if not math.isclose(bar.get_linewidth(),border_pt,abs_tol=1e-6) or bar.get_edgecolor()[3]<.999:
                    add('bar_outline',f'axes {i}: opaque {border_pt:g} pt outline required','error'); break
                if sum(abs(x-y) for x,y in zip(bar.get_edgecolor()[:3],bar.get_facecolor()[:3]))<.03:
                    add('bar_outline_contrast',f'axes {i}: border and fill are nearly identical'); break
    if target_width_mm is not None:
        actual=float(fig.get_figwidth()*25.4)
        if not math.isclose(actual,target_width_mm,abs_tol=.1):
            add('canvas_width',f'{actual:.2f} mm; expected {target_width_mm:.2f} mm','error')
    return findings

"""Render a bilingual example with synthetic paired observations."""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from audit_layout import audit_layout
from style_defaults import apply_style, format_axes, PALETTE


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--font', type=Path, action='append', default=[])
    args = parser.parse_args()
    fonts = apply_style(args.font)
    args.out.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.2, 3.1))
    fig.subplots_adjust(left=.15, right=.96, bottom=.24, top=.81)
    reference = [12, 19, 24, 31]
    revised = [15, 24, 27, 38]
    positions = list(range(len(reference)))
    for y, start, end in zip(positions, reference, revised):
        ax.plot([start, end], [y, y], color='#9FB0BF', lw=1.2, zorder=1)
    for values, marker, color, label in (
        (reference, 'o', PALETTE[0], '基准'),
        (revised, 's', PALETTE[1], '比较条件'),
    ):
        ax.plot(values, positions, ls='none', marker=marker, mfc='white',
                mec=color, mew=1.2, ms=5.8, label=label)
    ax.set(xlim=(0, 45), ylim=(3.5, -.5), yticks=positions,
           yticklabels=['A', 'B', 'C', 'D'], xlabel='响应 / kPa', ylabel='试件编号')
    ax.legend(ncol=2, loc='lower left', bbox_to_anchor=(0, 1.03), borderaxespad=0)
    format_axes(ax)
    fig.text(.15, .055, '合成数据。仅用于检查图型、字体及导出。', fontsize=9)
    findings = audit_layout(fig)
    if findings:
        raise SystemExit(f'Figure audit failed: {findings}')
    for ext in ('png', 'pdf', 'svg'):
        fig.savefig(args.out / f'paired-demo.{ext}', dpi=300)
    plt.close(fig)
    print('Fonts:', ', '.join(fonts))
    print('Created paired-demo.png, paired-demo.pdf and paired-demo.svg')


if __name__ == '__main__':
    main()

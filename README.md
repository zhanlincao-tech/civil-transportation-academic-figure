# Research Figure Studio

适用于论文、学位论文和技术报告的科研绘图 Skill。按问题选择图型，覆盖概念和机理、工程剖面、柱状与折线、散点与分布、热图与空间、有向网络、配对与区间、概率曲线和时频图。默认使用亮色白底、中文宋体、英文及数字 Times New Roman、1 磅图框和柱体边线、少量数值标注。

## 换电脑使用

1. 解压安装包。找到内部的 `research-figure-studio` 文件夹，确认它的直接下级就是 `SKILL.md`。
2. 把整个文件夹复制到下列对应位置。父目录不存在时可新建。个人安装与项目安装任选一种，同名旧版先移到技能目录之外备份。

| 范围 | 路径 |
|---|---|
| Windows，个人使用 | `%USERPROFILE%\.agents\skills\research-figure-studio\SKILL.md` |
| macOS / Linux，个人使用 | `~/.agents/skills/research-figure-studio/SKILL.md` |
| 某个项目共享 | `项目根目录/.agents/skills/research-figure-studio/SKILL.md` |

3. 在另一台电脑的 Codex 新对话中输入以下指令。如果技能未出现在选择列表，重新启动 Codex。 [OpenAI 官方安装路径](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

> 使用 $research-figure-studio。先检查我给的数据和比较对象，再画图。输出 300 dpi PNG、PDF、SVG 和可复现的绘图脚本。

## 在另一台电脑验证出图

安装包里的说明文件可直接由 Codex 读取。要运行随附 Python 绘图和数据检查脚本，先在包含本 README 的目录安装依赖。建议使用 Python 3.11。Windows 的 Python 启动器也可用 `py -3.11` 代替 `python`。

```text
python -m pip install -r requirements.txt
python research-figure-studio/scripts/smoke_render.py --out demo-output
```

示例会用合成数据生成配对图，输出 PNG、PDF 和 SVG。脚本会检查两种字体是否可用。请在新电脑上安装有授权的 SimSun 和 Times New Roman。若字体文件已合法取得，也可给示例命令重复传入 `--font`，分别指定两个文件的本机路径。SVG 保留可编辑文字，接收方查看 SVG 时也需相应字体。PDF 嵌入字体，可用于核对版式。安装包采用公开论文链接和图号作为参照。

## 分享或上传 GitHub

- 直接分享这个 ZIP 即可，接收者按上方说明安装。
- GitHub 网页上传时，先把 ZIP 解压到独立目录，再创建名为 `research-figure-studio` 的仓库。建议先选 **Private**。在仓库的 **Add file → Upload files** 上传解压出的 **README.md、requirements.txt 和 research-figure-studio 文件夹**，提交后检查仓库内有 `research-figure-studio/SKILL.md`。私有仓库可以在设置里邀请指定协作者。 [创建仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) · [邀请协作者](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/inviting-collaborators-to-a-personal-repository)
- 从 GitHub 获取时可用仓库的 **Code → Download ZIP**，解压后复制内部技能文件夹到技能目录。

仓库可共享的内容是本 Skill 的规则、通用脚本、合成数据示例和安装说明。需要为别人的论文绘图时，单独提供其获准使用的数据和结构参数。沉井条目是原项目确认的施工阶段约束，迁移到其他工程前应按该工程资料核对。

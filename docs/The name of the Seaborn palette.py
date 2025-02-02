import seaborn as sns
import matplotlib.pyplot as plt

# 获取所有 Seaborn 调色板的名称
palette_names = [
    "deep", "muted", "bright", "pastel", "dark", "colorblind",
    "husl", "hls", "Set1", "Set2", "Set3", "tab10", "tab20",
    "tab20b", "tab20c", "Paired", "Accent", "Spectral"
]

# 计算调色板的数量
num_palettes = len(palette_names)

# 计算需要的图片数量（每张图片显示4个调色板）
num_images = (num_palettes + 3) // 4  # 每个图片包含4个子图

# 遍历每个图片
for image_idx in range(num_images):
    # 计算当前图片中的调色板范围
    start_idx = image_idx * 4
    end_idx = min(start_idx + 4, num_palettes)
    current_palette_names = palette_names[start_idx:end_idx]
    num_current_palettes = len(current_palette_names)

    # 创建一个图形对象和一组子图（axes），子图的数量等于当前图片中的调色板数量
    # 每个子图占据一行，列数为1
    # 图形的宽度为8英寸，高度为每个子图2英寸乘以调色板的数量
    fig, axes = plt.subplots(nrows=num_current_palettes, ncols=1, figsize=(8, 2 * num_current_palettes))

    # 如果只有一个子图，axes 不是数组，需要转换为数组
    if num_current_palettes == 1:
        axes = [axes]

    # 遍历每个调色板并绘制
    for ax, palette_name in zip(axes, current_palette_names):
        # 获取调色板
        palette = sns.color_palette(palette_name)
        num_colors = len(palette)

        # 绘制调色板
        for i, color in enumerate(palette):
            ax.bar(i, 1, color=color, width=1)  # 使用 bar 绘制色块

        # 在每个色块上显示颜色名称（十六进制值）
        for i, color in enumerate(palette):
            # 将 RGB 颜色转换为十六进制格式
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)
            )
            # 在色块上显示颜色名称，并设置旋转角度为90度
            ax.text(i, 0.5, hex_color, color='black' if color[0] + color[1] + color[2] > 1.5 else 'white',
                    fontsize=8, ha='center', va='center', rotation=45)

        # 设置标题
        ax.set_title(f"Seaborn Palette: {palette_name}", fontsize=12, pad=10)

        # 隐藏坐标轴
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-0.5, num_colors - 0.5)
        ax.set_ylim(0, 1)

    # 调整布局
    plt.tight_layout()

    # 保存图片
    plt.savefig(
        f'../output/images/Seaborn_Palettes_{image_idx + 1}.png',  # 保存图片的路径
        dpi=500,  # 设置图片的分辨率
        bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
        facecolor='white'  # 设置保存图片的背景颜色为白色
    )

    # 显示图像
    plt.show()
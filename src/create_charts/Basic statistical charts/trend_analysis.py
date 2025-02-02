import pandas as pd
import matplotlib.pyplot as plt
from math import pi

class ComparisonVisualization:
    def __init__(self, data_file):
        """
        初始化 ComparisonVisualization 类

        :param data_file: 数据文件路径，CSV格式
        """
        # 使用 pandas 读取 CSV 文件并存储为 DataFrame
        self.df = pd.read_csv(data_file)

    def plot_bar_chart(self):
        """
        绘制柱状图，用于不同产品的销量对比
        """
        # 创建一个新的图形窗口，设置大小为 10x6 英寸
        plt.figure(figsize=(10, 6))

        # 绘制柱状图，使用 'Product' 列作为 x 轴，'Sales' 列作为 y 轴，颜色为浅蓝色
        plt.bar(self.df['Product'], self.df['Sales'], color='skyblue')

        # 设置图表标题，字体大小为 16
        plt.title('Product Sales Comparison (Bar Chart)', fontsize=16)

        # 设置 x 轴标签
        plt.xlabel('Product')

        # 设置 y 轴标签
        plt.ylabel('Sales')

        # 旋转 x 轴标签 45 度以避免重叠
        plt.xticks(rotation=45)

        # 添加网格线，样式为虚线，透明度为 0.6
        plt.grid(True, linestyle='--', alpha=0.6)

        # 自动调整布局以防止标签被裁剪
        plt.tight_layout()

        plt.savefig(
            '../../../output/images/bar_chart.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率

        # 显示图表
        plt.show()

    def plot_horizontal_bar_chart(self):
        """
        绘制条形图，用于国家GDP排名
        """
        # 创建一个新的图形窗口，设置大小为 10x6 英寸
        plt.figure(figsize=(10, 6))

        # 绘制水平条形图，使用 'Product' 列作为 y 轴，'GDP' 列作为 x 轴，颜色为浅绿色
        plt.barh(self.df['Product'], self.df['GDP'], color='lightgreen')

        # 设置图表标题，字体大小为 16
        plt.title('GDP Ranking (Horizontal Bar Chart)', fontsize=16)

        # 设置 x 轴标签
        plt.xlabel('GDP')

        # 设置 y 轴标签
        plt.ylabel('Product')

        # 添加网格线，样式为虚线，透明度为 0.6
        plt.grid(True, linestyle='--', alpha=0.6)

        # 自动调整布局以防止标签被裁剪
        plt.tight_layout()

        plt.savefig(
            '../../../output/images/horizontal_bar_chart.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率

        # 显示图表
        plt.show()

    def plot_radar_chart(self):
        """
        绘制雷达图，用于多维数据对比（如能力评估/产品属性对比）
        """
        # 提取属性数据，假设数据集中有 5 个属性列
        categories = [f'Attribute_{i+1}' for i in range(5)]
        values = self.df[categories].values.tolist()

        # 计算角度，使每个属性均匀分布在一个圆周上
        angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
        angles += angles[:1]  # 闭合雷达图的角度

        # 创建子图，使用极坐标系
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

        # 遍历每个产品，绘制其对应的雷达图
        for i, product in enumerate(self.df['Product']):
            value = values[i] + [values[i][0]]  # 闭合雷达图的数据
            ax.plot(angles, value, linewidth=1, label=product)  # 绘制折线
            ax.fill(angles, value, alpha=0.25)  # 填充区域

        # 添加图例，位置在右上角，稍微偏移
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # 设置雷达图的起始角度为 90 度（即从顶部开始）
        ax.set_theta_offset(pi / 2)

        # 设置雷达图的方向为逆时针
        ax.set_theta_direction(-1)

        # 设置 x 轴标签为属性名称
        plt.xticks(angles[:-1], categories)

        # 设置径向标签的位置
        ax.set_rlabel_position(30)

        # 设置图表标题，位置稍微高一些
        plt.title('Product Attributes Comparison (Radar Chart)', y=1.1, fontsize=16)

        plt.savefig(
            '../../../output/images/radar_chart.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率

        # 显示图表
        plt.show()

# 使用示例：
if __name__ == "__main__":
    # 创建 ComparisonVisualization 对象并传入数据文件路径
    viz = ComparisonVisualization('../../../data/raw_data/trend_analysis.csv')

    # 绘制柱状图
    viz.plot_bar_chart()

    # 绘制条形图
    viz.plot_horizontal_bar_chart()

    # 绘制雷达图
    viz.plot_radar_chart()

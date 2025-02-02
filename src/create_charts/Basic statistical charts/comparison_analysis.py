import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ChartCreator:
    def __init__(self, data_path):
        """
        初始化ChartCreator类的实例。

        参数:
        data_path (str): 包含数据的CSV文件的路径。
        """
        self.df = pd.read_csv(data_path)  # 读取CSV文件并存储在DataFrame中

    def plot_histogram(self):
        """
        绘制并保存数据的直方图。

        直方图用于显示数据的分布情况。
        """
        sns.set_palette("husl")  # 设置直方图的调色板为 husl
        plt.figure(figsize=(12, 8))  # 创建一个12x8英寸的图形
        ax = sns.histplot(
            self.df['Value'],  # 使用 'Value' 列的数据
            bins=15,  # 将数据分成15个区间
            kde=True,  # 显示核密度估计曲线
            color='c',  # 设置直方图的颜色为青色
            edgecolor='black'  # 设置直方图柱子的边缘颜色为黑色
        )  # 绘制直方图
        ax.grid(True, alpha=0.7)  # 添加网格线，透明度为0.7
        plt.title('Histogram of Value', fontsize=18, pad=15, fontweight='bold')  # 设置图表标题，字体大小为18，与图表顶部的距离为15，字体加粗
        plt.xlabel('Value', fontsize=14, labelpad=10)  # 设置x轴标签，字体大小为14，与x轴的距离为10
        plt.ylabel('Frequency', fontsize=14, labelpad=10)  # 设置y轴标签，字体大小为14，与y轴的距离为10
        plt.savefig(
            '../../../output/images/histogram.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        plt.show()  # 显示图表

    def plot_density(self):
        """
        绘制并保存数据的密度图。

        密度图用于显示数据的概率密度分布。
        """
        sns.set_palette("mako")  # 设置密度图的调色板为 mako
        plt.figure(figsize=(10, 6))  # 创建一个10x6英寸的图形
        ax = sns.kdeplot(
            self.df['Value'],  # 使用 'Value' 列的数据
            fill=True,  # 填充密度曲线下的区域
            color='c',  # 设置密度曲线的颜色为青色
            alpha=0.7  # 设置密度曲线的透明度为0.7
        )  # 绘制密度图
        ax.grid(True, alpha=0.5)  # 添加网格线，透明度为0.5
        plt.title('Density Plot of Value', fontsize=18, pad=15, fontweight='bold')  # 设置图表标题，字体大小为18，与图表顶部的距离为15，字体加粗
        plt.xlabel('Value', fontsize=14, labelpad=10)  # 设置x轴标签，字体大小为14，与x轴的距离为10
        plt.ylabel('Density', fontsize=14, labelpad=10)  # 设置y轴标签，字体大小为14，与y轴的距离为10
        plt.savefig(
            '../../../output/images/density_plot.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        plt.show()  # 显示图表

    def plot_boxplot(self):
        """
        绘制并保存数据的箱线图。

        箱线图用于显示数据的分布情况，包括中位数、四分位数和异常值。
        """
        sns.set_palette("Set2")  # 设置箱线图的调色板为 Set2
        plt.figure(figsize=(10, 6))  # 创建一个10x6英寸的图形

        # 绘制箱线图
        ax = sns.boxplot(
            x='Category',  # 使用 'Category' 列作为x轴
            y='Value',  # 使用 'Value' 列作为y轴
            data=self.df,  # 使用的数据集
            hue='Category',  # 使用 'Category' 列作为颜色区分
            palette="Set2",  # 设置调色板为 Set2
            showfliers=True  # 显示异常值
        )
        ax.grid(True, axis='y', alpha=0.5)  # 添加y轴方向的网格线，透明度为0.5
        plt.title('Boxplot of Value by Category', fontsize=18, pad=15,
                  fontweight='bold')  # 设置图表标题，字体大小为18，与图表顶部的距离为15，字体加粗
        plt.xlabel('Category', fontsize=14, labelpad=10)  # 设置x轴标签，字体大小为14，与x轴的距离为10
        plt.ylabel('Value', fontsize=14, labelpad=10)  # 设置y轴标签，字体大小为14，与y轴的距离为10
        plt.savefig(
            '../../../output/images/boxplot.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        plt.show()  # 显示图表

    def plot_violin(self):
        """
        绘制并保存数据的小提琴图。

        小提琴图用于显示数据的分布情况，结合了箱线图和密度图的优点。
        """
        sns.set_palette("muted")  # 设置小提琴图的调色板为 muted
        plt.figure(figsize=(10, 6))  # 创建一个10x6英寸的图形
        ax = sns.violinplot(
            x='Category',  # 使用 'Category' 列作为x轴
            y='Value',  # 使用 'Value' 列作为y轴
            data=self.df,  # 使用的数据集
            hue='Category',  # 使用 'Category' 列作为颜色区分
            palette="muted",  # 设置调色板为 muted
            bw_method=0.5  # 设置核密度估计的带宽
        )  # 绘制小提琴图
        ax.grid(True, axis='y', alpha=0.5)  # 添加y轴方向的网格线，透明度为0.5
        plt.title('Violin Plot of Value by Category', fontsize=18, pad=15, fontweight='bold')  # 设置图表标题，字体大小为18，与图表顶部的距离为15，字体加粗
        plt.xlabel('Category', fontsize=14, labelpad=10)  # 设置x轴标签，字体大小为14，与x轴的距离为10
        plt.ylabel('Value', fontsize=14, labelpad=10)  # 设置y轴标签，字体大小为14，与y轴的距离为10
        plt.savefig(
            '../../../output/images/violin_plot.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        plt.show()  # 显示图表


if __name__ == "__main__":
    """
    主程序入口。

    实例化ChartCreator类并调用其方法来生成各种图表。
    """
    chart_creator = ChartCreator('../../../data/raw_data/comparison_analysis.csv')
    chart_creator.plot_histogram()
    chart_creator.plot_density()
    chart_creator.plot_boxplot()
    chart_creator.plot_violin()

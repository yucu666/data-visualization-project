import pandas as pd
import matplotlib.pyplot as plt

class TrendVisualization:
    def __init__(self, data_file):
        """
        初始化 TrendVisualization 类
        :param data_file: 数据文件路径，CSV格式
        """
        # 读取CSV文件中的数据
        self.df = pd.read_csv(data_file)
        # 确保日期列是 datetime 类型，以便更好地处理日期数据
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def plot_line_chart(self):
        """
        使用 plt 绘制折线图，展示三列市场销量随时间的变化
        """
        # 创建一个新的图形，设置大小为14x8英寸
        plt.figure(figsize=(14, 8))
        # 绘制 Market_Sales_1 的折线图，颜色为蓝色，标记为圆圈
        plt.plot(self.df['Date'], self.df['Market_Sales_1'], label='Market Sales 1', color='b', marker='o', linewidth=3, linestyle='-')
        # 绘制 Market_Sales_2 的折线图，颜色为绿色，标记为星号
        plt.plot(self.df['Date'], self.df['Market_Sales_2'], label='Market Sales 2', color='g', marker='*', linewidth=3, linestyle='--')
        # 绘制 Market_Sales_3 的折线图，颜色为红色，标记为三角形
        plt.plot(self.df['Date'], self.df['Market_Sales_3'], label='Market Sales 3', color='r', marker='^', linewidth=3, linestyle=':')
        # 设置图表标题
        plt.title('Market Sales Trends (Line Chart)', fontsize=16)
        # 设置X轴标签
        plt.xlabel('Date')
        # 设置Y轴标签
        plt.ylabel('Market Sales')
        # 旋转X轴标签以便更好地显示日期
        plt.xticks(rotation=45)
        # 显示网格线
        plt.grid(True)
        # 自动调整子图参数，使其填充整个图像区域
        plt.tight_layout()
        # 显示图例
        plt.legend()
        plt.savefig(
            '../../../output/images/line_chart.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        # 显示图表
        plt.show()

    def plot_area_chart(self):
        """
        使用 plt 绘制面积图，强调三列市场销量的累计变化
        """
        # 创建一个新的图形，设置大小为14x8英寸
        plt.figure(figsize=(14, 8))
        # 绘制堆叠面积图，颜色分别为蓝色、绿色和红色，透明度为0.6
        plt.stackplot(self.df['Date'],
                      self.df['Market_Sales_1'],
                      self.df['Market_Sales_2'],
                      self.df['Market_Sales_3'],
                      labels=['Market Sales 1', 'Market Sales 2', 'Market Sales 3'],
                      colors=['b', 'g', 'r'],
                      alpha=0.6)
        # 设置图表标题
        plt.title('Market Sales Trends (Area Chart)', fontsize=16)
        # 设置X轴标签
        plt.xlabel('Date')
        # 设置Y轴标签
        plt.ylabel('Market Sales')
        # 旋转X轴标签以便更好地显示日期
        plt.xticks(rotation=45)
        # 显示网格线
        plt.grid(True)
        # 自动调整子图参数，使其填充整个图像区域
        plt.tight_layout()
        # 显示图例
        plt.legend()
        plt.savefig(
            '../../../output/images/area_chart.png',  # 保存图片的路径
            dpi=500,  # 设置图片的分辨率
            bbox_inches='tight',  # 紧凑地保存图形，去除多余的空白
            facecolor='white'  # 设置保存图片的背景颜色为白色
        )  # 提高保存图片的分辨率
        # 显示图表
        plt.show()


if __name__ == "__main__":
    # 创建 TrendVisualization 对象并传入数据文件路径
    viz = TrendVisualization('../../../data/raw_data/distribution_analysis.csv')

    # 绘制折线图
    viz.plot_line_chart()

    # 绘制面积图
    viz.plot_area_chart()

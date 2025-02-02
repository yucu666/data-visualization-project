import pandas as pd
import numpy as np

# 设置随机种子以确保结果可复现
# 通过设置随机种子，可以确保每次运行代码时生成的随机数相同，便于调试和验证结果。
np.random.seed(10)

# 生成日期范围
# 使用 pandas 的 date_range 函数生成从 2020-01-01 开始的 12 个日期，频率为每月月底 (ME)。
dates = pd.date_range(start="2020-01-01", periods=12, freq="ME")

# 生成3列市场销量数据（模拟数据）
# 使用 numpy 的 random.randn 函数生成 12 个标准正态分布的随机数，
# * 100 + 500 对这些随机数进行缩放和平移，使得均值为 500，标准差为 100。
market_sales_1 = np.random.randn(12) * 100 + 500
market_sales_2 = np.random.randn(12) * 100 + 500
market_sales_3 = np.random.randn(12) * 100 + 500

# 创建 DataFrame
# 将生成的日期和市场份额数据组合成一个 DataFrame，列名为 'Date' 和 'Market_Share'。
df = pd.DataFrame({
    'Date': dates,
    'Market_Sales_1': market_sales_1,
    'Market_Sales_2': market_sales_2,
    'Market_Sales_3': market_sales_3
})

# 保存数据到CSV文件
# 将生成的 DataFrame 保存到指定路径的 CSV 文件中，不保存行索引。
df.to_csv('../../../data/raw_data/distribution_analysis.csv', index=False)

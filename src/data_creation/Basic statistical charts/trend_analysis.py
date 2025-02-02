import pandas as pd
import numpy as np

# 设置随机种子以确保结果可复现
np.random.seed(10)

# 生成示例数据
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],  # 定义产品名称列表
    'Sales': np.random.randint(100, 1000, size=5),  # 随机生成销量，范围在100到999之间，共5个数据点
    'GDP': np.random.randint(1000, 10000, size=5),  # 随机生成GDP，范围在1000到9999之间，共5个数据点
    'Attribute_1': np.random.rand(5),  # 随机生成属性1，范围在0到1之间，共5个数据点
    'Attribute_2': np.random.rand(5),  # 随机生成属性2，范围在0到1之间，共5个数据点
    'Attribute_3': np.random.rand(5),  # 随机生成属性3，范围在0到1之间，共5个数据点
    'Attribute_4': np.random.rand(5),  # 随机生成属性4，范围在0到1之间，共5个数据点
    'Attribute_5': np.random.rand(5),  # 随机生成属性5，范围在0到1之间，共5个数据点
}

# 创建DataFrame
df = pd.DataFrame(data)

# 定义保存路径
save_path = '../../../data/raw_data/trend_analysis.csv'

# 保存数据到 CSV 文件
df.to_csv(save_path, index=False)

import numpy as np
import pandas as pd

# 设置随机种子以确保结果可复现
np.random.seed(42)

# 生成数值型数据
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=50),
    'Value': np.random.randn(50) * 5 + 50  # 均值为50，标准差为5的正态分布
}

# 创建DataFrame
df = pd.DataFrame(data)

# 定义保存路径
save_path = '../../../data/raw_data/comparison_analysis.csv'

# 保存数据到 CSV 文件
df.to_csv(save_path, index=False)

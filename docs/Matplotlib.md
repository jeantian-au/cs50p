![[Pasted image 20260530173930.png]]
### 版块 1: Python 基础与数据准备 (Top Left, Yellow Section)

- **导入 Numpy (`import numpy as np`)**：
    - **核心功能**：处理 ndarray（N维数组），这是数据分析计算的基石。
    - **优势**：支持向量化运算，比传统的 Python 列表循环（List Iteration）科学且高效。
    - **别名 (Alias)**：`np` 是行业暗号/约定俗成，虽然可以自定义为 `my_np`，但强烈建议保留 convention。
- **数据操作**：
    - 在 DataCamp 的例子中，你成功用 Numpy 将人口数组 `np_pop` 进行了整体放大（`np_pop * 2`），直接传给 scatter 的 `s`（Size）参数，从而控制圆圈大小。

### 版块 2: VS Code 环境配置与排错 (Middle Left, Blue Section)

- **问题排查 (reportMissingModuleSource)**：
    - **表现**：代码下方出现黄色/蓝色波浪下划线（image_0.png）。
    - **根源**：VS Code 的 Pylance 插件找不到安装的库（环境未配置/库未安装）。
- **拼写错误排查 (image_1.png)**：
    - **表现**：ERROR: Could not find a version... No matching distribution found...
    - **根源**：单词拼写错误，将 `matplotlib` 拼成了 `matpltlib`（少了一个 'o'）。
- **标准解决方案流程**：
    - **终端安装**：运行 `pip3 install matplotlib numpy`（image_3.png 显示安装成功）。
    - **选择解释器 (Select Python Interpreter)**：按下 `Command + Shift + P` 调用命令面板，选择正确的 Python 版本路径。
    - Reload Window：刷新编辑器状态。
    - **忽略 Notice**：Pip 升级提示（notice）不影响现有库的使用，可以忽略。

### 版块 3: Matplotlib 核心架构 (Object Hierarchy) (Top Right, Green Section)

- **套娃结构 Artists Hierarchy**：
    - **Figure (fig)**：最顶层的“大画布”/项目看板容器，不直接画图。
    - **Axes (axs)**：最常打交道的“子面板”/坐标系（X轴+Y轴区域）。
    - **Axis**：具体的 X 轴、Y 轴标签、刻度线、网格线（.grid()）。
- **两大设计流派对比**：
    - **快捷流派 (Pyplot 状态机)**：使用 `plt.scatter()`。 Matplotlib 在后台自动帮你创建 Figure 和 Axes。代码短，适合快速探索。
    - **专业流派 (面向对象 Object-Oriented)**：使用 `fig, ax = plt.subplots()`。显式定义 `fig` 和 `ax` 对象，然后通过 `ax.` 后缀调用方法。**官方强烈推荐**在实际项目和复杂布局中使用。

### 版块 4: 高级绘图、自定义布局与方法 (Bottom Half, Orange/Purple Section)

- **自定义 3x2 多子图布局 (image_8.png comparison)**：
    - **自定义变量**：支持将名字写成 `canvas, collection = plt.subplots(...)`，但要明确哪个对应 Figure，哪个对应 Axes 列表。
    - **子图排列索引**：索引遵循从左到右、从上到下的阅读顺序，从 0 开始。
        - 第一排从左到右：`Collection[0]`, `Collection[1]`（一行两列）。
        - 第二排从左到右：`Collection[2]`, `Collection[3]`。
        - 第三排从左到右：`Collection[4]`, `Collection[5]`。
    - **操纵分图**：精准调用代码 `collection[0].plot(x, y, c="red", alpha=0.5)` 控制某张子图的外观。
- **Charting 方法 (image_10.png comparison)**：
    - **`.plot(x, y)`**：生成**折线图**，用于展示随时间或步骤的趋势（Trend）。
    - **`.scatter(x, y)`**：生成**散点图**，用于展示两个变量之间的相关性（Correlation）。
    - **`.hist(x)`**：生成**直方图**（只有一个主要变量输入），用于展示连续变量的频率分布（Distribution）。
- **Layout 方法 (image_10.png combination)**：
    - **`.grid(True/False)`**：用于在子图画布上添加灰色参考网格线，辅助数据读取。
```python
import matplotlib.pyplot as plt
import numpy as np

# === 80% 的图都是这个模板的变体 ===
fig, ax = plt.subplots(figsize=(8, 5))    # 创建画布 + 单个子图

ax.plot(x, y, label='line 1')              # 画图(.plot/.scatter/.hist 换这里)
ax.set_xlabel('X axis label')              # X 轴标签
ax.set_ylabel('Y axis label')              # Y 轴标签
ax.set_title('Plot Title')                 # 标题
ax.legend()                                # 图例
ax.grid(True)                              # 网格

plt.show()                                 # 显示
```

![[Screenshot 2026-05-30 at 17.55.58.png]]
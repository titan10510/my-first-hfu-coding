from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

figure, ax = plt.subplots()

# 4條line的坐標點（x,y）
line1 = [(1, 1), (2, 1)]
line2 = [(2, 1), (2, 2)]
line3 = [(2, 2), (1, 2)]
line4 = [(1, 2), (1, 1)]

#打包法
(line1_xs, line1_ys) = zip(*line1)
(line2_xs, line2_ys) = zip(*line2)
(line3_xs, line3_ys) = zip(*line3)
(line4_xs, line4_ys) = zip(*line4)

# 創建4條線，並添加
ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='b'))
ax.add_line(Line2D(line2_xs, line2_ys, linewidth=1, color='r'))

ax.add_line(Line2D(line3_xs, line3_ys, linewidth=1, color='k'))
ax.add_line(Line2D(line4_xs, line4_ys, linewidth=1, color='y'))

# 展示
plt.plot()
plt.show()
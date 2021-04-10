if __name__ == "__main__":
    from timeit import Timer
    import matplotlib.pyplot as plt

    l = list(range(400))
    time_all = []
    for i in range(400):
        t_for_index = Timer(stmt="l[%d]" % i, setup="from __main__ import l")
        time_all.append(t_for_index.timeit(100000))

    # 以索引为x轴、索引时间为y轴绘制散点图，可见索引时间随索引序号变化的波动不大
    plt.scatter(l, time_all, color='r', marker='+')
    plt.show()




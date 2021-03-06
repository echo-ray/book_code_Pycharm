# -*- coding: utf-8 -*-
"""
    数据预处理
    ~~~~~~~~~~~~~~~~

    过滤式特征选择

    :copyright: (c) 2016 by the huaxz1986.
    :license: lgpl-3.0, see LICENSE for more details.
"""

from sklearn.feature_selection import *


def test_VarianceThreshold():
    '''
    测试 VarianceThreshold  的用法

    :return:  None
    '''
    X = [[100, 1, 2, 3],
         [100, 4, 5, 6],
         [100, 7, 8, 9],
         [101, 11, 12, 13]]
    selector = VarianceThreshold(1)
    selector.fit(X)
    print("Variances is %s" % selector.variances_)
    print("After transform is %s" % selector.transform(X))
    print("The surport is %s" % selector.get_support(True))
    print("After reverse transform is %s" %
          selector.inverse_transform(selector.transform(X)))


def test_SelectKBest():
    '''
    测试 SelectKBest  的用法，其中考察的特征指标是 f_classif

    :return:  None
    '''
    X = [[1, 2, 3, 4, 5],
         [5, 4, 3, 2, 1],
         [3, 3, 3, 3, 3, ],
         [1, 1, 1, 1, 1]]
    y = [0, 1, 0, 1]
    print("before transform:", X)
    selector = SelectKBest(score_func=f_classif, k=3)
    selector.fit(X, y)
    print("scores_:", selector.scores_)
    print("pvalues_:", selector.pvalues_)
    print("selected index:", selector.get_support(True))
    print("after transform:", selector.transform(X))

def test_SelectPercentile():
    '''
    测试 SelectPercentile  的用法，其中考察的特征指标是 f_classif

    :return:  None
    '''
    X = [[1, 2, 3, 4, 5],
         [5, 4, 3, 2, 1],
         [3, 3, 3, 3, 3, ],
         [1, 1, 1, 1, 1]]
    y = [0, 1, 0, 1]
    print("before transform:", X)
    selector = SelectPercentile(score_func=chi2, percentile=50) # percentile=50 保留50%
    selector.fit(X, y)
    print("scores_:", selector.scores_)
    print("pvalues_:", selector.pvalues_)
    print("selected index:", selector.get_support(True))
    print("after transform:", selector.transform(X))

"""
统计函数:
f_classif:基于方差分析ANOVA,依靠F-分布的依据,利用平方和与自由度所计算的组间与组内均方估计出F值,适用于分类问题

chi2:计算卡方统计量,适用于分类问题

f_regression:基于线性回归分析来计算统计指标,适用于回归问题
"""


if __name__ == '__main__':
    test_VarianceThreshold()  # 调用 test_VarianceThreshold
    test_SelectKBest() # 调用 test_SelectKBest
    test_SelectPercentile()

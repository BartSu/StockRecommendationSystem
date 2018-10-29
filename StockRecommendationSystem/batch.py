#!/usr/bin/env python3
"""Example of using nbparameterise API to substitute variables in 'batch mode'
"""
# NYSE：New York Stock Exchange 纽约证券交易所
# 二十支股票：
# GOOG谷歌,TSLA特斯拉,AAPL苹果,AMZN亚马逊,MSFT微软,NVDA英伟达,INTC英特尔,QCOM高通,WDC西部数据,AMD超威,ORCL甲骨文,SAP思爱普,CSCO思科,BABA阿里巴巴,NOK诺基亚,T美国电话电报公司,VZ微讯,FB脸书,TWTR推特,SNAP色拉布

from nbparameterise import extract_parameters, parameter_values, replace_definitions
import nbformat

stock_names = ['GOOG','TSLA','AAPL','AMZN','MSFT','NVDA','INTC','QCOM','WDC','AMD','ORCL','SAP','CSCO','BABA',
           'NOK','T','VZ','FB','TWTR','SNAP']

with open("StockRecommendationSystem.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

orig_parameters = extract_parameters(nb)

for name in stock_names:
    print("Running for stock", name)

    # Update the parameters and run the notebook
    params = parameter_values(orig_parameters, stock=name)
    new_nb = replace_definitions(nb, params)

    # Save
    with open("StockRecommendationSystem %s.ipynb" % name, 'w') as f:
        nbformat.write(new_nb, f)

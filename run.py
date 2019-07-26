import os
import time
import unittest
import HTMLTestRunner


def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    # 测试用例均使用"test_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


cases = get_test_cases('testcase')
now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
test_reports_address = 'report'      # 测试报告存放位置
filename = 'report/' + now + 'report.html'  # 设置报告文件名
if not os.path.exists(test_reports_address):
    os.makedirs(test_reports_address)
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Web自动化测试', description=u'详细测试结果如下:')
runner.run(cases)
fp.close()
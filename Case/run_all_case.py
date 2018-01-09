import unittest,os,time,sys
import HTMLTestReportEN
path = os.path.basename(os.path.abspath("."))
cases = dict()
for case in os.listdir("."):
    if ".py" not in case and "report" not in case:
        abspath = os.path.join(os.path.abspath("."),case)
        for abscase in os.listdir(abspath):
            if "Test" in abscase:
                value = abscase.replace(".py","")
                key = ".".join([path,case,value])
                cases[key] = value
names = locals()
caselist = []
for case in cases:
    x = case
    y = cases[case]
    caselist.append(y)
    names[y] = __import__(x,fromlist=[y])

print(caselist)


suit = unittest.TestSuite()
for i in caselist:
    suit.addTest(eval(i+"."+i)("Test"))
run = unittest.TextTestRunner()
run.run(suit)


def allcase(TestCases):
    testunit=unittest.TestSuite()
    testunit.addTests(TestCases)
    runner = unittest.TextTestRunner()
    result = runner.run(TestCases)

if __name__ == '__main__':
    now = str(time.strftime("%Y-%m%d0%H%M%S",time.localtime()))
    report_abspath = os.path.join(report,"result_"+now+".html")
    with open(report_abspath,"wb") as fp:
        runner = HTMLTestReportEN.HTMLTestRunner(stream=sys.stdout,title="自动化测试",description="测试结果如下：")
        retures = runner.run()
        print(retures.success_count)
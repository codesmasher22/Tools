import speedtest
speedTest = speedtest.Speedtest() 
print(speedTest.get_best_server())
print(speedTest.download())
print(speedTest.upload())
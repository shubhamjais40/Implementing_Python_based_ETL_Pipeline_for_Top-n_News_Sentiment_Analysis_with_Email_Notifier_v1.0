import sys
sys.path.append(r'C:\Users\cvb\Documents\automation_python\etl_python\src')
sys.path.append(r'C:\Users\cvb\Documents\automation_python\etl_python\loaded_data')
import importlib

#tester = importlib.import_module('test')
import test ,hello

#print(sys.path)

print(test.sumif(2,3))

#hello.greet("munmun")
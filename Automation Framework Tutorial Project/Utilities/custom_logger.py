import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    getLogger = logging.getLogger(loggerName)

    #By default log all messages
    getLogger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("C:\\Users\\glend\\workspace_python\\Automation Framework Tutorial Project\\Logs\\all_project_logs.log", mode = 'a')
    fileHandler.setLevel(logLevel)  #File handler will override line 10

    formatter = logging.Formatter('%(asctime)s: %(name)s : %(levelname)s: %(message)s', datefmt="%m/%d/%y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    getLogger.addHandler(fileHandler)

    return getLogger
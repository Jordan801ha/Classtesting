try: 
    import MyLibrary

    iCount = 245
    NumTests = 0

    sName = "Alfalfa"

  #  fAve = iCount/iNumTests  
   # print(fAve)
   # print(sName[15])
   # fNewFile = open("test")
except ImportError:
    print("cannot load module")
except ZeroDivisionError: 
    print("dividing by zero")
except NameError:
    print("Cannot find variable")
except IndexError:
    print("String variable having problems")
except FileNotFoundError
    print("Test file does not exist")
except Exception as eError:
    print("eError")            
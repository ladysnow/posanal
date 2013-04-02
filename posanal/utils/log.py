
class log:  
        file = False
        stdout= False
        file = "/var/log/posanal"
        @classmethod
        def __init__(cls,msg):           
                if (cls.file):
                    fo = open(cls.file, "a")
                    fo.write(str(msg) + "\n")
                    fo.close()
                if(cls.stdout):
                    print(msg)   
                         
class error:
        active = False
        @classmethod
        def __init__(cls,msg):
            if(cls.active):
                log("Error %s" % (msg))

class warning:
        active = False
        @classmethod
        def __init__(cls,msg):
            if(cls.active):
                log("Warning %s" % (msg))

class info:
        active = False
        @classmethod
        def __init__(cls,msg): 
            if(cls.active):
                log("Info %s" % (msg))

class debug:
        active = False
        @classmethod
        def __init__(cls,msg):
            if(cls.active):
                log("Debug %s" % (msg))



                    

            
            
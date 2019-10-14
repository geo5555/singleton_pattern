class dbConnect():
    _instance = None

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("super is called")
            print("db con is established")
            cls._name = name
        return cls._instance

    # def __init__(self, name):
    #     print("db is initialized")

    def __str__(self):
        return f"db connection name is {self._name}"

    def printName(cls):
        print("connection is ", cls._name)


a = dbConnect("db1")
b = dbConnect("db2")
c = dbConnect("db3")
d = dbConnect("db4")
print(a)
print(b)
print(c)
print(d)
d.printName()

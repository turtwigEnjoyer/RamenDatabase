class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        for obj in objectList:
            print ("Ramen: ")
            for attribute, value in vars(obj).items():
                print("   -" + attribute +": "+ str(value) +"\n")



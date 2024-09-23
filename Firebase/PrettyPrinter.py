class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        for obj in objectList:
            for attribute, value in vars(obj).items():
                print("   -" + attribute +": "+ value +"\n")



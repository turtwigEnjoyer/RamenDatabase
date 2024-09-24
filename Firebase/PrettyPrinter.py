class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        for obj in objectList:
            print ("Ramen: ")
            for attribute, value in vars(obj).items():
                if attribute.startswith('_') or callable(value):
                    continue
                print("   -" + attribute +": "+ str(value) +"\n")



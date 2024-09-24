import inspect


class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        for obj in objectList:
            print ("Ramen: ")
            for attribute, value in obj.__dict__.items():
                #To prevent printing methods or internal attributes
                if attribute.startswith('_') or callable(value):
                    continue
                print("   -" + attribute +": "+ str(value))



class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        for obj in objectList:
            print ("Ramen: ")
            for attribute, value in vars(obj).items():
                #Skips methods or internal attributes
                if attribute.startswith('_') or callable(value):
                    continue
                #Skips class methods. Somehow this did not happen before
                if attribute == "from_dict":
                    continue
                print("   -" + attribute +": "+ str(value))



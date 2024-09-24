from pyparsing import empty


class PrettyPrinter:
    @staticmethod
    def print(objectList: list ):
        if len(objectList) == 0:
            print('No results')
            return
        for obj in objectList:
            print ("Ramen: ")
            for attribute, value in obj.__dict__.items():
                #Skips methods or internal attributes
                if attribute.startswith('_') or callable(value):
                    continue
                #Skips class methods. Somehow this did not happen before
                if attribute == "from_dict":
                    continue
                print("   -" + attribute +": "+ str(value))



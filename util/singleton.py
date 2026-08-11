# Decorator che rende una classe singleton: restituisce sempre la stessa istanza.
def Singleton(class_):
    instances = {}

    # Crea l'istanza al primo utilizzo, poi restituisce sempre quella esistente.
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

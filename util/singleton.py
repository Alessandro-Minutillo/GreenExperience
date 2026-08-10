'''
    Implementazione della funzione Singleton
    Implementa una funzione che, usata come decorator di una classe,
    viene eseguita prima del costruttore e istanzia l'oggetto
    solo se non è già presente un'istanza della stessa classe,
    altrimenti restituisce l'istanza già presente
'''

def Singleton(class_):
    instances = {}
    
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    
    return getinstance
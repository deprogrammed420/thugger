import random

IME_FILE = "C:\\Users\\Kiko\\Desktop\\diskordo\\\libs\\thugger\\vsi_verzi.txt"


def thugger(st_verzov=1, filter=True):
    """zgenerira verz od Young Thug-a"""
    with open(IME_FILE, 'r') as file:
        verzi = file.readlines()
        verzi_brezvrstic = [line.rstrip('\n') for line in verzi]
        vec_vrstic = []
        for i in range(st_verzov):
            random_vrstica = verzi_brezvrstic[random.randint(0, len(verzi_brezvrstic) - 1)]
            if filter:
                random_vrstica = (random_vrstica.replace("nigger", "lad")
                                  .replace("nigga", "dude")
                                  .replace("niggers", "boys")
                                  .replace("niggas", "guys")
                                  .replace("Nigger", "Lad")
                                  .replace("Nigga", "Dude")
                                  .replace("Niggers", "Boys")
                                  .replace("Niggas", "Guys"))

            vec_vrstic.append(random_vrstica)
        return '\n'.join(vec_vrstic)

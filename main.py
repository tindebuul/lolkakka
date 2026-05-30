from champ_statit import open_analytics

champ = ""

kielletty_merkki = ["'", "1"]

while (True):
        champ = input("Ketä pelaat: ")
        
        champ = champ.strip().replace(" ", "")
                                      
        for i in kielletty_merkki:
            champ = champ.replace(i, "")

        if champ == "exit":
            break

        open_analytics(champ)




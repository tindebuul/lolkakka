from champ_statit import open_analytics

champ = ""

while (True):
        champ = input("Ketä pelaat: ")

        if champ == "exit":
            break

        open_analytics(champ)




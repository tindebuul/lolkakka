from champ_statit import open_analytics

champ = ""

kielletty_merkki = ["'", " "]


     
while (True):
        champ = input("Ketä pelaat?: ")
        
        champ = champ.strip().replace(" ", "")

        if champ == "exit":
            break

        rank = input("Mikä rank?: ")

        for i in kielletty_merkki:
            champ = champ.replace(i, "")
            rank = rank.replace(i, "_")

        if rank == "exit":
             break

        patch = input("Mikä patch?: ")

        if patch == "exit":
             break

        open_analytics(champ, rank, patch)



import ast

inhalt = ""
dic = {}

with open("daten/daten_freiburg.txt", "r") as file:
    for zeile in file:
        zeile = zeile.strip()
        if zeile:
            try:
                key, var = zeile.split(":", 1)
                key = key.strip()
                var = ast.literal_eval(var.strip())

                dic[int(key)] = var
            except ValueError as e:
                print(f"Fehler beim Verarbeiten der Zeile: {zeile} -> {e}")
print(dic)

test = {
    1:["2:03:17","2000","m","ETH"],
    2:["3:03:17","2001","w","ETH"],
    3:["7:03:17", "2000","w", "ETH"]
}
print(test)
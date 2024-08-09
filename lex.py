cod_fonte = "position = initial + rate * 60"
cod_fonte2 = cod_fonte.replace(" ", "")
lexema = ""
id_count = 1
for i in range(0, len(cod_fonte2)):
    if cod_fonte2[i].isalpha():
        lexema += cod_fonte2[i]
        if cod_fonte2[i+1] in ("=","+","*"):
            print(f"<ID, {id_count}>")
            lexema = ""
            print("<OP, "+cod_fonte2[i+1]+">")
            id_count += 1
    if cod_fonte2[i].isdigit():
        lexema += cod_fonte2[i]
print("<NUM, "+lexema+">") 
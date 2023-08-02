def calcLoc():
    global comida, indumentaria, perfumería
    
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene menos locales que los demás.")
    elif comida < indumentaria and comida < perfumería:
        print(f"El rubro con menos locales es 'comida', con {comida} locales")
    elif indumentaria < comida and indumentaria < perfumería:
        print(f"El rubro con menos locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería < comida and perfumería < indumentaria:
        print(f"El rubro con menos locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print(f"Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales, con {comida} locales.")
    elif indumentaria == perfumería :
        print(f"Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales, con {indumentaria} locales.")
    elif comida == perfumería:
        print(f"Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales, con {perfumería} locales.")
    
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene más locales que los demás.")
    elif comida > indumentaria and comida > perfumería:
        print(f"El rubro con más locales es 'comida', con {comida} locales")
    elif indumentaria > comida and indumentaria > perfumería:
        print(f"El rubro con más locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería > indumentaria and perfumería > comida:
        print(f"El rubro con más locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print(f"Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales, con {comida} locales.")
    elif indumentaria == perfumería :
        print(f"Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales, con {indumentaria} locales.")
    elif comida == perfumería:
        print(f"Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales, con {perfumería} locales.")

pessoa = [
    {"nome":"André",
     "idade":42,
     "endereço":{"rua":"Rua do zé",
                 "cep":88070220,
                 "cidade":"Florianopolis"}
     },
    {"nome":"Maria",
     "idade":35,
     "endereço":{"rua":"Rua do joão",
                 "cep":88070221,
                 "cidade":"São José"}}]



print(pessoa[0]["endereço"]["cidade"])
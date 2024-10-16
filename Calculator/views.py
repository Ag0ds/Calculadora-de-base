from django.shortcuts import render, HttpResponse

def home(request):
    if request.method=="POST":
        numero = float(request.POST.get("numero",0))
        base = float(request.POST.get("base",0))
        base_desejada = float(request.POST.get("base_desejada",0))

        Resultado = calcula_base(numero, base, base_desejada)
        return render(request, "home.html",{"Resultado":Resultado})
    
    return render(request, "home.html")

def calcular(request):
    if request.method=="POST":
        numero = int(request.POST.get("numero",0))
        base = int(request.POST.get("base",0))
        base_desejada = int(request.POST.get("base_desejada",0))

        Resultado = calcula_base(numero, base, base_desejada)
        return render(request, "home.html",{"Resultado":Resultado} )
    return HttpResponse("Requisição invalida")


#calculadora de base

def calcula_base(numero, base, base_desejada):
    numero = str(numero)
    Q = int(len(numero))
    Resultado = 0
    Q = Q-1
    T = 0
   
    while Q >= 0:
        parcial = soma_de_base(int(numero[T]),mutiplicacao_base(Resultado,base,base_desejada),base_desejada)
        Resultado = parcial
        T += 1
        Q -= 1
    return Resultado
    
def mutiplicacao_base(valor_1, valor_2, base):
    loop_1 = len(str(valor_1))
    loop_2 = len(str(valor_2))
    valor_1 = (str(valor_1)[::-1])
    valor_2 = (str(valor_2)[::-1])
    R = 0
    T = 0
    Resultado_mut = ""
    while loop_1 > 0:
        primeiro_resultado = int(valor_1[R]) * int(valor_2[T])
        if primeiro_resultado > int(valor_2):
            resto = primeiro_resultado % base
            quociente = primeiro_resultado // base 
            primeiro_resultado = str(resto) + str(quociente)
        Resultado_mut = Resultado_mut + str(primeiro_resultado)
        R += 1
        loop_1 -= 1
    Resultado_mut = int((Resultado_mut)[::-1])
    return Resultado_mut


def soma_de_base(valor_1, valor_2, base):
    if valor_2 > valor_1:
        valor_1 , valor_2 = valor_2, valor_1
    loop_1 = len(str(valor_1))
    loop_2 = len(str(valor_2))
    valor_1 = (str(valor_1)[::-1])
    valor_2 = (str(valor_2)[::-1])
    R = 0
    Resultado_mut = 0
    while loop_1 > 0:
        if loop_2 < 1:
            primeiro_resultado = int(valor_1[R]) + 0
        elif loop_1 < 1:
            primeiro_resultado = 0 + int(valor_2[R])
        else:
            primeiro_resultado = int(valor_1[R]) + int(valor_2[R])
        if primeiro_resultado >= base:
            resto = primeiro_resultado % base
            quociente = primeiro_resultado // base 
            primeiro_resultado = str(quociente) + str(resto)
        Resultado_mut = Resultado_mut + int(primeiro_resultado)*(10**R)
        R += 1
        loop_1 -= 1
        loop_2 -= 1
    Resultado_mut = int(Resultado_mut)
    return Resultado_mut
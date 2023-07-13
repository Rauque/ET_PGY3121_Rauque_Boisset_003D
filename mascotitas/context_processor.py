
def total_carrito(request):
    total = 0
    if request.user in request.session: 
        try:
            for key,value in request.session['carrito'].items():
                total = total + (int(value['precio']))*(value['cantidad'])
        except KeyError:
            request.session['carrito']={}
            total = 0 
    return {'total_carrito':int(total)}



def total_carrito_imp(request):
    total_imp = 0
    if request.user in request.session: 
        try:
            for key,value in request.session['carrito'].items():
                total_imp = total_imp + (int(value['precio']))*(value['cantidad'])
        except KeyError:
            request.session['carrito']={}
            total_imp = 0 
    return {'total_carrito_imp':int(total_imp*0.19)}




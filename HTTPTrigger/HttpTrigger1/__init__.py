import logging

import azure.functions as func


from math import sin


def cal_integral_calc(x=None,y=None):
    N = [10,100,1000,10000,100000,1000000,10000000]
    out=[]
    for j in range(len(N)):
        i = 0
        di = 0.0
        while i<N[j]:
            parts = ((y-x)/N[j])*i 
            length = abs((y-x)/N[j])
            breadth = abs(sin(parts))
            di += length*breadth
            i+=1
        out.append(di)
    return str(out)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        lower = req.route_params.get('lower')
        upper = req.route_params.get('upper')
    except:
         return func.HttpResponse(
             "This HTTP request is not properly formed with all required inputs",
             status_code=200
    )   

    result = cal_integral_calc(float(lower), float(upper))
    return func.HttpResponse(
             f'Response: {result}',
             status_code=200
    )

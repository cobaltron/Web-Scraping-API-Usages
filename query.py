import wikipedia
import wolframalpha

while True:
    inp=input("Q: ")
    try:
        app_id="R9VTKV-XRVJ4WVPUE"
        client=wolframalpha.Client(app_id)
        res=client.query(inp)
        answer=next(res.results).text
        print (answer)
    except:
        inp=inp.split(' ')
        #input=" ".join(input[2:])
        print (wikipedia.summary(inp))
        

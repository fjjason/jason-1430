import bottle
from bottle import route, run, static_file
from flask import jsonify,request
import spacy 
import re, json
from bottle import request, response
from bottle import post, get, put, delete

nlp = spacy.load('en_core_web_sm') 

app = bottle.default_app()



@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'

@route('/code/<filename>')
def server_static(filename):
	return static_file(filename,root="/code")
#{"sentence":"Hello World! Jason"}


from bottle import get, post, request # or route

@get('/ner') 
def ner():
    return '''
        <form action="/ner" method="post">
            inputSentence: <input name="input" type="text" />
            <input value="get NER" type="submit" />
        </form>
    '''

@post('/ner') 
def do_ner():
	sentence = request.forms.get('input')
	print(sentence)
	#sentence = posted_data['sentence']	
	doc = nlp(sentence) 
	res = ""
	for ent in doc.ents: 
		res += "\n"	
		res += ent.text + " : " + ent.label_
	if res == "":
		return json.dumps({'res': "No NER detected, try adding names/location/etc"})

	return json.dumps({'res': res})





if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, debug=True, reloader=True)

from flask import *
import json,requests
from telegraph import Telegraph
app = Flask(__name__)
@app.route('/')
def api():
    title = request.args.get('title')
    content = request.args.get('content')  
    telegraph = Telegraph()     
    telegraph.create_account(short_name='1337')

    response = telegraph.create_page(
   f'{title}',
        html_content=f'<p>{content}</p>'
    )
    x = (response['url'])     
    data = {"url":f"{x}","result":f"True"}
    json_string = json.dumps(data, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response
        
app.run()        

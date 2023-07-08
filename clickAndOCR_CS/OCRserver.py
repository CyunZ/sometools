import flask
import cnocr

ocr = cnocr.CnOcr(det_model_name='naive_det')

app = flask.Flask(__name__)

@app.route('/') 
def home():
    return "Hello World"
    
@app.route('/photo',methods=['POST'])
def photo():
    #接收图片  
    name = flask.request.form['name']
    print(name)
    file = flask.request.files['file']
    file.save('test.jpg')
    result = ocr.ocr('test.jpg')
    print(result)
    texts = ''
    for line in result:
        texts += line['text']
    return texts

    

app.run(host='0.0.0.0',port=5000, debug=True)
import patoolib
from flask import Flask
from flask import send_file,request,render_template
import os
import pathlib
import patoolib
app = Flask(__name__)
pathl = pathlib.Path()    
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        files = request.files['pdf']
        # return files
        with open(pathl / "temp"/"ee",'wb') as out:
            # file.write(out)
            out.write(files)
            print("jinxing")
            # out.close()
            
        return "点击了文件上传"
    return render_template("yy.html")
    return 'Hello, World!'

app.run(debug=True)
print("调用了这个python文件")
from flask import Flask, render_template,request
import pickle 
import numpy as np

app = Flask(__name__)

def prediction(list):
    with open('laptop_price_predictor.pickle','rb') as file:
        model = pickle.load(file)
        return model.predict([list])

@app.route('/', methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')
        
        x = []
        x.append(int(ram))
        x.append(float(weight))
        x.append(len(touchscreen))
        x.append(len(ips))
        
        
        
        company_list = ['acer', 'apple',
       'asus', 'dell', 'hp', 'lenovo',
       'msi', 'other', 'toshiba']
        
        typename_list = ['2in1Convertible', 'gaming', 'netbook',
       'notebook', 'ultrabook', 'workstation']
        
        opsys_list = ['linux', 'mac', 'other', 'windows']
        
        cpu_list = ['amd', 'intelcorei3', 'intelcorei5',
       'other']
        
        gpu_list = ['amd', 'intel', 'nvidia']
        
        # for item in company_list:
        #     if item == company:
        #         x.append(1)
        #     else:
        #         x.append(0)
                
        # for item in typename_list:
        #     if item == typename:
        #         x.append(1)
        #     else:
        #         x.append(0)

        # for item in opsys_list:
        #     if item == opsys:
        #         x.append(1)
        #     else:
        #         x.append(0)
                
        # for item in cpu_list:
        #     if item == cpu:
        #         x.append(1)
        #     else:
        #         x.append(0)
                
        # for item in gpu_list:
        #     if item == gpu:
        #         x.append(1)
        #     else:
        #         x.append(0)
        
        def x_add(list,value):
            for item in list:
                if item == value:
                    x.append(1)
                else:
                    x.append(0)
        
        x_add(company_list,company)
        x_add(typename_list,typename)
        x_add(opsys_list,opsys)
        x_add(cpu_list,cpu)
        x_add(gpu_list,gpu)
        
        pred = prediction(x)*329
        pred = np.round(pred[0])
        
    return render_template("index.html",pred= pred)

if __name__ == "__main__":
    app.run(debug=True)
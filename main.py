from flask import Flask, render_template, request, make_response

import draw_graph

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/show/', methods = ['POST'])
def show():
    result = request.form
    formura1 = result['formura_1'].strip()
    formura2 = result['formura_2'].strip()
    formura3 = result['formura_3'].strip()
    formura4 = result['formura_4'].strip()
    formura5 = result['formura_5'].strip()
    formura = [formura1, formura2, formura3, formura4, formura5]
    formura = [x for x in formura if x]
    # send_type = 'POST通信'
    graphValue = draw_graph.plot_graph(
        formura)
    
    response = make_response(graphValue)
    response.headers['Content-Type'] = 'image/png'

    return response

if __name__ == '__main__':
    app.run(debug = True, port = 8888)
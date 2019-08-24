from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)
SECRET_KEY = '123'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    # month = request.form.get('month')
    # file = request.files.get('data')

    file = request.files['file']
    month = request.form['month']
    print(month)

    files = {'data': (file.filename, file.stream, file.mimetype)}
    r = requests.post(
        "http://95.213.252.26/api/save-data/",
        files=files,
        data={'month': month, 'secret': SECRET_KEY}
    )
    # print(r.status_code, r.reason)
    if r.status_code == requests.codes.ok:
        resp = r.json()
        print(resp)

    return render_template('index.html')

    # if month in ['aug', 'sep']:
    #     print('OK!')
        # req = requests.request(
        #     method='POST',
        #     # url='http://127.0.0.1:5001/api/save-image/',
        #     url='http://95.213.252.26/api/save-data/',
        #     files=dict(
        #         data=(
        #             file.filename,
        #             file.stream,
        #             file.mimetype
        #         )
        #     ),
        #     data=dict(
        #         month=month,
        #         secret=SECRET_KEY
        #     )
        # )

        # files = {'data': (file.filename, file.stream, file.mimetype)}
        # data = {'month': month, 'secret': SECRET_KEY}
        # req = requests.post(url='http://95.213.252.26/api/save-data/',
        #                     # files=files,
        #                     data=data)


        # with open('sample_plan.xml', 'rb') as payload:
        #     headers = {'auth-token': 'abCdeFgh'}
        #     files = {'data': ('sample_plan.xml', payload, 'text/xml')}
        #     req = requests.post(url='http://abc123.com/index.php/plan/', \
        #                         headers=headers, files=files)

        # if req.status_code == requests.codes.ok:
        #     resp = req.json()
        #     print(resp)
        #
        # print('OK!OK!OK!')

#         https://dev-gang.ru/article/python-flask-otpravlyaem-fayly-i-dannye-formy-iz-odnogo-servisa-v-drugoy/
# https://codex.so/python-flask


if __name__ == '__main__':
    app.run(port=5000)

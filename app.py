__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    return "<h1>OpenShift Ninja - MODIFIED BY Oswald ON January 10th 2016</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

from bottle import route, run

@route('/')
def index():
    return "<h1>OI RAFAEL</h1>"

if __name__ == '__main__':
    run()

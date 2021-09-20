# import dependencies
from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
@app.route('/Dashboard')
def Dashboard():
    return render_template('base.html')

# Error route
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    #run this when running on LOCAL server...
    app.run(debug=True)

    #...OR run this when running on PRODUCTION server...
    # app.run(debug=False)








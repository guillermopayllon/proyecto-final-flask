#Archivo Principal del proyecto

#Importamos FLASK para trabajar con el
from flask import Flask, render_template

#####################################################################################
#Variable que representa nuestra aplicación

app = Flask(__name__)



#Página Principal
@app.route("/")
def inicio():
    return render_template('index.html')


#Página Portfolio
@app.route("/portfolio")
def portfolio():
    return render_template('/portfolio.html')


#Página Acerca de
@app.route('/about')
def about():
    return render_template('about.html')

#Página contacto
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Página blog
@app.route('/blog')
def blog():
    return render_template("blog.html")




    
    

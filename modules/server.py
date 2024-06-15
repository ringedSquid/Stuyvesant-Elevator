from bottle import route, run, request, get, post, template, response, redirect, static_file
import bottle

bottle.TEMPLATE_PATH.insert(0, '../views/')

@route('/display')
def index():
    return template('display')

@route('/static/<filename>')
def styelsheet_static(filename):
    return static_file(filename, root="static/")
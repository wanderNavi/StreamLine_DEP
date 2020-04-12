from flask import render_template

def main():
    ret = render_template('landing.html')
    return (ret)
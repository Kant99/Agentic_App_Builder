def coder(design: dict):
    design["index.html"]="""This is the HTML file"""
    design["style.css"]="""This is the CSS file"""
    design["index.js"] = """
function add(a, b) { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function divide(a, b) { return a / b; }
"""
    return design

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/',)
def page_index():

    page_content = """ 
    <style>
    h2 {color: green;}
    </style>
    <p> Hello </p>
    <h2> OPS </h2>
    <h1 style=" color: red">Hi</h1>

    <form action="http://httpbin.org/get">
        <input type="password" name="pass" value="12345">
        <input type="submit" value="Отправить Дарине">
        <input type="checkbox" name="subscribe">
        <input type="checkbox" name="subscribe">
        </br>
        <textarea name="aboutme" >
        Исходный текст тут
        </textarea>
    </form>
    """
    return page_content


app.run('0.0.0.0', 5000)
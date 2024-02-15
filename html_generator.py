def make_body(title, body):
    return f"""

    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}  </title>
    </head>

    <body>
    {body}
    </body>

    </html> 
    """
def form():
    return"""
<html>
    <body>
    <form action = "http://localhost:5000/user" method = "post"> 
    <label for="fname">Nimi:</label>
    <input type="text"  name="username"><br><br>
    <input type="Submit" value="nappi">
    </form> 
    </body> 
</html> 
    """
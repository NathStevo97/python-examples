import webbrowser
import os
print ()
f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

filename = 'file:///'+os.getcwd() +'/' + 'helloworld.html'
webbrowser.open_new_tab(filename)

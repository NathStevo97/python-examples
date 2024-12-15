import SimpleHTTPServer  # servers files from the current directory and below

# directly maps the directory structure to HTTP requests
import SocketServer  # a module that simplifies the task of writing network servers
import os  # module for usiing operating system functionality

os.chdir(os.getcwd() + "/public")  # changes directory to file required
PORT = 8000  # define port number for html mapping to be displayed on

Handler = (
    SimpleHTTPServer.SimpleHTTPRequestHandler
)  # defines how web server handles incoming requests
# SimpleHTTPRequestHandler serves files from current directory + subdirectories, in this case just index.html

httpd = SocketServer.TCPServer(("", PORT), Handler)
# defines the server as one that uses the TCP protocol to send and receive messages

print("Serving at port", PORT)
httpd.serve_forever()  # method on TCP server that starts the server and begins listening and responding to incoming requests

import os
import json
import webbrowser
import xmlrpclib, sys

def render_video(path):
    r = r'<center><video src="' + path + r'" controls width="960" height="720"></center>'
    return r

def main(args):
    if len(args) == 0:
        args.append('lbry://wonderfullife')

    daemon = xmlrpclib.ServerProxy('http://localhost:7080/')

    if len(args) > 1:
        print 'Too many args', args

    else:
        if args[0][7:] != 'settings':
            r = daemon.get(args[0][7:])
            print r
            path = r['path']
            if path[0] != '/':
                path = '/' + path

            print path
            filename = path.split('/')[len(path.split('/')) - 1]
            extension = path.split('.')[len(path.split('.')) - 1]

            if extension in ['mp4', 'flv', 'mov']:
                h = str(render_video(path))
                f = open('lbry.html', 'w')
                f.write(h)
                f.close()
                webbrowser.open('file://' + os.path.join(os.getcwd(), 'lbry.html'))

            else:
                webbrowser.open('file://' + path)
        else:
            r = daemon.get_settings()
            f = open('lbry.html', 'w')
            f.write("<body>" + json.dumps(r) + "</body>")
            f.close()
            webbrowser.open('file://' + os.path.join(os.getcwd(), 'lbry.html'))

if __name__ == "__main__":
   main(sys.argv[1:])
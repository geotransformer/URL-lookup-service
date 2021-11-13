import logging
from flask import Flask, jsonify, request

app = Flask(__name__)
malwareDB = {}

log = logging.getLogger('URLLookupService')

class URLLookupService(object):
    def __init__(self):
        log.setLevel(logging.DEBUG)
        stdoutHandler = logging.StreamHandler()
        stdoutHandler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")
        stdoutHandler.setFormatter(formatter)
        log.addHandler(stdoutHandler)

    @app.route("/")
    @app.route('/healthy', methods=['GET'])
    def health():
        return jsonify({"healthy": "UP"})

    @app.route('/urlinfo/1/<path:subpath>', methods=['GET'])
    def checkURL(subpath):
        query_string = str(request.query_string.decode("utf-8"))
        url = subpath
        if query_string:
            url = subpath + "?" + query_string
        safe = True
        if url in  malwareDB:
            safe = False 
        return jsonify({"safe": safe, "url": url})

    def loadMalwareDB(self, local_malware_DB):
        with open(local_malware_DB) as f:
            for line in f:
                url = str(line).strip()
                malwareDB[url] = url
        log.info(str(malwareDB))

    def start(self):
        app.run(host='0.0.0.0', port=8888, debug=True, use_reloader=False)


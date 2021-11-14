import logging
from log import init_logging
from flask import Flask, jsonify, request

app = Flask(__name__)
malwareDB = {}
log = logging.getLogger('URLLookupService')

class URLLookupService(object):
    def __init__(self):
        init_logging(log)

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

    # Load malware urls from local file
    def loadMalwareDB(self, local_malware_DB):
        log.info("Initialize malware url DB from local file")
        try:
            with open(local_malware_DB) as f:
                for line in f:
                    url = str(line).strip()
                    malwareDB[url] = url
            log.info(str(malwareDB))
        except Exception as ex:
            log.error("Error to load malware file: {0}".format(local_malware_DB))
            raise ex


    def start(self):
        app.run(host='0.0.0.0', port=8888, debug=True, use_reloader=False)


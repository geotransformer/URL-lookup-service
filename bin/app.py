
import logging
from URLLookupService import URLLookupService

log = logging.getLogger('app')
log.setLevel(logging.DEBUG)
stdoutHandler = logging.StreamHandler()
stdoutHandler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")
stdoutHandler.setFormatter(formatter)
log.addHandler(stdoutHandler)

if __name__ == '__main__':
    log.info("Starting URLLookupService")
    app = URLLookupService()
    app.loadMalwareDB("/opt/run/url-lookup-service/config/malware_url.txt")
    app.start()



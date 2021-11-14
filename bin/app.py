
import logging
from log import init_logging
from URLLookupService import URLLookupService

log = logging.getLogger('app')

if __name__ == '__main__':
    init_logging(log)
    log.info("Starting URLLookupService")
    app = URLLookupService()
    app.loadMalwareDB("/opt/run/url-lookup-service/config/malware_url.txt")
    app.start()



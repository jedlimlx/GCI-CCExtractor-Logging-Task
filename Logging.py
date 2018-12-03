import coloredlogs, logging
import coloredlogs.converter

logger = logging.getLogger()
logging.basicConfig(filename='demo.log')

coloredlogs.install(level='DEBUG', logger=logger,
                    fmt='%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s',
                    level_styles={'info': {'color' : 'yellow', 'bold' : True},
                                  'warning': {'color': 'red'}})

# Yellow Logger Info
logger.info("INFORMATION")

# Output to a File
logger.warn("WARNING!!")

from flask_restx import Api

import config


scraperfy_api = Api(prefix=config.API_PREFIX, version='0.1.0', title='Scraperfy API',
        description='A RESTful API that serves data from the Scraperfy Package'
    )


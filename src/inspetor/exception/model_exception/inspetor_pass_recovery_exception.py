from src.inspetor.exception.exception_abstract import ExceptionAbstract

import logging


class InspetorPassRecoveryException(ExceptionAbstract):
    status_code = 700
    severity    = logging.CRITICAL

    REQUIRED_PASS_RECOVERY_EMAIL = {
        'message': 'recovery_email is a required property. It cannot be null.',
        'code'   : 7001,
    }

    REQUIRED_PASS_RECOVERY_TIMESTAMP = {
        'message': 'timestamp is a required property. It cannot be null on creation.',
        'code'   : 7002,
    }

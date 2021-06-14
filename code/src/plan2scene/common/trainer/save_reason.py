import enum

class SaveReason(enum.Enum):
    '''
    Specify the reason to save a checkpoint
    '''
    REST_MDOEL = 'base_model'
    INTERVAL = 'interval'


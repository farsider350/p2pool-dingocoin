from p2pool.bitcoin import networks

PARENT = networks.nets['dingocoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 2*24*60 # shares
REAL_CHAIN_LENGTH = 2*24*60 # shares
TARGET_LOOKBEHIND = 60 # shares
SPREAD = 8 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 2010
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 2011
BOOTSTRAP_ADDRS = '139.180.181.92'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-dingocoin'
VERSION_CHECK = lambda v: None if 150300 <= v else 'Dingocoin version too old. Upgrade to 0.15.3.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set([])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000

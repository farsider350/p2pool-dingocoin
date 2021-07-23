import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c1c1c1c1'.decode('hex')
P2P_PORT = 33117
ADDRESS_VERSION = 30
RPC_PORT = 34646
RPC_CHECK =RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'dingocoin' in (yield bitcoind.rpc_help()) and
#            (yield helper.check_block_header(bitcoind, '1a91e3dace36e2be3bf030a65679fe821aa1d6ef92e7c9902eb318182c355691')) and
                          (yield bitcoind.rpc_getinfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 88*100000000 >> (height + 1)//100000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'DINGO'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dingocoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dingocoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dingocoin'), 'dingocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://openchains.info/coin/dingocoin/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://openchains.info/coin/dingocoin/address/'
TX_EXPLORER_URL_PREFIX = 'https://openchains.info/coin/dingocoin/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

from multiprocessing import Process
from services.blocks_service import BlocksService

#main
def SpawnSingletonBlockService():
    BlocksService()

if __name__ == '__main__':
    p = Process(target=SpawnSingletonBlockService, args=())
    p.start()
    p.join()
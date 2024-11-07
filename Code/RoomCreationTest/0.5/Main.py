from Script import *
from threading import Thread

if __name__ == "__main__":

    while True:
        thread_frame = Thread(target=frame())
        thread_frame.start()
        thread_main = Thread(target=main())
        thread_main.start()
        thread_main.join()
        thread_frame.join()
        pygame.display.update()
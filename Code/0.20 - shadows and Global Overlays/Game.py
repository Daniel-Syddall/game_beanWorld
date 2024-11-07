from data.App import App
from threading import Thread
from pygame.display import update

def main():
    app = App()
    while True:
        thread_frame = Thread(target=app.frameDelay())
        thread_run = Thread(target=app.run())
        thread_frame.start()
        thread_run.start()
        thread_run.join()
        thread_frame.join()
        update()

if __name__ == "__main__":
    main()
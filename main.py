import time
from pathlib import Path
from organizer import FileOrganizer
from rich import print
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class DesktopHandler(FileSystemEventHandler):

    def __init__(self, organizer: FileOrganizer):
        self.organizer = organizer

    def on_created(self, event):
        if event.is_directory:
            return

        time.sleep(0.5)
        self.organizer.organize_file(Path(event.src_path))

if __name__ == "__main__":
    organizer = FileOrganizer()
    event_handler = DesktopHandler(organizer)
    observer = Observer()

    watch_dir = organizer.base_path
    observer.schedule(event_handler, path=str(watch_dir), recursive=False)

    print(
        f"[bold green][+] MacDeskClean is running... [/bold green] Watching"
        f"{watch_dir}"
    )
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[bold red][!] Stopping MacDeskClean.[/bold red]")
    observer.join()
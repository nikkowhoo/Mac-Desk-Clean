import subprocess

class MacNotifier:
    
    @staticmethod
    
    def send(title: str, message: str, subtitle: str = "MacDeskClean"):
        #"Uses the notification center subprocess to create  notification"
        escaped_title = title.replace('"','\\"')
        escaped_msg = message.replace('"','\\"')
        escaped_sub = subtitle.replace('"','\\"')

        script = (
            f'display notification "{escaped_msg}" with title'
            f' "{escaped_title}" subtitle "{escaped_sub}"'
        )
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            print(f"[Notified] {title}: {message}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to send notification: {e}")
    
        


from rich.console import Console

class LogPanel:
    def __init__(self):
        self.console = Console()

    def log_info(self, message):
        self.console.log(message, style="blue")

    def log_warning(self, message):
        self.console.log(message, style="yellow")

    def log_error(self, message):
        self.console.log(message, style="bold red")

    def log_success(self, message):
        self.console.log(message, style="green")

    def log_debug(self, message):
        self.console.log(message, style="magenta")

    def log_custom(self, message, style):
        self.console.log(message, style=style)


#AI-Genned, work smarter not harder kids
#You should still be able to recognize what it does,
#line for line, though;
#Progress is progress!

import sys

class TeeStdout:
    """Duplicates or redirects stdout to a file when enabled."""
    def __init__(self, filename="console_output.log"):
        self.terminal = sys.stdout
        self.log_file_path = filename
        self.file = None
        self.enabled = False

    def toggle(self, enable=None, filename=None):
        """Enables or disables stdout redirection to file."""
        if filename:
            self.log_file_path = filename

        # Determine new state if not explicitly passed
        self.enabled = not self.enabled if enable is None else enable

        if self.enabled:
            if not self.file or self.file.closed:
                self.file = open(self.log_file_path, "w", encoding="utf-8")
            sys.stdout = self
        else:
        # Restore normal terminal output
            sys.stdout = self.terminal
            if self.file and not self.file.closed:
                self.file.close()

    def write(self, message):
        # Always write to the real terminal
        self.terminal.write(message)
        # Also write to file if enabled
        if self.enabled and self.file and not self.file.closed:
            self.file.write(message)
            self.file.flush()  # Ensure it writes immediately

    def flush(self):
        self.terminal.flush()
        if self.file and not self.file.closed:
            self.file.flush()
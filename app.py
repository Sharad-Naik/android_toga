import toga
import datetime
from toga.style import Pack
from .sub import add_numbers
from toga.style.pack import COLUMN, ROW


class bumblebee(toga.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_text = toga.TextInput(readonly=True, initial='')
        self.result_text = toga.TextInput(readonly=True, initial='')
        self.time_label = toga.Label(datetime.datetime.now().strftime('%H:%M:%S'))

    def update_label_text(self):
        # Update the label text with the current time
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.time_label.text = f'Current Time: {current_time}'
        #threading.Event().wait(1)

    def run_python_script(self, widget):
        # Call the function from myscript and capture its output
        result = add_numbers(5, 8)

        # Set the output as the text in the text field
        self.result_text.value = result

    def say_hi(self, widget):
        # Update the text in the text field to show number 23
        self.update_label_text()
        self.number_text.value = self.time_label.text

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Add the number text field to the main_box
        main_box.add(self.number_text)
        main_box.add(self.result_text)
        main_box.add(self.time_label)
        
        button_run_script = toga.Button('Run Script', on_press=self.run_python_script)
        main_box.add(button_run_script)

        # Add a button to the main_box
        button = toga.Button('Time', on_press=self.say_hi)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        # Start a separate thread to update the label text continuously
        #thread = threading.Thread(target=self.update_label_text)
        #thread.daemon = True  # Make the thread a daemon, so it terminates with the main process
        #thread.start()

        self.main_window.show()



def main():
    return bumblebee()

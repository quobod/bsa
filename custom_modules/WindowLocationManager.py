from .CoordinatesManager import save_location, get_location
from .StatusMessenger import STATUS_MESSENGER


def window_location_handler(window):

    def save_and_exit():
        message = STATUS_MESSENGER['warning']('Closing the main window')
        print("\n\t\t{}\n".format(message))
        coordinates = {
            'x': window.winfo_rootx(),
            'y': window.winfo_rooty()
        }
        save_location(coordinates)
        window.destroy()

    def on_open(content):
        message = STATUS_MESSENGER['success']('Opening the main window')
        print("\n\t\t{}\n".format(message))
        win_coordinates = get_location()
        x = None
        y = None
        if win_coordinates:
            x = win_coordinates['x']
            y = win_coordinates['y']
            content.geometry("+{}+{}".format(x, y))

    def exit(): save_and_exit()

    window.protocol("WM_DELETE_WINDOW", save_and_exit)
    on_open(window)


def save_and_exit_window(window):
    message = STATUS_MESSENGER['warning']('Closing the main window')
    print("\n\t\t{}\n".format(message))
    coordinates = {
        'x': window.winfo_rootx(),
        'y': window.winfo_rooty()
    }
    save_location(coordinates)
    window.destroy()

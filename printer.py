import win32api
import win32print

def printShoppingList(df):
    text = "\n".join([n.capitalize() for n in df["name"]])
    print(text)

    # Get the default printer
    printer_name = win32print.GetDefaultPrinter()

    with open("print.txt", "w", encoding="utf-8") as f:
        f.write(text)

    win32api.ShellExecute(
        0,
        "print",
        "print.txt",
        None,
        ".",
        0
    )


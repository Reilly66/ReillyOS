import ui

ADMIN_PASSWORD = "@dm1n"

def start_bios():
    bios_io = ui.IO("BIOS")
    bios_io.output("##########")
    bios_io.output("###BIOS###")
    bios_io.output("##########")
    get_bios_command(bios_io)

def get_bios_command(bios_io):
    command = bios_io.input()
    if " " in command:
        command = command.split(" ")
    else:
        command = [command]

    match command[0].lower():
        case "boot":
            boot(bios_io, command)
        case _:
            bios_io.output("Command not recognised", color="red")

def boot(bios_io, command):
    def boot_command():
        # get the parameters of the command
        command.pop(0)
        admin = "-a" in command
        return admin
    admin = boot_command()
    if admin:
        user_input_password = bios_io.input("Enter admin password: ")
        if user_input_password != ADMIN_PASSWORD:
            bios_io.output("Incorrect admin password", color="red")
    
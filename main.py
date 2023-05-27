import core
from Transversal.primary import end_program

# Main Loop
while True:
    try:
        core.main_menu()
    except KeyboardInterrupt:
        end_program()

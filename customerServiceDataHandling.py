import datetime
#Task 1
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
 
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
 
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def printCritical(text):
    print(colors.bg.black, colors.fg.red)
    print(text, colors.reset)

def printWarning(text):
    print(colors.bg.black, colors.fg.orange)
    print(text, colors.reset)

def printSuccess(text):
    print(colors.bg.black, colors.fg.green)
    print(text, colors.reset)

def printWorking(text):
    print(colors.bg.black, colors.fg.blue)
    print(text, colors.reset)

def askMenu(choices, text):
    counter = 1
    choice_list = []
    for choice in choices:
        new_choice = str(counter) + ". " + str(choice)
        choice_list.append(new_choice) 
        counter += 1
    separator = "\n"
    menu = separator.join(choice_list)
    printWorking(menu)
    printWarning(text)
    user_input = input("Selection: ")
    try:
        index = int(user_input)
        index <= len(choices) == True
        index >= 0 == True
    except ValueError:
        printCritical("Function error! Please make sure choose one of the chosen options!")
    except TypeError:
        printCritical("Function error! Please make sure to input numbers for menu selections!")
    else:
        return index-1

def openTicket(tickets, customer, issue, priority):
    ticket_id = customer + str(datetime.datetime.now())
    open_tickets = tickets.get("open")
    new_ticket = {"ID": ticket_id, "customer": customer, "priority": priority, "issue": issue}
    open_tickets.setdefault(ticket_id, new_ticket)

def selectTicket(ticket_dictionary, status):
    ticket_keys = list(ticket_dictionary.keys())
    if len(ticket_keys) >= 1:
        index = askMenu(ticket_keys, "Please choose a ticket: ")
        ticket_id = str(ticket_keys[index])
        return ticket_id
    else:
        print(f"There are no {status} tickets.")

def deleteTicket(tickets, status):
    ticket_category = tickets.get(status)
    ticket = selectTicket(ticket_category, status)
    if ticket != None:
        ticket_category.pop(str(ticket), "not found")
    else:
        print("Could not find ticket to delete.")
    
def updateTicket(tickets, status):
    ticket_category = tickets.get(status)
    ticket = selectTicket(ticket_category, status)
    if len(ticket) >= 1:
        ticket_found = ticket_category.get(str(ticket))
        if len(ticket_found) >= 1:
            input_option = askMenu(["Customer", "Priority", "Issue"], "Please choose what to update: ")
            choice = ""
            option = int(input_option)
            if type(option) == int:
                new_info = ""
                if option == 0:
                    new_info = str(input("Customer name: "))
                    choice = "customer"
                if option == 1:
                    new_priority = askMenu(["High", "Medium", "Low"], "Please select a new priority for this ticket:")
                    if new_priority == 0:
                        new_info = "High"
                    if new_priority == 1:
                        new_info = "Medium"
                    if new_priority == 2:
                        new_info = "Low"
                    choice = "priority"
                if option == 2:
                    new_info = str(input("Issue: "))
                    choice = "issue"
            ticket_found.update({choice: new_info})
    else:
        print("Ticket unable to be loaded!")

def viewTickets(tickets, status):
    tickets_to_show = []
    if status in ["open", "closed"]:
        found_tickets = tickets.get(status).values()
        print(status, "tickets: ")
        if len(found_tickets) >= 1:
            counter = 1
            for ticket in found_tickets:
                ticket_info = "- " + str(counter) + " " + str(ticket.get("customer")) + " " + str(ticket.get("priority"))  + " " + str(ticket.get("issue"))
                tickets_to_show.append(ticket_info)
                print(ticket_info)
                counter += 1
            return found_tickets
        else:
            print("None")
            return None

def mainLoop():
    tickets = {
        "open": {},
        "closed": {}
    }
    openTicket(tickets, "Bob", "computer no work", "High")
    openTicket(tickets, "Jim", "phone exploded", "Low")
    openTicket(tickets, "Billy", "out of coffee", "High")
    openTicket(tickets, "Garnt", "hangover", "Medium")
    while True:
        input_option = askMenu(["Create Ticket", "View Tickets", "Update Ticket", "Delete Ticket"], "Please choose an operation: ")
        try:
            option = int(input_option)
            if option == 0:
                # create ticket
                customer_name = str(input("Customer name: "))
                issue = str(input("Issue: "))
                input_priority = askMenu(["High", "Medium", "Low"], "Please select a priority for this ticket:")
                if input_priority == 0:
                    input_priority = "High"
                if input_priority == 1:
                    input_priority = "Medium"
                if input_priority == 2:
                    input_priority = "Low"
                openTicket(tickets, customer_name, issue, input_priority)
                viewTickets(tickets, "open")
            if option == 1:
                # view tickets
                input_status = askMenu(["open", "closed"], "Please select category to view: ")
                if input_status == 0:
                    input_status = "open"
                if input_status == 1:
                    input_status = "closed"
                viewTickets(tickets, input_status)
            if option == 2:
                # update ticket
                input_status = askMenu(["open", "closed"], "Please select category to search through: ")
                if input_status == 0:
                    input_status = "open"
                if input_status == 1:
                    input_status = "closed"
                updateTicket(tickets, input_status)
                viewTickets(tickets, input_status)
            if option == 3:
                # delete ticket
                input_status = askMenu(["open", "closed"], "Please select category to search through: ")
                if input_status == 0:
                    input_status = "open"
                if input_status == 1:
                    input_status = "closed"
                deleteTicket(tickets, input_status)
                viewTickets(tickets, input_status)
        except ValueError:
            printCritical("Program error! Please make sure choose one of the chosen options!")
        except TypeError:
            printCritical("Program error! Please make sure to input numbers for menu selections!")
        except:
            printCritical("Program error! An unknown error has occured. Double check any inputs and try again!")
        finally:
            printSuccess("done!\n------------------------------")

mainLoop()
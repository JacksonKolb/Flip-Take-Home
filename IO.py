class IO:
    GREETING_MSG = "Hi! Thanks for calling Joe's Pizza. How can I help you today?"
    ORDER_INSTRUCTION_MSG = "Great! How many pizzas will you be ordering?"
    NAME_INSTRUCTION_MSG = "Thanks! I need a name for the order. What's your name?"
    PRICE_QUOTE_MSG = "Our large pizzas are $20, and our small pizzas are $10. Pepperoni or vegetarian pizzas cost $2 extra. Would you like to place an order?"
    OPERATOR_MSG = "I'll send you to an operator now."
    INVALID_INPUT_MSG = "Invalid input, please try again."


    @staticmethod
    def read_input(prompt):
        return input(prompt).strip().lower()  
    
    @staticmethod
    def print_message(message):
        print(message)

    @staticmethod
    def display_greeting():
        IO.print_message(IO.GREETING_MSG)

    @staticmethod
    def display_order_instruction():
        IO.print_message(IO.ORDER_INSTRUCTION_MSG)


    @staticmethod
    def display_name_instruction():
        IO.print_message(IO.NAME_INSTRUCTION_MSG)

    @staticmethod
    def display_operator_message():
        IO.print_message(IO.OPERATOR_MSG)

    @staticmethod
    def display_invalid_input():
        IO.print_message(IO.INVALID_INPUT_MSG)

    @staticmethod
    def read_keypad_input(prompt):
        while True:
            response = input(prompt).strip()  
            if response.isdigit() and 0 <= int(response) <= 9:
                return int(response)
            else:
                IO.print_message("Please enter a number from 0 to 9.")

    @staticmethod
    def display_pizza_size(pizza_number):
        IO.print_message(f"Thanks! Lets get the details for pizza number {pizza_number}. What size will the pizza be?")

    @staticmethod
    def display_pizza_size_input(pizza_number):
        IO.print_message(f"Ok, {pizza_number} pizzas.")
        
    @staticmethod
    def display_toppings(pizza_size):
        IO.print_message(f"A {pizza_size} size pizza. What kind of pizza will you have? You can say cheese, pepperoni, or vegetarian")
        
    @staticmethod
    def display_goodbye(name):
        IO.print_message(f"Okay {name}, your order will be ready in 30 minutes.  See you soon!")
        
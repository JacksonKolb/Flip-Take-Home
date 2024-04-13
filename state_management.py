from abc import ABC, abstractmethod
from IO import *

class StateContext:
    def __init__(self):
        self.state = None
        self.last_message = ""

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

class StateBase(ABC):
    @abstractmethod
    def handle(self, context, user_input):    
        if user_input == '0':
            IO.display_operator_message
            context.set_state(ExitState())
            return True
        elif user_input == 'repeat':
            IO.print_message(context.last_message)
            return True


class GreetState(StateBase):
    def handle(self, context):
        while True:
            IO.display_greeting()
            user_input = IO.read_input(">>> ").lower()
            if super().handle(context, user_input):
                break
            if 'order' in user_input:
                context.set_state(OrderState())
                break
            else:
                IO.display_invalid_input()



class OrderState(StateBase):
    def handle(self, context):
        num_pizzas = IO.read_keypad_input(IO.ORDER_INSTRUCTION_MSG)
        if super().handle(context, num_pizzas):
            return
        if num_pizzas > 0:
            context.order = {'pizzas': num_pizzas, 'details': []}
            context.set_state(PizzaOrderState())


class PizzaOrderState(StateBase):
    def __init__(self):
        self.pizza_index = 0
        self.step = 'size'

    def handle(self, context):
        if self.step == 'size':
            self.handle_pizza_size(context)
        elif self.step == 'type':
            self.handle_pizza_type(context)

    def handle_pizza_size(self, context):
        IO.display_pizza_size(self.pizza_index + 1)
        pizza_size = IO.read_input(">>> ").lower()
        if super().handle(context, pizza_size):
            return
        if pizza_size in ['small', 'large'] :
            context.order['details'].append({'size': pizza_size})
            self.step = 'type'

    def handle_pizza_type(self, context):
        IO.display_toppings(context.order['details'][self.pizza_index]['size'])
        pizza_type = IO.read_input(">>> ").lower()
        if super().handle(context, pizza_type):
            return
        if pizza_type in ['cheese', 'pepperoni', 'vegetarian']:
            context.order['details'][self.pizza_index]['type'] = pizza_type
            self.pizza_index += 1
            if self.pizza_index >= context.order['pizzas']:
                context.set_state(CustomerNameState())
            else:
                self.step = 'size'


class CustomerNameState(StateBase):
    def handle(self, context):
        IO.display_name_instruction()
        customer_name = IO.read_input(">>> ").strip()
        if super().handle(context, customer_name):
            return
        if customer_name:
            context.order['customer_name'] = customer_name
            IO.display_goodbye(customer_name)
            context.set_state(ExitState())

class ExitState(StateBase):
    def handle(self, context):
        IO.print_message("Goodbye!")
        context.set_state(None)

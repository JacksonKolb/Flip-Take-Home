from state_management import StateContext, GreetState

def main():
    context = StateContext()
    context.set_state(GreetState())

    while context.state is not None:
        context.request()

if __name__ == "__main__":
    main()

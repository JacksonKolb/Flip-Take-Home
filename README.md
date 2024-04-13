# Pizza Assistant

This is a simple Python application that assists users in ordering pizzas through a command-line interface.
 
## Getting Started

To run the Pizza Assistant application, you can use Docker. Follow the steps below to build and run the Docker container:

### Prerequisites

- Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

### Running the Pizza Assistant Application

To run the Pizza Assistant application inside a Docker container, you first need to ensure that the `build-and-run.sh` script is executable. You can achieve this by running the following command in the project directory, which for me looks like :

```bash
~/Workspace/Flip-Take-Home$ chmod +x build_and_run.sh
```

Once the script is executable, you can start the application by running:

```bash
./build_and_run.sh
```
This script handles the building of the Docker image and starts the application in a Docker container, opening the Pizza Assistant interface in interactive mode (-it). By executing this script, all necessary steps from building the image to running the container are managed automatically.

## Design Decisions

### State Management Pattern
- **Why we used it**: We chose the state management pattern to manage the user interactions step-by-step. It helps keep the code organized, especially when dealing with a bunch of different user input stages.
- **What's good about it**:
  - **Keeps things separate**: Each state like `GreetState` and `OrderState` handles its own thing. This makes it easier to understand and manage.
  - **Easy to add more**: Adding new steps or types of interactions is straightforward, which is great for future updates.

### Use of Abstract Base Classes (ABC)
- **Why this approach**: `StateBase` is an abstract class that sets a standard for all states. Every state must have a `handle` method, which keeps things consistent across the board.
- **Benefits**:
  - **Uniformity**: Ensures all states handle inputs in a consistent manner.
  - **Customizability**: Allows each state to implement necessary methods uniquely.

### Dependency on Static Methods for I/O
- **Why go static**: We used static methods in the `IO` class so we can call them anywhere without creating an instance. It simplifies the code and keeps input/output management centralized. **That way when this inevitably grows to N users, we can rip this class out and replace it with front-end library stuff. No more terminal/text-based, hurray!**
- **Why it helps**:
  - **Ease of use**: Just use the class name to call methods, which is straightforward.
  - **One place to manage**: Makes it easier to change how messages are shown or inputs are handled from one place.


## Possible Improvements

1. **Robust User Input Handling**:
   - **Current Issue**: Right now, we kind of expect that users will always enter the right stuff after just one prompt. There is some error handling here and there, but it's inconsistent.
   - **Fix**: We could beef up the error handling, and maybe put this logic into the `IO` class to avoid repeating ourselves.

2. **Use of Enums**:
   - **Current Issue**: There are some hardcoded strings in the state manager, which couples implementation details to our rules. 
   - **Fix**: Enums or something similar. That way if we add size "medium" we don't need to update implementation details. This makes things less imperative and less brittle.

3. **Separation of Concerns**:
   - **Current Issue**: `IO` class handles both input and output, as well as consts.
   - **Fix**: Split it into two classes – one for input and another for output. This makes the code cleaner and adheres to the Single Responsibility Principle. We can also break those consts into a consts file, but I don't feel strongly about that yet due to current scale.

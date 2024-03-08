class Assistant:
    def __init__(self, name, description, model, model_config, main_agent, tools, memory=None):
        self.name = name
        self.description = description
        self.model = model
        self.model_config = model_config
        self.main_agent = main_agent
        self.tools = tools
        self.memory = memory or {}

    def show_information(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Model: {self.model}")
        print(f"Model Configuration: {self.model_config}")
        print(f"Main Agent: {self.main_agent}")
        print(f"Tools: {', '.join(self.tools)}")
        print(f"Memory: {self.memory}")
        
    def __str__(self):
        return f"Name: {self.name} , Description: {self.description} , Model: {self.model}"


    def add_to_memory(self, key, value):
        self.memory[key] = value

# Create an instance of Assistant
my_assistant = Assistant(
    name="Asis1",
    description="Test Assistant",
    model="Model1",
    model_config={"parameter1": "value1"},
    main_agent="MainAgent1",
    tools=["Tool1", "Tool2"]
)

# Show information about the assistant
my_assistant.show_information()

# Add a data to the assistant's memory
my_assistant.add_to_memory("data1", "information1")

# Show updated information
my_assistant.show_information()

bbb
jkjjjj
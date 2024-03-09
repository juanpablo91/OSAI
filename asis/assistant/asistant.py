


class Asis:
    def __init__(self, name, description, model_name, model_config, main_agent, tools, memory=None):
        self.name = name
        self.description = description
        self.mode_name = model_name
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
    
    #load the model choices
    def loadModel(self, model):
        self.model = Model(self.model_name)
        self.model.upload_model()        


    def add_to_memory(self,):
        self.memory[key] = value



my_assistant = Asis(
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

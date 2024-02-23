from openai import OpenAI
client = OpenAI(api_key="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")

class Character:

    def __init__(self, description, name):
        self.description = description
        self.name = name
        self.history = []

    def describe_character(self):
        return f"{self.description}. Your name is {self.name}"
    
    def update_character(self, description="", name=""):
        if description: self.description = description
        if name: self.name = name

    def history_length(self):
        return len(self.history)
    
    def get_history(self):
        for item in self.history:
            print(item)

    def get_name(self):
        return self.name
    
    def create_new(self, message):
        self.history = []
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system", "content": f"{self.description}. Your name is {self.name}"},
                {"role":"user", "content":message}
            ]
        )

        self.history.append({"role":"user","content":message})
        self.history.append({"role":completion.choices[0].message.role,"content":completion.choices[0].message.content})
        return(completion.choices[0].message.content)
    
    def cont(self, message, debug=False):
        message_history = []

        for item in self.history:
            message_history.append(item)

        if debug == True: print(message_history[:])

        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system", "content": f"{self.description}. Your name is {self.name}"},
                *message_history,                
                {"role":"user","content":message}
                ]
        )

        self.history.append({"role":"user","content":message})
        self.history.append({"role":completion.choices[0].message.role,"content":completion.choices[0].message.content})
        return(completion.choices[0].message.content)
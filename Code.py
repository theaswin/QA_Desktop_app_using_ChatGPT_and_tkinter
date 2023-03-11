import openai
import pytesseract
import cv2
import re
from pytesseract import Output
openai.api_key = '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'
import tkinter as tk

while True:
    
    window = tk.Tk()
    window.title("My window")
    window.geometry("1200x750")
    window.resizable(False,False)
    image = tk.PhotoImage(file="./assets/Upper.png")
    label = tk.Label(window,image=image)
    label.place(x=0,y=0)
    # Giving labels
    # Getting entry
    entry = tk.Entry(window)
    # place of the entry
    entry.config(font=('Ariel',20))
    entry.place(x=750,y=150)


    # Function for receiving input from user
    def get_input():
        InputQuestion = entry.get()


        Question = InputQuestion

        # Set the model and parameters
        model_engine = "text-davinci-002"
        temperature = 0.7
        max_tokens = 60



        # Generate the translation using the OpenAI API
        response = openai.Completion.create(
            engine=model_engine,
            prompt=f"Answer the question {Question}",
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the translation from the response
        Answer = response.choices[0].text.strip()

        displayAnswer=tk.Label(window,text=Answer)
        displayAnswer.config(font=('Ariel',17))
        displayAnswer.place(x=00,y=500)

    def RestartButton():
        pic = tk.PhotoImage(file='./assets/Cover.png')
        labelFOrImage = tk.Label(window,image=pic)
        labelFOrImage.place(x=0,y=390)
    
    # Button for submit
    submit = tk.Button(window,text="  ▶ Run ",command=get_input,relief='raised',bg='black',fg='grey')
    Restart = tk.Button(window,text=" ↻ Restart ",command=RestartButton,relief='raised',bg='black',fg='grey')
    submit.config(font=('Ariel',20))
    Restart.config(font=('Ariel',20))
    Restart.place(x=950,y=280)
    submit.place(x=810,y=280)
    break




window.mainloop()

from flask import Flask, render_template, request

app = Flask(__name__)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(plain_text, shift_amount, EncodeorDecore):
    OriginalText = ""
    # Adjust shift for decoding
    if EncodeorDecore == "decode":
        shift_amount *= -1
    
    for letter in plain_text:
        # Only shift letters, skip spaces or non-alphabet characters
        if letter in alfabeto:
            # Find the current position and apply the shift
            ShiftPosition = (alfabeto.index(letter) + shift_amount) % len(alfabeto)
            OriginalText += alfabeto[ShiftPosition]
        else:
            # If it's not a letter, keep the character as it is (spaces, punctuation)
            OriginalText += letter
    
    return OriginalText

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        direction = request.form["direction"]
        text = request.form["text"].lower()  # Convert to lowercase to match alphabet
        shift = int(request.form["shift"]) % len(alfabeto)  # Ensure shift is within bounds
        
        result = ceasar(plain_text=text, shift_amount=shift, EncodeorDecore=direction)
        
        return render_template("index.html", result=result, direction=direction, text=text, shift=shift)
    
    return render_template("index.html", result="")

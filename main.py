from pyscript import document

def check_eligibility(event):
    # Fetch inputs from HTML
    reg = document.querySelector('input[name="answer1"]:checked')
    med = document.querySelector('input[name="answer3"]:checked')
    section = document.getElementById("sct").value
    result_element = document.getElementById("Result")
    
    # 1. Validation check
    if not reg or not med:
        result_element.innerHTML = "<span style='color:red;'>Please answer all questions completely.</span>"
        return

    # 2. Eligibility logic check
    if reg.value == "no":
        result_element.innerHTML = "❌ <b>Instruction:</b> Please register online through the link provided by your advisor."
    elif med.value == "no":
        result_element.innerHTML = "❌ <b>Instruction:</b> Please consult the clinic to secure your medical clearance."
    else:
        # 3. Team assignment mapping to your specific image filenames
        # Note: 'tigers.jpg' is used here. Make sure the filename on GitHub matches this.
        teams = {
            "TOPAZ": ("Green Hornets", "hornets.jpg"),
            "RUBY": ("Blue Bears", "bears.jpg"),
            "SAPPHIRE": ("Red Bulldogs", "bulldogs.jpg"),
            "EMERALD": ("Yellow Tigers", "tigers.jpg")
        }
        
        team_name, img_filename = teams.get(section)
        
        # 4. Success Output with Image
        result_element.innerHTML = f"""
            <div style="text-align: center;">
                <p style="color: green; font-weight: bold; font-size: 1.2rem;">Congratulations!</p>
                <p>You are part of the <b>{team_name}</b>!</p>
                <img src="{img_filename}" alt="{team_name}" style="max-width: 200px; height: auto; border-radius: 10px; margin-top: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            </div>
        """
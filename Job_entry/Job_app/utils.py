from fontawesome_5.fields import IconField

def generate_font_awesome_choices():
    choices = [(icon, icon.replace('fa-', '').title()) for icon in IconField.choices]
    return choicesy
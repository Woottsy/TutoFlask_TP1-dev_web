from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, DecimalField
from wtforms.validators import DataRequired

class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])
    
class FormLivre(FlaskForm):
    idL=HiddenField('idL')
    Titre = StringField ('Titre')
    Prix = DecimalField ('Prix', validators =[DataRequired()])
    Img = StringField ('Premiere de couverture')
    Auteur_id = StringField ('idA')
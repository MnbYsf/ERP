from odoo import models, fields

class TpAttestation(models.Model):
    _name = "tp.attestation"
    _description = "Attestation"

    name = fields.Char(string="Nom de l'attestation", required=True)
    etudiant = fields.Char(string="Nom de l'étudiant")
    date_creation = fields.Date(string="Date de création")
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("valide", "Validée"),
        ("annulee", "Annulée"),
    ], string="Statut", default="brouillon")
    description = fields.Text(string="Description")

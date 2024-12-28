"""
Python Dictionaries with translasions and transliterations.
Used to store translations from different to populate the traslations.json file.
Contains regex funtions to harmonize different names for the same region from different sources (Todo).
Contains function to traslate across three languages in the translation.json output file (Todo).
Notes:
    a) "Στερεά Ελλάδα" is translated as "Sterea Ellada", because there is a NUTS_1 Central Greece too that includes more nuts2 regions.
    b) Check why "Ευρυτανία" has been singled out in the implementation, although it belongs to "Sterea Ellada".
    c) Pelopennes is broken to two areas because of different grant limits.
    d) Todo: Aggregate in NUTS 1.
"""

# Region names from MIS source
MIS_REGIONS_TRANSLATIONS_GR_EN = {
    "Ιονίων Νήσων": "Ionian Islands",
    "Αττικής": "Attica",
    "Κεντρικής Μακεδονίας": "Central Macedonia",
    "Θεσσαλίας": "Thessaly",
    "Κρήτης": "Crete",
    "Στερεάς Ελλάδας": "Sterea Ellada",
    "Ηπείρου": "Epirus",
    "Πελοποννήσου": "Peloponnese",
    "Δυτικής Ελλάδας": "Western Greece",
    "Ανατολικής Μακεδονίας και Θράκης": "Eastern Macedonia and Thrace",
    "Δυτικής Μακεδονίας": "Western Macedonia",
    "Νοτίου Αιγαίου": "South Aegean",
    "Βορείου Αιγαίου": "North Aegean",
}

# Region names from the official Implementation guide
# Check why 'Ευρυτανία has been singled out.

OFFICIAL_GUIDE_REGIONS_TRANSLITERATIONS_GR_EN = {
    'Βόρειο Αιγαίο': 'Voreio Aigaio',
    'Κρήτη': 'Crete',
    'ΑνατολικήΜακεδονία- Θράκη': 'Eastern Macedonia and Thrace',
    'Κεντρική Μακεδονία': 'Central Macedonia',
    'Δυτική Μακεδονία': 'Western Macedonia',
    'Ήπειρος': 'Epirus',
    'Θεσσαλία': 'Thessaly',
    'Ιόνια Νησιά': 'Ionian Islands',
    'Δυτική Ελλάδα': 'Western Greece',
    'Στερεά Ελλάδα': 'Sterea Ellada',
    'Ευρυτανία': 'Sterea Ellada',
    'Πελοπόννησος:Δήμοι Μεγαλόπολης,Γορτυνίας Τρίπολης Οιχαλίας': 'Peloponnese: Megalopolis, Gortynia, Tripoli, Oichalia',
    'Πελοπόννησος:Λοιποί Δήμοι': 'Peloponnese: Other Municipalities',
    'Νότιο Αιγαίο': 'South Aegean',
}

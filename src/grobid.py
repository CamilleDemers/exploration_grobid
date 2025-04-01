from grobid_client.grobid_client import GrobidClient

# To-do : traiter les sous-dossiers contenant les PDFs pour chacune des revues individuellement,
# puis stocker les fichiers XML/TEI dans des sous-dossiers correspondant (pour l'instant, les fichiers 
# ont été mis manuellement dans le dossier pdfs pour chaque revue une à la fois)

client = GrobidClient(config_path='config.json')
client.process(
    'processFulltextDocument', 
    input_path='pdfs', 
    output='xml_tei'
)
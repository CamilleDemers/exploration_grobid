import os
import pandas as pd
from slugify import slugify
from bs4 import BeautifulSoup

# Reference : https://komax.github.io/blog/text/python/xml/parsing_tei_xml_python/

def xml_tei_to_df(folder:str) -> pd.DataFrame:
    # créer une liste de dictionnaires qui deviendra notre dataframe
    df = []

    # Renommer les fichiers au besoin
    tei_docs = os.listdir(folder)

    for file in tei_docs:
        tei_doc = '-'.join(slugify(file).split('-')[:6])
        os.rename(os.path.join(folder, file), os.path.join(folder, tei_doc + '.xml'))

        # Parser le XML du fichier avec BeautifulSoup
        with open(f'{folder}/{tei_doc}.xml', 'r', encoding='utf-8') as tei:
            soup = BeautifulSoup(tei, features='xml')

            # doi
            try:
                doi = soup.find('idno', type='DOI').getText()
            
            except:
                print(tei_doc, 'no doi info')
                doi=None

            # premier auteur
            try:
                first_author = soup.author.persName.get_text(" ")
            except:
                print(tei_doc, 'no first author info')
                first_author=None

            # titre
            try:
                title = soup.title.getText()
            except:
                print(tei_doc, 'no title info')
                title=None

            # résumé
            abstract = soup.abstract.get_text() if soup.abstract else None       

            # date de publication
            try:
                publication_date = soup.find('date', type='published')['when']
            except:
                print(tei_doc, 'no date info')
                publication_date=None

            # nom du périodique
            try:
                journal_title = soup.find('title', level='j').getText()
            except:
                print(tei_doc, 'no journal info')
                journal_title=None

            # nom de l'éditeur
            try:
                publisher = soup.publisher.getText()            
            except:
                print(tei_doc, 'no publisher info')
                publisher=None

            # corps du texte
            body = ''
            try:
                body = "\n".join(
                    [
                        (section.find('head').get_text() if section.find('head') else "") +
                        "\n" +
                        "\n".join([p.get_text() for p in section.find_all('p')])
                        for section in soup.body.find_all('div', recursive=False)
                    ]
                )
                    
            except:
                print(tei_doc, 'no body info')
                body=None


            # Stocker le corps du texte dans un fichier txt (pour consultation)
            if not os.path.exists(f'txts/{folder[11:]}'): # Créer un sous-dossier au besoin
                os.makedirs(f'txts/{folder[11:]}')
            txt_file_name = f'txts/{folder[11:]}/{tei_doc}.txt'
            with open(txt_file_name, 'w', encoding='utf-8') as f:
                f.write(body)                 

            dic = {
                'doi' : doi,
                'first_author' : first_author,
                'title' : title,
                'abstract' : abstract,
                'published' : publication_date,
                'journal' : journal_title,
                'publisher' : publisher,
                'body' : body
            }

        df.append(dic)

    return pd.DataFrame(df)

xml_dirs = os.listdir('xml_tei')

for xml_dir in xml_dirs:
    df = xml_tei_to_df('xml_tei/' + xml_dir)

    csv_file_name = xml_dir
    df.to_csv('csvs/' + xml_dir + '.csv', index=False)
# Curso-PLN
Contenido del curso: Introducción a los concetos de NLP: Cod Fac.

## Descripción de scripts:

* RT.ipynb: Transformación de un corpus en lenguaje natural a una representación de términos y documentos.
* w2v.py: Manipulación de un modelo de word embeddings en español, para su uso es necesario descargar un modelo pre-entrenado. (https://github.com/dccuchile/spanish-word-embeddings)
* austinHouseData.csv: Corpus para la predicción del precio de una casa a partir de su descripción.
* FakeNews: Corpus procesado y pre-etiquetado de noticias falsas y verdaderas. (https://mega.nz/file/sz8SXbYK#hGEhjDrB9LIb4MA_Iuv5y-5oudCv1AtR-zPH-rDKwyc)

### Descarga de modelos para RT.ipynb
* Descargar modelo de Porter (stemming) desde script para Natural Language Toolkit: nltk.download("punkt") 
* Descargar modelo de lemmatización y stopwords desde la terminal para Spacy: python -m spacy download en_core_web_sm

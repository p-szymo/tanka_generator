# tankanizer

Using Allison Parrish's [Pronouncing](https://github.com/aparrish/pronouncingpy) to count syllables, I experiment with generating poetry in the tanka form using several corpora and a Markov chain.

Thinking as I'm typing that perhaps I can use the Markov chain to generate poetry that I can then use to train a more sophisticated RNN generator. Some sort of text generation loop.

Early stages!

## List of files
- **data** folder - text files to use as a source for the generator.
<!-- - **scrap_files** folder - backups, old workbooks, old texts/jsons, and other scraps.
  - includes NLTK-tokenized version of dictionary with some punctuation (poetic apostrophes and hyphens)
    - lacks some proper segmentation but not as oversegmented as the wordninja version -->
- **.gitignore** - list of files to ignore.
<!-- - **Procfile** - requirement for Heroku deploy. -->
- **README.md** - this very file!
<!-- - **app.py** - file with app layout and tankanizer function (reconfigured for use with Streamlit). -->
- **tankanizer.ipynb** - the main workbook, polished, from beginning to end. One can start by opening from the Markov dictionary.
- **functions.py** - text file with functions, from processing text to the final poetry generator.
<!-- - **requirements.txt** - requirement for Heroku deploy.
- **scraping_sandbox.ipynb** - notebook with an example of scraping the work of one particular poet.
- **setup.sh** - requirement for Heroku deploy. -->
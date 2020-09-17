# tankanizer

Using Allison Parrish's [Pronouncing](https://github.com/aparrish/pronouncingpy) to count syllables, I generate poetry in the tanka form using a corpus of Walt Whitman poems (created in [this notebook](https://github.com/p-szymo/poetrydb_poem_generator/blob/master/scraping_sandbox.ipynb) within my [poetrydb_poem_generator](https://github.com/p-szymo/poetrydb_poem_generator) project) and a Markov chain.

NOTE: A tanka is a poetic form originating in Japan, comprised of five lines in a distinct 5-7-5-7-7 syllabic structure.

## To use the app locally, run the following in Terminal (after cloning the repo):
```streamlit run app.py```

## Future steps

Within the app, I'd like users to be able to upload a corpus and use it to generate poetry.

In a larger context, I'd like to use Markov chain across several corpora to generate poetry that I can then use to train a more sophisticated RNN (LSTM) generator. I envision some sort of text generation loop, the visual/written equivalent of audio feedback.

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
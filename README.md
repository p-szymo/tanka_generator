# [tankanizer](https://peaceful-sierra-10406.herokuapp.com/)
## a Markov chain poetry generator with syllabic constraints

Using Allison Parrish's [Pronouncing](https://github.com/aparrish/pronouncingpy) to count syllables, I generate poetry in the tanka form with a corpus of Walt Whitman poems and a Markov chain. A tanka is a poetic form originating in Japan, comprised of five lines in a distinct 5-7-5-7-7 syllabic structure.

NOTE: The corpus was created in [this notebook](https://github.com/p-szymo/poetrydb_poem_generator/blob/master/scraping_sandbox.ipynb) within my [poetrydb_poem_generator](https://github.com/p-szymo/poetrydb_poem_generator) project.

## To use the app locally, run the following in Terminal (after cloning the repo):
```streamlit run app.py```

## To use the app on the World Wide Web, click [here](https://peaceful-sierra-10406.herokuapp.com/)!

## Future steps

I'd like to allow users to upload a corpus within the app, which would then process the text and create a usable Markov dictionary to act as the source for the tankanizer.

In a larger context, I'd like to use Markov chain across several corpora to generate poetry that I can then use to train a more sophisticated RNN (LSTM) generator. I envision some sort of text generation loop, the visual/written equivalent of audio feedback.

## List of files
- **data** folder - text files to use as a source for the generator.
- **.gitignore** - list of files to ignore.
- **Procfile** - requirement for Heroku deploy.
- **README.md** - this very file!
- **app.py** - file with app layout and tankanizer function call.
- **functions.py** - text file with functions, from processing text to the final poetry generator.
- **requirements.txt** - requirement for Heroku deploy.
- **setup.sh** - requirement for Heroku deploy.
- **tankanizer.ipynb** - the main workbook, from loading and processing the corpus to generating some tankas.
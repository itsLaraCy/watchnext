
import spacy
import numpy as np
nlp = spacy.load("en_core_web_md")

# create a function to return which movies a user would watch next.
def next_movies(description):
    similarities= []

    sentence_to_compare = nlp(description)
    for movie in movies:
        similarities.append(sentence_to_compare.similarity(nlp(movie)))
    index = np.argmax(similarities)
    recommendations = movies[index]
    return recommendations
# Read in the movies.txt file. Each separate line is a description of a different movie
file=open("movies.txt", "r")
movies = file.readlines()
descriptions=[]
for movie in movies:
    details = movie.split(":")
    descriptions.append(details[1])
file.close()
print(next_movies("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."))

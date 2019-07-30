# parser, updated for Nexmo integration
# TODO: "interpret" lemmatized words and form response messages

# import NLP libraries
import nltk
from nltk.tokenize import word_tokenize

def parse_report(report = ''):
    # function call to split string into individual words (tokenize)
    tokens = word_tokenize(report)
    nltk.download('stopwords')
    print(tokens)

    # function call to remove stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))

    # reassign to tokens if not a stop word
    tokens = [w for w in tokens if not w in stop_words]
    print(tokens)

    # lemmatize (as opposed to stemming)
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet
    lem = WordNetLemmatizer()

    # get parts of speech for each word
    def get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    # lemmatize sentence
    tokens = ' '.join(lem.lemmatize(w, get_wordnet_pos(w)) for w in tokens)
    print(tokens)

    return

# test calls
parse_report("There is a student with a gun.")
parse_report("active shooter")
parse_report("There's a fire")
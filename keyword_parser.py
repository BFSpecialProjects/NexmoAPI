# parser, updated for Nexmo integration
# TODO: "interpret" lemmatized words and form response messages

# import NLP libraries
import nltk
from nltk.tokenize import word_tokenize

def parse_report(report = ''):
    # function call to split string into individual words (tokenize)
    tokenized_report = word_tokenize(report)
    nltk.download('stopwords')
    print(tokenized_report)

    # function call to remove stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))

    # reassign to tokens if not a stop word
    tokenized_report = [w for w in tokenized_report if not w in stop_words]
    print(tokenized_report)

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
    # tr = finalized tokenized report
    tr = ' '.join(lem.lemmatize(w, get_wordnet_pos(w)) for w in tokenized_report)
    print(tr)

    identify_threat(tokenized_report)

    return

def identify_threat(tr):
    # function to see if message actually denotes a threat
    
    # import premade model
    import gensim
    model = gensim.models.KeyedVectors.load('incident_model.model')
    
    # doesn't need more training, init_sims to save memory
    model.init_sims(replace=True)

    # compare user input to root word
    # if word matches a known threat, move on to reporting
    # else return error to user
    for w in tr:
        try:
            if (model.similarity(w, 'gun') > .4):
                print ('True')
                break
            elif (model.similarity(w, 'fire') > .4):
                print ('True')
                break
            else:
                print ('False')
        except:
            # instead of trying to process a contraction (which returns and eror)
            # just pass over apostrophe
            pass
    return

# test calls
parse_report("There is a student with a gun")
parse_report("active shooter")
parse_report("There's a fire")
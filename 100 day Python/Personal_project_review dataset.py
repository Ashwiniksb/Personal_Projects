import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

df = pd.read_excel(r"C:\Users\lenovo\Downloads\Data Analyst - Test Data.xlsx")
df.info()
df.head()

#understand the range of dates the data is taken from.
date_min = df['date'].min()
date_max = df['date'].max()
print(date_min, date_max) #it is from August of 2018 to August of 2019.

df['review_pro'] = df['Review'].str.lower()
df['review_pro'] = df['review_pro'].str.replace('[^A-Za-z0-9]' , ' ', regex = True)

#char = re.findall('[^A-Za-z0-9]', df['review_pro'][0])
#print(char)

#then we tokenize

# =============================================================================
# for i in range(1, 6449):
#     df['review_pro'][i] = df['review_pro'][i].apply(lambda text: nltk.word_tokenize(text))
# =============================================================================

df['review_pro'] = df['review_pro'].astype(str).apply(nltk.word_tokenize) 

#remove stopwords from the list of above words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
df['review_pro'] = df['review_pro'].apply(lambda tokens: [word for word in tokens if word not in stop_words])

lemm = WordNetLemmatizer()

def lemmatize_words(word_list):
    return [lemm.lemmatize(word) for word in word_list]

df['review_pro'] = df['review_pro'].apply(lemmatize_words)
df['review_pro'] = df['review_pro'].apply(' '.join)

# =============================================================================
# text = "I am very very Happy and greatful"
# analysis = TextBlob(text)
# sentiment = analysis.sentiment.polarity
# =============================================================================

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    return sentiment

df['sentiment_score'] = df['review_pro'].apply(analyze_sentiment)

def sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
        
df['sentiment'] = df['sentiment_score'].apply(sentiment)

#convert to csv to get the dataset downloaded
df['Review'].dropna(inplace=True)

csv_file_path = r"C:\Users\lenovo\Downloads\Review_assignment.csv"
df.to_csv(csv_file_path, index=False) 



positive = (df['sentiment'] == 'Positive').sum()
negative = (df['sentiment'] == 'Negative').sum()
neutral = (df['sentiment'] == 'Neutral').sum()

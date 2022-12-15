
from summarization import summarize
from sentiment_analysis import sentiment
from recommendation_bookmark import recommendation_bookmark
from recommmendation_gpt import recommmendation_gpt
from data_query import generate_articles

interest_list = ["crypto news", "soccer", "developer tools"]
def main():
    article_list = generate_articles(top=250)
    # article_list --> tuples of title & url 
    filtered_list  = sentiment(article_list)
    open_end_recs = recommmendation_gpt(filtered_list,interest_list[0])
    #bookmark_recs = recommendation_bookmark(filtered_list)
    user_recs = summarize(open_end_recs) #+ summarize(bookmark_recs)
    return user_recs # tuples of title & summary 
if __name__ == "__main__" :
    main()
from hn import HN
from hn import Story


def generate_articles(top):
    hn = HN()
    # get top articles from HN , manual query for twitter data due to API limit 
    id_list = hn.get_stories(story_type='best', limit=top)
    article_list = [(Story.fromid(id).title, Story.fromid(id).url) for id in id_list]
    return article_list

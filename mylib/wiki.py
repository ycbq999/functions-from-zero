import wikipedia
from yake import KeywordExtractor

#build a function to return the summary of a wikipedia page
def get_wiki_summary(page):
    """
    This function returns the summary of a wikipedia page
    """
    return wikipedia.summary(page)

#build a function to search wikipedia pages for a match
def search_wiki_pages(query):
    """
    This function searches wikipedia pages for a match
    """
    return wikipedia.search(query)


#build a function to return the wikipedia page
def get_wiki_page(page):
    """
    This function returns the wikipedia page
    """
    return wikipedia.page(page)

#return the keywords from a wikipedia page
def get_wiki_keywords(page):
    """
    This function returns the keywords from a wikipedia page
    """
    content = get_wiki_page(page).content
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    #return a dictionary of the top 10 keywords
    return {keyword[0]: keyword[1] for keyword in keywords[:10]}


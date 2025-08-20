class Article:
    @staticmethod
    def all():
        return Article._all_articles

    @staticmethod
    def reset_all():
        Article._all_articles.clear()
    # Track all articles
    _all_articles = []
    def __init__(self, author, magazine, title):
        # ...existing code...
        Article._all_articles.append(self)
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value
        
class Author:
    def articles(self):
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})

class Magazine:
    @staticmethod
    def all():
        return Magazine._all_magazines

    @staticmethod
    def reset_all():
        Magazine._all_magazines.clear()
    # Track all magazines
    _all_magazines = []
    def __init__(self, name, category):
        # ...existing code...
        Magazine._all_magazines.append(self)

    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("category must be a non-empty string")
        self._category = value

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [art.title for art in arts]

    def contributing_authors(self):
        from collections import Counter
        arts = self.articles()
        if not arts:
            return None
        author_counts = Counter([art.author for art in arts])
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        mags = cls._all_magazines
        if not mags:
            return None
        return max(mags, key=lambda mag: len(mag.articles()), default=None) if any(mag.articles() for mag in mags) else None
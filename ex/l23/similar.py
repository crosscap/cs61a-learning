class Restaurant:
    """A restaurant."""
    all = []
    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=num_shared_reviewers):
        """Return the K most similar restaurants to SELF, 
        using SIMILARITY for comparison."""
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(r, self))[:k]

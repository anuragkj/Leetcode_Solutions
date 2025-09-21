from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        # Dictionary to store available movies, mapping movie -> SortedList of (price, shop)
        self.available = {}
        # SortedList to store rented movies, sorted by (price, shop, movie)
        self.rented = SortedList()
        # Dictionary to map (shop, movie) -> price for fast lookup during rent and drop operations
        self.shop_movie_price = {(shop, movie): price for shop, movie, price in entries}

        # Populate the available dictionary with the provided entries
        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))  # Add available movie to SortedList

    def search(self, movie: int) -> list[int]:
        """
        Returns up to 5 shops that have an unrented copy of the given movie,
        sorted by price (ascending) and shop (ascending in case of tie).
        """
        # Retrieve the first 5 shops for the given movie, or an empty list if no available copies
        return [shop for _, shop in self.available.get(movie, [])[:5]]

    def rent(self, shop: int, movie: int) -> None:
        """
        Rents a movie from the given shop, removes the unrented copy from the available list,
        and adds it to the rented list.
        """
        price = self.shop_movie_price[(shop, movie)]  # Get the price of the movie
        # Remove from available list (unrented movies)
        self.available[movie].remove((price, shop))
        # Add to rented list
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Returns a rented movie back to the shop, removes it from the rented list,
        and adds it back to the available list.
        """
        price = self.shop_movie_price[(shop, movie)]  # Get the price of the movie
        # Remove from rented list
        self.rented.remove((price, shop, movie))
        # Add back to available list (unrented movies)
        self.available[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        """
        Returns up to 5 of the cheapest rented movies, sorted by price, shop (in case of tie), 
        and movie (in case of further tie).
        """
        # Retrieve the first 5 rented movies from the rented list
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

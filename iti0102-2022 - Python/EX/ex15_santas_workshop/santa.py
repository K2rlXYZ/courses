"""Santa gaming.py."""
import requests
import urllib.parse as url_encode


class NiceAndNaughtyList:
    """List class for the nice and naughty lists."""

    def __init__(self, nice_list_file_name: str, naughty_list_file_name: str):
        """Construct this class."""
        self.nice_list = []
        for line in open(nice_list_file_name, encoding="utf-8"):
            temp = line.split(", ")
            self.nice_list.append((temp[0], temp[1].strip()))
        self.naughty_list = []
        for line in open(naughty_list_file_name, encoding="utf-8"):
            temp = line.split(", ")
            self.naughty_list.append((temp[0], temp[1].strip()))

    def get_naughty_list(self):
        """Return naughty list."""
        return self.naughty_list

    def get_nice_list(self):
        """Return nice list."""
        return self.nice_list


class Wishlist:
    """Create a class for containing a list for the wishes of the children."""

    def __init__(self, filename: str):
        """Construct this class."""
        self.wishes = {}
        for line in open(filename, encoding="utf-8"):
            temp = line.split(", ")
            self.wishes[temp[0]] = [x.strip() for x in temp[1:-1]] + [temp[-1].strip()]

    def get_wishes(self):
        """Return wishlist."""
        return self.wishes


class ProductionAndStock:
    """Create a class to conatin info about products and stock."""

    def __init__(self, query_url: str, nice_and_naughty_lists: NiceAndNaughtyList, wishlist: Wishlist):
        """Construct this class."""
        self.query_url = query_url
        self.nice_and_naughty_lists = nice_and_naughty_lists
        self.wishlist = wishlist
        self.products = {}
        self.recipients = {}

    def get_product_info(self, product_name: str):
        """Get product info from web."""
        r = requests.get(self.query_url + url_encode.quote(product_name))
        return r.text

    def parse_product_info(self, product_info):
        """Parse the product info to a more interpretable form."""
        temp = product_info.strip("{").strip("}").split(",")
        temp = [x.split(":") for x in temp]
        temp = [[y.strip("\"") for y in x] for x in temp]
        temp1 = {}
        for x in temp[1:-1] + [temp[-1]]:
            temp1[x[0]] = x[1]
        product = [temp[0][1], temp1]
        return product

    def add_parsed_product_info(self, product):
        """Add parsed info to products list."""
        self.products[product[0]] = product[1]

    def get_product_list(self):
        """Return products list."""
        return self.products

    def get_recipient_list(self):
        """Return recipients list."""
        return self.recipients

    def parse_wishlist_into_products_and_recipients(self):
        """Parse the wishlist that was given in the constructor into the products and recipients list respectively."""
        for pair in self.wishlist.get_wishes().items():
            if pair[0] not in self.recipients.keys():
                self.recipients[pair[0]] = {}
            for product in pair[1]:
                parse = self.parse_product_info(self.get_product_info(product))
                self.recipients[pair[0]][parse[0]] = parse[1]

        for pair in self.recipients.items():
            for product in pair[1].items():
                if product[0] not in self.products.keys():
                    self.add_parsed_product_info(product)
                else:
                    if "Count" not in self.products[product[0]].keys():
                        self.products[product[0]]["Count"] = 2
                    else:
                        self.products[product[0]]["Count"] += 1


if __name__ == '__main__':
    wishes = Wishlist("ex15_wish_list.csv")
    nice_and_naughty = NiceAndNaughtyList("ex15_nice_list.csv", "ex15_naughty_list.csv")
    pas = ProductionAndStock("https://cs.ttu.ee/services/xmas/gift?name=", nice_and_naughty, wishes)
    print(pas.get_product_info("swimming flippers"))
    pas.add_parsed_product_info(
        pas.parse_product_info(
            pas.get_product_info("swimming flippers")))
    print(pas.get_product_list())
    pas.parse_wishlist_into_products_and_recipients()
    print(pas.get_product_list())
    print(pas.get_recipient_list())

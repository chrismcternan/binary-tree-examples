# file name: stock-binary-search-tree.pt
# author: Chris McTernan
#
# Parses S&P 500 data into a binary search tree and outputs based on a search
import csv
import time


# Creates a class to store stock data in bins
class StockData:
    def __init__(self, ticker: str, name: str, sector: str) -> None:
        self.ticker = ticker
        self.name = name
        self.sector = sector

    def print_data(self):
        print('Stock Ticker: ' + self.ticker)
        print('Company Name: ' + self.name)
        print('Sector: ' + self.sector)


class CompanyNameTree:
    def __init__(self, key: str, data: StockData) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.data = data

    # defines a function to search for a key and returns object StockData
    def search(self, key: str) -> StockData:
        if self.key == key:
            return self.data

        if key < self.key:
            if self.left:
                return self.left.search(key=key)
            else:
                print('No object found at key')
                return None
        elif key > self.key:
            if self.right:
                return self.right.search(key=key)
            else:
                print('No object found at key')
                return None

    # defines function for printing tree in-order (left, root, right)
    def print_inorder(self) -> None:
        if self.left is not None:
            self.left.print_inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.print_inorder()

    def print_preorder(self) -> None:
        print(self.key, end=' ')
        if self.left is not None:
            self.left.print_preorder()
        if self.right is not None:
            self.right.print_preorder()

    def print_postorder(self) -> None:
        if self.left is not None:
            self.left.print_postorder()
        if self.right is not None:
            self.right.print_postorder()
        print(self.key, end=' ')

    # defines function that returns true or false based on input
    def high_low(self, value: str) -> bool:
        if value < self.key:
            return False
        elif value > self.key:
            return True

    # defines function to insert values into tree based on high/low
    def insert(self, key: str, data: StockData) -> None:
        # if empty, adds key to root node
        if self.key is None:
            self.key = key
        # if value returns low, then branch left
        elif not self.high_low(key):
            # adds recursive tree if value does not exist at left branch
            if self.left is None:
                self.left = CompanyNameTree(key=key, data=data)
            else:
                self.left.insert(key=key, data=data)
        # if value returns high, then branch right
        elif self.high_low(key):
            # adds recursive tree if value does not exist at right branch
            if self.right is None:
                self.right = CompanyNameTree(key=key, data=data)
            else:
                self.right.insert(key=key, data=data)


# Creates a class tp store stock data by sector in a tree
class SectorSearchTree:
    """
        Stores stock data by Sector. Each node stores a sector which contains a list of the company
        stock. When searching by sectors, the list is returned and the data is found in CompanyNameTree
    """
    def __init__(self, sector_key: str) -> None:
        self.key = sector_key
        self.left = None
        self.right = None
        self.ticker_list = []

    # searches for sector name if it already exists in tree, points to the node
    def find_sector(self, sector: str) -> object:
        if self.key == sector:
            return self
        elif self.key < sector:
            if self.left:
                return self.left.find_sector(sector=sector)
            else:
                self.left = SectorSearchTree(sector_key=sector)
                return self.left
        elif self.key > sector:
            if self.right:
                return self.right.find_sector(sector=sector)
            else:
                self.right = SectorSearchTree(sector_key=sector)
                return self.right

    # defines function that takes sector node and appends to name_list
    def add_company(self, sector: str, company_index: str) -> None:
        sector_node = self.find_sector(sector=sector)
        sector_node.ticker_list.append(company_index)

    def print_sector(self, sector: str):
        sector_node = self.find_sector(sector=sector)
        ticker_list = sector_node.ticker_list
        for index in ticker_list:
            row_data = node.search(index)
            row_data.print_data()


# Initializes the tree with empty node
node = CompanyNameTree(key='', data=StockData(ticker='',name='',sector=''))
sector_root = SectorSearchTree(sector_key='')
with open('stock_data.csv', newline='') as f:
    csv_data = csv.reader(f, delimiter=',')
    ticker_arr = []
    for row in csv_data:
        node.insert(key=row[0], data=StockData(ticker=row[0], name=row[1], sector=row[2]))
        sector_root.add_company(sector=row[2], company_index=row[0])
        ticker_arr.append(row)

# node.print_inorder()
# print('\n')

# search for Company data with ticker
# stock_ticker = 'DDD'
# # records search time
# company_search_time = time.time()
# # find and print data in BST
# stock_data = node.search(stock_ticker)
# if stock_data:
#     stock_data.print_data()
# print("---%s seconds ---" % (time.time() - company_search_time))

search_time_start = time.time()
sector_search = 'Health Care'
sector_root.print_sector(sector_search)
binary_sector_search_time = time.time() - search_time_start

search_time_start = time.time()
for row in ticker_arr:
    if row[2] == 'Health Care':
        print('Stock Ticker: ' + row[0])
        print('Company Name: ' + row[1])
        print('Sector: ' + row[2])
loop_sector_search_time = time.time() - search_time_start
print("Sector Search using Binary Trees Indexing:")
print("---%s seconds ---" % binary_sector_search_time)
print("Sector Search using iteration")
print("---%s seconds ---" % loop_sector_search_time)


# loop_search_time = time.time()
# for row in ticker_arr:
#     if row[0] == 'ZTS':
#         print('Stock Ticker: ' + row[0])
#         print('Company Name: ' + row[1])
#         print('Sector: ' + row[2])
# print("---%s seconds ---" % (time.time() - loop_search_time))

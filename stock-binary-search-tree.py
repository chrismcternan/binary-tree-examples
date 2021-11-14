# file name: stock-binary-search-tree.pt
# author: Chris McTernan
#
# Parses S&P 500 data into a binary search tree and outputs based on a search
import csv
import time


class StockData:
    def __init__(self, ticker: str, name: str, sector: str) -> None:
        self.ticker = ticker
        self.name = name
        self.sector = sector

    def print_data(self):
        print('Stock Ticker: ' + self.ticker)
        print('Company Name: ' + self.name)
        print('Sector: ' + self.sector)


class BinarySearchTree:
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
                self.left = BinarySearchTree(key=key, data=data)
            else:
                self.left.insert(key=key, data=data)
        # if value returns high, then branch right
        elif self.high_low(key):
            # adds recursive tree if value does not exist at right branch
            if self.right is None:
                self.right = BinarySearchTree(key=key, data=data)
            else:
                self.right.insert(key=key, data=data)


node = BinarySearchTree(key=None, data=None)
with open('constituents_csv.csv', newline='') as f:
    csv_data = csv.reader(f, delimiter=',')
    ticker_arr = []
    for row in csv_data:
        node.insert(key=row[0], data=StockData(ticker=row[0], name=row[1], sector=row[2]))
        ticker_arr.append(row)

# node.print_inorder()
# print('\n')

# search for Company data with ticker
stock_ticker = 'DDD'
# records search time
BST_search_time = time.time()
# find and print data in BST
stock_data = node.search(stock_ticker)
if stock_data:
    stock_data.print_data()
print("---%s seconds ---" % (time.time() - BST_search_time))

# loop_search_time = time.time()
# for row in ticker_arr:
#     if row[0] == 'ZTS':
#         print('Stock Ticker: ' + row[0])
#         print('Company Name: ' + row[1])
#         print('Sector: ' + row[2])
# print("---%s seconds ---" % (time.time() - loop_search_time))

class PageUtil:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = self.calculate_total_pages()

    def calculate_total_pages(self):
        return (self.total_items + self.page_size - 1) // self.page_size

    def get_page(self, page_number):
        if not self.is_valid_page_number(page_number):
            return []

        start_index, end_index = self.calculate_indices(page_number)
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        if not self.is_valid_page_number(page_number):
            return {}

        start_index, end_index = self.calculate_indices(page_number)
        page_data = self.data[start_index:end_index]

        return self.create_page_info(page_number, page_data)

    def is_valid_page_number(self, page_number):
        return 1 <= page_number <= self.total_pages

    def calculate_indices(self, page_number):
        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, self.total_items)
        return start_index, end_index

    def create_page_info(self, page_number, page_data):
        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": page_number > 1,
            "has_next": page_number < self.total_pages,
            "data": page_data
        }

    def search(self, keyword):
        results = self.filter_data_by_keyword(keyword)
        num_results = len(results)
        num_pages = (num_results + self.page_size - 1) // self.page_size

        return self.create_search_info(keyword, num_results, num_pages, results)

    def filter_data_by_keyword(self, keyword):
        return [item for item in self.data if keyword in str(item)]

    def create_search_info(self, keyword, num_results, num_pages, results):
        return {
            "keyword": keyword,
            "total_results": num_results,
            "total_pages": num_pages,
            "results": results
        }
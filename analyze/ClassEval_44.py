import re
import string
import gensim
from bs4 import BeautifulSoup


class HtmlUtil:

    def __init__(self):
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def __format_line_feed(text):
        return re.sub(re.compile(r'\n+'), '\n', text)

    def format_line_html_text(self, html_text):
        if not html_text:
            return ''
        soup = BeautifulSoup(html_text, 'lxml')

        self._replace_code_tags(soup)
        self._format_list_items(soup)
        self._format_paragraphs(soup)

        clean_text = gensim.utils.decode_htmlentities(soup.get_text())
        return self.__format_line_feed(clean_text)

    def _replace_code_tags(self, soup):
        code_tags = soup.find_all(name=['pre', 'blockquote'])
        for tag in code_tags:
            tag.string = self.CODE_MARK

    def _format_list_items(self, soup):
        ul_ol_group = soup.find_all(name=['ul', 'ol'])
        for ul_ol_item in ul_ol_group:
            li_group = ul_ol_item.find_all('li')
            for li_item in li_group:
                li_item_text = li_item.get_text().strip()
                if li_item_text:
                    li_item.string = self._format_list_item_text(li_item_text)

    def _format_list_item_text(self, li_item_text):
        if li_item_text[-1] in string.punctuation:
            return '[{0}]{1}'.format('-', li_item_text)
        return '[{0}]{1}.'.format('-', li_item_text)

    def _format_paragraphs(self, soup):
        p_group = soup.find_all(name=['p'])
        for p_item in p_group:
            p_item_text = p_item.get_text().strip()
            if p_item_text:
                p_item.string = self._format_paragraph_text(p_item, p_item_text)

    def _format_paragraph_text(self, p_item, p_item_text):
        if p_item_text[-1] in string.punctuation:
            return p_item_text
        next_sibling = p_item.find_next_sibling()
        if next_sibling and self.CODE_MARK in next_sibling.get_text():
            return p_item_text + ':'
        return p_item_text + '.'

    def extract_code_from_html_text(self, html_text):
        text_with_code_tag = self.format_line_html_text(html_text)

        if self.CODE_MARK not in text_with_code_tag:
            return []

        return self._get_code_list(html_text, text_with_code_tag)

    def _get_code_list(self, html_text, text_with_code_tag):
        soup = BeautifulSoup(html_text, 'lxml')
        code_tags = soup.find_all(name=['pre', 'blockquote'])
        code_count = text_with_code_tag.count(self.CODE_MARK)
        return [code_tags[i].get_text() for i in range(code_count) if code_tags[i].get_text()]
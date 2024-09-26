from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
  page_size=10
  page_query_param='p'#change the word that you write in search at the time of search any page default you write page and change according to you
  page_size_query_param='records'#decided by client that he is how many content see in webpage
  max_page_size=7
  last_page_strings='end'
 
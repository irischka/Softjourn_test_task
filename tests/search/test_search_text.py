from page_object.pages.search_page import SearchPage
from data_user.data_user import SearchValue

"""TC001"""


def test_search_text(browser):
    search_page = SearchPage(browser)

    "Preconditions: Navigate to the Google Page"
    search_page.navigate_to_page()

    "Step: Enter the text 'Selenium' in the Search field and click the Search button"
    results = search_page \
        .set_search_field(SearchValue.SELENIUM_TEXT.value) \
        .search_field_submit() \
        .find_elements(search_page.RESULT_TEXT)

    "Expected: Verify that the 'Selenium' text is displayed in each results"

    print("\nResult of search is:")
    print(len(results))

    assert all([search_page.SELENIUM_TEXT in result.text for result in results]), \
        "The text is not displayed in each results"

    "Expected: Verify that the key worlds 'Selenium' is bolt"
    bolt_text = search_page.find_elements(search_page.BOLT_TEXT)

    assert all([result.value_of_css_property("font-weight") >= "700" or "bolt" for result in bolt_text]), \
        "The key worlds are not bolt"

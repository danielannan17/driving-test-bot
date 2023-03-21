def get_date_of_week(date_str, day_of_week_str):
    # Parse the input date string into a datetime object
    date = datetime.datetime.strptime(date_str, '%dth %b %Y').date()
    
    # Convert the day of the week string to an integer (0 = Monday, 1 = Tuesday, etc.)
    day_of_week = datetime.datetime.strptime(day_of_week_str, '%A').weekday()
    
    # Compute the target day of the week (0 = Monday, 1 = Tuesday, etc.)
    target_day = (day_of_week - date.weekday()) % 7
    
    # Compute the delta from the input date to the target day of the week
    delta = datetime.timedelta(days=target_day)
    
    # Compute the date of the target day of the week in the same week as the input date
    target_date = date + delta
    
    return target_date

def get_start_date(string):
    date_str = string.split("between ")[1].split(" – ")[0]
    # start_date = datetime.datetime.strptime(date_str, "%dth %b %Y").date()
    return date_str


def get_unique_xpath(tag: Tag) -> str:
    """
    Given a BeautifulSoup Tag object, returns a unique XPath expression
    that can be used as a locator in Playwright.
    """
    if not tag.name:
        return ''

    # Initialize the XPath expression with the tag name
    xpath = tag.name

    # Add indices to the XPath expression until it's unique
    while tag.parent:
        parent = tag.parent
        siblings = parent.find_all(tag.name, recursive=False)

        if len(siblings) > 1:
            index = siblings.index(tag) + 1
            xpath = f"{tag.name}[{index}]/" + xpath
        else:
            xpath = f"{tag.name}/" + xpath

        tag = parent

    return '/' + xpath
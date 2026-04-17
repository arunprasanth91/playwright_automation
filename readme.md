1. Playwright powerful automation tool for web automation and API automation
2. Multi language support
3. Multi Browser and OS compatibility 
4. Record & Playback facility
5. Auto waiting mechanism, avoiding manual wait commands
6. Inbuilt logging and screenshot tools. 

pytest --headed = To run in headed mode. 

Different locators:
1. page.get_by_label
2. page.get_by_role
3. page.get_by_placeHolder
4. page.locator
5. page.locator().filter()

when to use page.get_by_label() method to identify web element:
    1. Either input tag should be enclosed by label tag
        <label for="username" class="text-white">Username: <input type="text" name="username" id="username" class="form-control"> </label>
    2. Or, label tag (for="username") and input tag id (id="username") attribute should have a mapping like above. 


CSS Locator 

tag[attribute=value]
ID = #idvalue
class = .classvalue

wildcards
contains = tag[attribute*=value]
starts with = tag[attribute^=value]
ends with = tag[attribute$=value]


Xpath 

//tag[@attribute=value]
wildcards:
starts with = //tag[starts-with(@attribute, value)]
ends with = //tag[ends-with(@attribute, value)]
contains = //tag[contains(@attribute,value)]
contains text = //tagname[contains(text(), 'substring')]
Siblings:
Parent sibling = //tag[@attribute=value]/parent-sibling::td
following sibling = //tag[@attribute=value]/following-sibling::tr
preceding sibling = //tag[@attribute=value]/preceding-sibling::tr

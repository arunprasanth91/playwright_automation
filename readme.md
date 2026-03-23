1. Playwright powerful automation tool for web automation and API automation
2. Multi language support
3. Multi Browser and OS compatibility 
4. Auto waiting mechanism, avoiding manual wait commands
5. Inbuilt logging and screenshot tools. 

pytest --headed = To run in headed mode. 


when to use page.get_by_label() method to identify web element:
    1. Either input tag should be enclosed by label tag
        <label for="username" class="text-white">Username: <input type="text" name="username" id="username" class="form-control"> </label>
    2. Or, label tag (for="username") and input tag id (id="username") attribute should have a mapping like above. 
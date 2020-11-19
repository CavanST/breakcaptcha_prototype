BrowserEngine browser = BrowserFactory.getWebKit();
Page page = browser.navigate("https://google.com/recaptcha/api2/demo");
page.show();


try (final WebClient webClient = new WebClient()) {
    final HtmlPage page = webClient.getPage("https://google.com/recaptcha/api2/demo");
    HtmlElement recaptcha = (HtmlElement) page.getFirstByXPath("//iframe");
}


WebDriver driver = new ChromeDriver(options);
driver.get("https://google.com/recaptcha/api2/demo");
By xpath = By.xpath("//iframe");
WebElement recaptcha = driver.findElements(xpath).get(0);
Point location = recaptcha.getLocation();
Actions actions = new Actions(driver);
actions.moveByOffset(location.getX(), location.getY()).perform();
actions.moveToElement(recaptcha).click().perform();

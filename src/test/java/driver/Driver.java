package driver;

import com.thoughtworks.gauge.AfterSuite;
import com.thoughtworks.gauge.BeforeSuite;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Driver {

    public static WebDriver webDriver;
    public static WebDriverWait webDriverWait;

    @BeforeSuite
    public void initializeDriver(){
        webDriver = DriverFactory.getDriver();
    }

    @AfterSuite
    public void closeDriver(){
        webDriver.quit();
    }
    
}

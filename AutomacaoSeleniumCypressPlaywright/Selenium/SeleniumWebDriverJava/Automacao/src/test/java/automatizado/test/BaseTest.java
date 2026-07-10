package automatizado.test;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import automatizado.page.CursoSeleniumPO;

public abstract class BaseTest {

    public static WebDriver driver;
    public static CursoSeleniumPO dsl;

    @BeforeClass
    public static void inicializar(){
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        dsl = new CursoSeleniumPO(driver);
    }

    @AfterClass
    public static void finalizar(){
        driver.quit();
    }
}
package automatizado.page;
import java.time.Duration;

import org.junit.Assert;
import static org.junit.Assert.assertEquals;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public abstract class BasePO {
    
    /**Driver base que será usado pelas pages**/
    public WebDriver driver;
    public final WebDriverWait wait;

    /**
     * Construtor base para criação da fábrica de elementos (PageFactory).
     * @param driver Driver da página atual.
     */
    public BasePO(WebDriver driver){
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        PageFactory.initElements(driver, this);
    }

    /**
     * Obtém o título da página e imprime no console
     * 
     * @return
     */
    public String ObterTituloPagina(String tituloEsperado) {
        String titulo = driver.getTitle();
        assertEquals(tituloEsperado, titulo);
        assert titulo != null : "O título da página é nulo.";
        System.out.println("Título da página: " + titulo);
        return titulo;
    }

    /**
     * Imprime o nome do WebElement no console
     * 
     * @param elemento
     */
    public void systemResult(String elemento) {
        System.out.println("Texto do Elemento: " + elemento);
    }

    /**
     * Imprime o nome do WebElement dentro de um frame no console
     * 
     * @param frame
     * @param elemento
     */
    public void systemResultFrame(WebElement frame, WebElement elemento) {
        driver.switchTo().frame(frame);
        System.out.println("Elemento: " + elemento.getAccessibleName());
    }

    /**
     * Aguarda até que o elemento seja visível na página
     * 
     * @param elemento
     */
    public void aguardarElementoComTexto(WebElement elemento) {
        wait.until(ExpectedConditions.visibilityOf(elemento));
        wait.until(ExpectedConditions.elementToBeClickable(elemento));
        wait.until(d -> !elemento.getText().trim().isEmpty());
    }

    /**
     * Aguarda até que o elemento seja visível na página e, em seguida, clica nele
     * 
     * @param elemento
     */
    public void delayClick(WebElement elemento) {
        wait.until(ExpectedConditions.elementToBeClickable(elemento));
        elemento.isDisplayed();
        elemento.isEnabled();
        elemento.click();
    }

    public boolean esperarSumirElemento(WebElement elemento) {
        return wait.until(
                ExpectedConditions.invisibilityOf(elemento));
    }

    public void retornarTelaPrincial() {
        String janelaPrincipal = driver.getWindowHandle();
        driver.switchTo().window(janelaPrincipal);
    }

    public void linhaVisivelTela(WebElement elemento) {
        @SuppressWarnings("unused")
        boolean resultado;
        try {
            aguardarElementoComTexto(elemento);
            resultado = elemento.isDisplayed();
        } catch (Exception e) {
            resultado = false;
        }
    }

    public void escrever(WebElement elemento, String texto){
        elemento.clear();
        elemento.sendKeys(texto);
        Assert.assertEquals(elemento.getAttribute("value"), texto);
    }

    public void validarElemento(WebElement elemento){
        elemento.isDisplayed();
        elemento.isEnabled();
    }

    public void esperarAlert(){
        new WebDriverWait(driver, Duration.ofSeconds(5)).until(ExpectedConditions.alertIsPresent());
    }

    public void esperarInput(WebElement elemento){
        new WebDriverWait(driver, Duration.ofSeconds(5)).until(ExpectedConditions.visibilityOf(elemento));
    }
}

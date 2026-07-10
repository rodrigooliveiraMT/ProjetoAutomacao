package automacaoSelenium.page;

import static org.junit.Assert.assertTrue;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ProjetoParticularPO extends BasePO {

    @FindBy(id = "elementosForm:nome")
    public WebElement campoNome;

    @FindBy(id = "elementosForm:sobrenome")
    public WebElement campoSobrenome;

    @FindBy(id = "elementosForm:sexo:0")
    public WebElement campoSexoMasculino;

    @FindBy(id = "elementosForm:sexo:1")
    public WebElement campoSexoFeminino;

    @FindBy(id = "elementosForm:comidaFavorita:0")
    public WebElement campoComidaCarne;

    @FindBy(id = "elementosForm:comidaFavorita:1")
    public WebElement campoComidaFrango;

    @FindBy(id = "elementosForm:comidaFavorita:2")
    public WebElement campoComidaPeixe;

    @FindBy(id = "elementosForm:comidaFavorita:3")
    public WebElement campoComidaVegetariano;

    @FindBy(id = "elementosForm:escolaridade")
    public WebElement campoEscolaridade;

    @FindBy(id = "elementosForm:esportes")
    public WebElement campoEsportes;

    @FindBy(id = "elementosForm:sugestoes")
    public WebElement campoSugestoes;

    @FindBy(id = "elementosForm:cadastrar")
    public WebElement botaoCadastrar;

    @FindBy(id = "alert")
    public WebElement systemResult;

    @FindBy(id = "confirm")
    public WebElement systemResultConfirm;

    @FindBy(id = "prompt")
    public WebElement systemResultPrompt;

    @FindBy(id = "buttonSimple")
    public WebElement buttonSimple;

    @FindBy(id = "buttonPopUpEasy")
    public WebElement buttonPopUpEasy;

    @FindBy(tagName = "textarea")
    public WebElement insetTextArea;

    @FindBy(id = "buttonPopUpHard")
    public WebElement buttonPopUpHard;

    @FindBy(id = "buttonDelay")
    public WebElement buttonDelay;

    @FindBy(id = "novoCampo")
    public WebElement insertNovoCampo;

    @FindBy(id = "frameButton")
    public WebElement buttonFrame;

    @FindBy(id = "frame1")
    public WebElement frame1;

    @FindBy(css = "html>body>center>a")
    public WebElement linkVoltar;

    @FindBy(id = "resultado")
    public WebElement resultado;

    public ProjetoParticularPO(WebDriver driver) {
        super(driver);
    }

    public void validarRadioButtonCheckbox(WebElement elemento) {
        if (elemento.isDisplayed() == true && elemento.isEnabled() == true) {
            assertTrue("O elemento (" + elemento.getAccessibleName() + ") está visível!", elemento.isDisplayed());
            assertTrue("O elemento (" + elemento.getAccessibleName() + ") está habilitado!", elemento.isEnabled());
            elemento.click();
            assertTrue(elemento.isSelected());
            systemResult(elemento.getAccessibleName());
        } else {
            System.out.println("Erro ao clicar no elemento >>>" + elemento.getAccessibleName()
                    + "\nO elemento não está visível ou habilitado!");
        }
    }

}

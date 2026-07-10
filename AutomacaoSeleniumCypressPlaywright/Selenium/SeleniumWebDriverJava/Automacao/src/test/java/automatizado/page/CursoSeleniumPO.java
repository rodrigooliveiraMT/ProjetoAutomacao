package automatizado.page;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class CursoSeleniumPO extends BasePO {

    @FindBy(id = "elementosForm:nome")
    public WebElement inputNome;

    @FindBy(id = "elementosForm:sobrenome")
    public WebElement inputSobreNome;

    @FindBy(id = "elementosForm:sexo:0")
    public WebElement radioButtonMasculino;

    @FindBy(id = "elementosForm:comidaFavorita:0")
    public WebElement radioButtonComida;

    @FindBy(id = "elementosForm:escolaridade")
    public WebElement selecioneEscolaridade;

    @FindBy(id = "elementosForm:esportes")
    public WebElement selecioneEsportes;

    @FindBy(id = "elementosForm:sugestoes")
    public WebElement inputSugestoes;

    @FindBy(css = "body>center>a")
    public WebElement linkVoltar;

    @FindBy(id = "resultado")
    public WebElement resultadoLinkVoltar;

    @FindBy(id = "alert")
    public WebElement alerta;

    @FindBy(id = "confirm")
    public WebElement confirmar;

    @FindBy(id = "prompt")
    public WebElement prompt;

    @FindBy(id = "buttonSimple")
    public WebElement buttonCliqueMe;

    @FindBy(id = "buttonPopUpEasy")
    public WebElement abrirPopupComIdentificao;

    @FindBy(css = "html>body>textarea")
    public WebElement inputTextarea;

    @FindBy(id = "buttonPopUpHard")
    public WebElement abrirPopupSemIdentificao;

    @FindBy(id = "buttonDelay")
    public WebElement inputComDalay;

    @FindBy(id = "novoCampo")
    public WebElement inputCampoNovo;

    @FindBy(id = "frame1")
    public WebElement validarFrame;

    @FindBy(id = "frameButton")
    public WebElement buttonFrame;

    @FindBy(css = "body>center>div>span")
    public WebElement resultadoDoCadastro;

    @FindBy(id = "descNome")
    public WebElement resultadoNome;

    @FindBy(id = "descSobrenome")
    public WebElement resultadoSobreNome;

    @FindBy(id = "descSexo")
    public WebElement resultadoSexo;

    @FindBy(id = "descComida")
    public WebElement resultadoComida;

    @FindBy(id = "descEscolaridade")
    public WebElement resultadoEscolaridade;

    @FindBy(id = "descEsportes")
    public WebElement resultadoEsportes;

    @FindBy(id = "descSugestoes")
    public WebElement resultadoSugestoes;

    @FindBy(id = "elementosForm:cadastrar")
    public WebElement buttonCadastrar;

    public CursoSeleniumPO(WebDriver driver) {
        super(driver);
    }
       
}

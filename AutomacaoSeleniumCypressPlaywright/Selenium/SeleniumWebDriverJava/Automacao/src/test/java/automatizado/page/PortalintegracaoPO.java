package automacaoSelenium.page;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class PortalintegracaoPO extends BasePO {

    @FindBy(id = "btnAcessar")
    public WebElement buttonAcessar;

    @FindBy(id = "txtCpfAcesso")
    public WebElement inputLogin;

    @FindBy(id = "txtSenhaAcesso")
    public WebElement inputSenha;

    @FindBy(id = "btnAcessar")
    public WebElement botaoAcessar;

    @FindBy(xpath = "//span[text()='Login ou Senha incorretos!']")
    public WebElement alertTituloInformarCredenciais;

    @FindBy(id = "lblMsgErro")
    public WebElement alertMensagemInformarCredenciais;

    @FindBy(id = "lnkFechar")
    public WebElement buttonFecharInformarCredenciais;

    @FindBy(id = "lnkbtSolicitaSenha")
    public WebElement buttonCliqueAqui;

    @FindBy(xpath = "//span[text()='Como solicitar sua senha']")
    public WebElement alertTituloCadastro;

    @FindBy(id = "lbMensagemSolicitaSenha")
    public WebElement alertMensagemCadastro;

    @FindBy(id = "lnkFecharSolicita")
    public WebElement buttonFecharAlertaCadastro;

    public PortalintegracaoPO(WebDriver driver) {
        super(driver);
    }

    public void efetuarLogin() {
        inputLogin.sendKeys("cqs.rodrigocosta");
        inputSenha.sendKeys("123");
        buttonAcessar.click();
    }

}

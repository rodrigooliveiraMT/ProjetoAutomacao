package automacaoSelenium.page;

import static org.junit.Assert.assertEquals;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class AcessoPericiaMedicaPO extends BasePO {

    @FindBy(className = "toast-message")
    public WebElement mensagemErro;

    @FindBy(className = "toast-title")
    public WebElement tituloErro;

    @FindBy(className = "logo-name")
    public WebElement validarTituloLogin;

    @FindBy(id = "txtLogin")
    public WebElement campoUsuario;

    @FindBy(id = "txtSenha")
    public WebElement campoSenha;

    @FindBy(id = "btnLogin")
    public WebElement botaoLogin;

    @FindBy(xpath = "//h3[contains(text(),'Perícia Médica')]")
    public WebElement tituloTelaInicial;

    @FindBy(xpath = "//p[contains(text(),'Configurações')]")
    public WebElement acessarModuloConfiguracoes;

    @FindBy(xpath = "//a[contains(text(),'Parâmetros do Sistema')]")
    public WebElement acessarParametrosSistema;

    @FindBy(xpath = "//a[@href='#tab1']")
    public WebElement validarAbaParametros;

    /**
     * Elementos relacionados ao módulo de Cadastros > Usuários, que ainda não foram
     * utilizados nos testes, mas podem ser úteis para futuras implementações.
     */

    @FindBy(id = "ContentPlaceHolder1_btnSalvar")
    public WebElement botaoSalvar;

    @FindBy(id = "ContentPlaceHolder1_btnFechar")
    public WebElement botaoCancelar;

    @FindBy(className = "toast-message")
    public WebElement mensagemSucesso;

    @FindBy(className = "toast-title")
    public WebElement tituloSucesso;

    @FindBy(xpath = "//div[@class='formErrorContent']")
    public WebElement validarObrigatorioCampoNome;

    @FindBy(xpath = "//p[contains(text(),'Cadastros')]")
    public WebElement ModuloCadastros;

    @FindBy(xpath = "//a[contains(text(),'Cadastro de Usuários')]")
    public WebElement MenuCadastroUsuarios;

    @FindBy(className = "breadcrumb")
    public WebElement validarTelaCadastroUsuarios;

    @FindBy(xpath = "//a[@href='#tab1']")
    public WebElement clickAbaUsuarios;

    @FindBy(xpath = "//a[@href='#tab2']")
    public WebElement clickAbaPermissaoCentralRelatorio;

    @FindBy(id = "btnNovo")
    public WebElement botaoNovoCadastroUsuario;

    @FindBy(id = "ContentPlaceHolder1_txt_USR_LOGIN_NOME_PERITO")
    public WebElement inputCampoNomePerito;

    @FindBy(id = "ContentPlaceHolder1_txt_USR_LOGIN_LOGIN")
    public WebElement inputCampoLogin;

    @FindBy(id = "ContentPlaceHolder1_ddl_USR_LOGIN_GRUPO_PERMISSAO_PERICIA_ID")
    public WebElement selecionarGrupoPermissao;

    @FindBy(id = "ContentPlaceHolder1_txt_USR_LOGIN_HASH")
    public WebElement inputCampoHash;

    @FindBy(id = "ContentPlaceHolder1_txt_USR_LOGIN_HASH_CONF")
    public WebElement inputCampoHashConfirmacao;

    @FindBy(id = "ContentPlaceHolder1_txt_USR_LOGIN_CPF")
    public WebElement inputCampoCPF;

    @FindBy(xpath = "//input[@aria-controls='grdResultados']")
    public WebElement inputCampoPesquisarUsuario;

    @FindBy(xpath = "//table/tbody/tr[1]")
    public WebElement linhaUsuario;

    // Cadastrar (Grupo - Permissões)
    @FindBy(xpath = "//a[@href='GrupoPermissoes.aspx']")
    public WebElement acessarMenuGrupoPermissoes;

    @FindBy(xpath = "//b[text()='Grupos - Permissões']")
    public WebElement validarTelaGrupoPermissoes;

    @FindBy(id = "btnNovo")
    public WebElement botaoNovoCadastroGrupoPermissao;

    @FindBy(id = "modalcadastronome1")
    public WebElement tituloModalGrupoPermissao;

    @FindBy(id = "ContentPlaceHolder1_txtNomeGrupo")
    public WebElement inputCampoNomeGrupo;

    @FindBy(id = "btnSalvarDocumento")
    public WebElement botaoSalvarGrupoPermissao;

    @FindBy(id = "btnFecharModalDrop")
    public WebElement botaoFecharGrupoPermissao;

    @FindBy(xpath = "//td[text()='Automação']")
    public WebElement linhaGrupoPermissao;

    @FindBy(className = "fa")
    public WebElement iconePermissao;

    @FindBy(xpath = "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_perm')]")
    public WebElement botaoEditarPermissao;

    @FindBy(xpath = "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_remove')]")
    public WebElement botaoExcluirPermissao;

    @FindBy(xpath = "//h4[normalize-space()='Permissões']")
    public WebElement tituloModalPermissoes;

    @FindBy(id = "uniform-ContentPlaceHolder1_CheckBox1")
    public WebElement checkboxPermissao;

    @FindBy(xpath = "//i[contains(@class,'glyphicon-floppy-saved')]")
    public WebElement botaoSalvarPermissoes;

    @FindBy(xpath = "//a[@href='Inicial.aspx']")
    public WebElement ModuloPericiasAgendadas;

    public AcessoPericiaMedicaPO(WebDriver driver) {
        super(driver);
    }

    public void efeturarLogin() {
        campoUsuario.sendKeys("1340");
        campoSenha.sendKeys("fgh38a");
        botaoLogin.click();
    }

    public void validarTexto(WebElement elemento, String textoEsperado) {
        String texto = elemento.getText();
        assertEquals(textoEsperado, texto);
        System.out.println("Texto do elemento: " + texto);

    }
}

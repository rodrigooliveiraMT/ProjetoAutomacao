package automatizado.test;

import static org.junit.Assert.assertEquals;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

import automatizado.page.PortalintegracaoPO;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class PortalIntegracaoTest extends BaseTest {

    public static PortalintegracaoPO dsl;

    public static final String URL_BASE = "https://proxima2.sisprevweb.com.br/estado_01/integracao/Login/Login.aspx";

    @BeforeClass
    public static void abrirPagina() {
        dsl = new PortalintegracaoPO(driver);
        driver.get(URL_BASE);
    }

    @Test
    public void TC001_validarTitulo() {
        dsl.ObterTituloPagina("Portal Integração");
    }

    @Test
    public void TC002_validarAcesso() {
        dsl.buttonAcessar.click();
        dsl.aguardarElementoComTexto(dsl.alertTituloInformarCredenciais);
        assertEquals("Login ou Senha incorretos!", dsl.alertTituloInformarCredenciais.getText());
        assertEquals("Favor verifique as informações digitadas e tente novamente.",
                dsl.alertMensagemInformarCredenciais.getText());
        dsl.buttonFecharInformarCredenciais.click();
    }

    @Test
    public void TC003_validarCadastro() {
        dsl.buttonCliqueAqui.click();
        dsl.aguardarElementoComTexto(dsl.alertTituloCadastro);
        assertEquals("Como solicitar sua senha", dsl.alertTituloCadastro.getText());
        assertEquals("Entre em contato com o Instituto para receber seus dados de acesso.",
                dsl.alertMensagemCadastro.getText());
        dsl.buttonFecharAlertaCadastro.click();
    }

    @Test
    public void TC004_validarLogin() {
        dsl.efetuarLogin();
    }

}

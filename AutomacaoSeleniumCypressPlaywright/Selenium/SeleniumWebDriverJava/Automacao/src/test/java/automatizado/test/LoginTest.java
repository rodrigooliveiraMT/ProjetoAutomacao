package automatizado.test;

import static org.junit.Assert.assertEquals;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

import automatizado.page.LoginPO;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class LoginTest extends BaseTest {

    public static LoginPO loginPage;

    @BeforeClass
    public static void prepararTestes(){
        loginPage = new LoginPO(driver);
    }

    @Test
    public void TC001_NaoDeveLogarComSenhaEmBrancoVazio(){
        // Validar acesso sem informar o email e senha!!!

        loginPage.executarAcaoDeLogar("", "");
        String mensagem = loginPage.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC002_DeveMostrarMensagemDeErroQuandoEmailPreenchidoESenhaVazia(){
        // Validar acesso sem informar a senha!!!

        loginPage.executarAcaoDeLogar("teste", "");
        String mensagem = loginPage.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC003_DeveMostrarMensagemDeErroQuandoEmailVazioESenhaIncorreta(){
        // Validar acesso sem informar o email!!!

        loginPage.executarAcaoDeLogar("", "teste");
        String mensagem = loginPage.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC004_ValidarEmailSenhaAmbosInvalidos(){
        // Validar acesso com email e senha inválidos!!!

        loginPage.executarAcaoDeLogar("teste", "teste");
        String mensagem = loginPage.obterMenssagem();

        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC005_ValidarEmailSenhaSenhaInvalido(){
        // Validar acesso com senha inválido!!!
    
        loginPage.executarAcaoDeLogar("admin@admin.com", "teste");
        String mensagem = loginPage.obterMenssagem();
    
        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC006_ValidarEmailSenhaEmailInvalido(){
        // Validar acesso com email inválido!!!

        loginPage.executarAcaoDeLogar("Aadmin@admin.com", "admin@123");
        String mensagem = loginPage.obterMenssagem();

        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC007_ValidarEmailSenhaAmbosValidos(){
        // Validar acesso com email e senha válidos!!!

        loginPage.executarAcaoDeLogar("admin@admin.com", "admin@123");
       assertEquals(loginPage.obterTituloPagina(), "Controle de Produtos");
    }
}

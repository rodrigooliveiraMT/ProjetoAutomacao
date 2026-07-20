package automatizado.test;

import static org.junit.Assert.assertEquals;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

import automatizado.builder.ProdutoBuilder;
import automatizado.page.ControleDeProdutoPO;
import automatizado.resource.CadastroProdutoUrl;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class ControDeProdutoTest extends BaseTest {
    
    public static ControleDeProdutoPO dsl;
    public static CadastroProdutoUrl cadastroProdutoUrl;

    @BeforeClass
    public static void abrirPagina(){
        dsl = new ControleDeProdutoPO(driver);
        driver.get(CadastroProdutoUrl.URL_BASE);
        //dsl.executarAcaoDeLogar("admin@admin.com", "admin@123");
    }

    @Test
    public void TC001_validarTitulo(){
        dsl.ObterTituloPagina("Login");
    }

        @Test
    public void TC002_NaoDeveLogarComSenhaEmBrancoVazio(){
        // Validar acesso sem informar o email e senha!!!

        dsl.executarAcaoDeLogar("", "");
        String mensagem = dsl.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC003_DeveMostrarMensagemDeErroQuandoEmailPreenchidoESenhaVazia(){
        // Validar acesso sem informar a senha!!!

        dsl.executarAcaoDeLogar("teste", "");
        String mensagem = dsl.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC004_DeveMostrarMensagemDeErroQuandoEmailVazioESenhaIncorreta(){
        // Validar acesso sem informar o email!!!

        dsl.executarAcaoDeLogar("", "teste");
        String mensagem = dsl.obterMenssagem();

        assertEquals("Informe usuário e senha, os campos não podem ser brancos.", mensagem);
    }

    @Test
    public void TC005_ValidarEmailSenhaAmbosInvalidos(){
        // Validar acesso com email e senha inválidos!!!

        dsl.executarAcaoDeLogar("teste", "teste");
        String mensagem = dsl.obterMenssagem();

        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC006_ValidarEmailSenhaSenhaInvalido(){
        // Validar acesso com senha inválido!!!
    
        dsl.executarAcaoDeLogar("admin@admin.com", "teste");
        String mensagem = dsl.obterMenssagem();
    
        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC007_ValidarEmailSenhaEmailInvalido(){
        // Validar acesso com email inválido!!!

        dsl.executarAcaoDeLogar("Aadmin@admin.com", "admin@123");
        String mensagem = dsl.obterMenssagem();

        assertEquals("E-mail ou senha inválidos", mensagem);
    }

    @Test
    public void TC008_ValidarEmailSenhaAmbosValidos(){
        // Validar acesso com email e senha válidos!!!

        dsl.executarAcaoDeLogar("admin@admin.com", "admin");
        assertEquals(dsl.tituloInicial.getText(), "Controle de Produtos");
    }

    @Test
    public void TC009_abrirModalSalvarProduto(){
        dsl.buttonAdicionar.click();
        dsl.buttonAdicionar.click();
        String titulo = dsl.tituloModalh4.getText();
        assertEquals("Produto", titulo);
        dsl.buttonSair.click();
        dsl.buttonSair.click();
    }

    @Test
    public void TC010_naoDeveSerPossivelCadastrarProdutoSemPreencherOsCampos(){
        dsl.buttonAdicionar.click();
        dsl.buttonSalvar.click();
        String menssagemObrigatorio = dsl.returnMenssagem.getText();
        assertEquals("Todos os campos são obrigatórios para o cadastro!", menssagemObrigatorio);
        dsl.buttonSair.click();
    }

    @Test
    public void TC011_adicionarProduto(){
        dsl.buttonAdicionar.click();
        ProdutoBuilder produtoBuilder = new ProdutoBuilder(dsl);
        produtoBuilder
        .builder();

        produtoBuilder
        .adicionarCodigo(1)
        .adicionarNome("Produto Teste")
        .adicionarQuantidade(1)
        .adicionarValor(10.00)
        .adicionarData("09/04/2025")
        .builder();

        produtoBuilder
        .adicionarCodigo(111)
        .adicionarQuantidade(null)
        .builder();

        dsl.cadastrarProduto(produtoBuilder);
        dsl.buttonSair.click();
    }
}

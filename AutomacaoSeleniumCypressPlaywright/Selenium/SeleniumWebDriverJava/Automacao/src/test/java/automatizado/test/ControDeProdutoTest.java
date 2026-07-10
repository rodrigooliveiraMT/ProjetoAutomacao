package automatizado.test;

import static org.junit.Assert.assertEquals;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

import automatizado.builder.ProdutoBuilder;
import automatizado.page.ControleDeProdutoPO;
import automatizado.page.LoginPO;
import automatizado.resource.Cadastro_Produto_Url;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class ControDeProdutoTest extends BaseTest {
    
    public static LoginPO loginPage;
    public static ControleDeProdutoPO controleProdutoPage;
    public static Cadastro_Produto_Url cadastroProdutoUrl;

    @BeforeClass
    public static void prepararTestes(){
        loginPage = new LoginPO(driver);
        loginPage.executarAcaoDeLogar("admin@admin.com", "admin@123");
        controleProdutoPage = new ControleDeProdutoPO(driver);
        assertEquals(controleProdutoPage.obterTituloPagina(), "Controle de Produtos");
        driver.get(Cadastro_Produto_Url.URL_BASE);
    }

    @Test
    public void TC001_abrirModalSalvarProduto(){
        controleProdutoPage.buttonAdicionar.click();
        controleProdutoPage.buttonAdicionar.click();
        String titulo = controleProdutoPage.tituloModalh4.getText();
        assertEquals("Produto", titulo);
        controleProdutoPage.buttonSair.click();
        controleProdutoPage.buttonSair.click();
    }

    @Test
    public void TC002_naoDeveSerPossivelCadastrarProdutoSemPreencherOsCampos(){
        controleProdutoPage.buttonAdicionar.click();
        controleProdutoPage.buttonSalvar.click();
        String menssagemObrigatorio = controleProdutoPage.returnMenssagem.getText();
        assertEquals("Todos os campos são obrigatórios para o cadastro!", menssagemObrigatorio);
        controleProdutoPage.buttonSair.click();
    }

    @Test
    public void TC003_adicionarProduto(){
        controleProdutoPage.buttonAdicionar.click();
        ProdutoBuilder produtoBuilder = new ProdutoBuilder(controleProdutoPage);
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

        controleProdutoPage.cadastrarProduto(produtoBuilder);
        controleProdutoPage.buttonSair.click();
    }
}

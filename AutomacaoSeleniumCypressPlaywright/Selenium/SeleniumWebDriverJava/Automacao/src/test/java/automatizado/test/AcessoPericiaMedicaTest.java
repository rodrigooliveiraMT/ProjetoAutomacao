package automacaoSelenium.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;
import org.openqa.selenium.Alert;
import org.openqa.selenium.support.ui.Select;

import automacaoSelenium.page.AcessoPericiaMedicaPO;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class AcessoPericiaMedicaTest extends BaseTest {

    public static AcessoPericiaMedicaPO dsl;

    public static final String URL_BASE = "https://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx";

    @BeforeClass
    public static void inicializarPage() {
        dsl = new AcessoPericiaMedicaPO(driver);
        driver.get(URL_BASE);
    }

    @Test
    public void TC001_validarTituloPagina() {
        dsl.ObterTituloPagina("Pericia | Login");
    }

    @Test
    public void TC002_validarTituloLogin() {
        assertEquals("Perícia Médica", dsl.validarTituloLogin.getText());
    }

    @Test
    public void TC003_validarMensagemLogin() {
        dsl.botaoLogin.click();
        dsl.delay(dsl.tituloErro);
        dsl.delay(dsl.mensagemErro);
        dsl.systemResult(dsl.tituloErro.getText());
        dsl.systemResult(dsl.mensagemErro.getText());
    }

    @Test
    public void TC004_efetuarLogin() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.acessarModuloConfiguracoes);
        dsl.delayClick(dsl.acessarParametrosSistema);
        dsl.validarTexto(dsl.validarAbaParametros, "Parâmetros");
        dsl.systemResult(dsl.tituloTelaInicial.getText());
    }

    @Test
    public void TC005_cadastrarUsuarioOperadorPericiaMedica() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.ModuloCadastros);
        dsl.delayClick(dsl.MenuCadastroUsuarios);
        dsl.validarTexto(dsl.validarTelaCadastroUsuarios, "Usuários");
        dsl.delayClick(dsl.botaoNovoCadastroUsuario);
        // dsl.delayClick(dsl.clickAbaUsuarios);
        // dsl.validarTexto(dsl.clickAbaUsuarios, "Usuários");
        dsl.botaoSalvar.click();
        dsl.delay(dsl.validarObrigatorioCampoNome);
        dsl.inputCampoNomePerito.sendKeys("AUTOMAÇÃO");
        dsl.inputCampoLogin.sendKeys("AUTOMACAO");
        Select selectPerfil = new Select(dsl.selecionarGrupoPermissao);
        selectPerfil.selectByVisibleText("Automação");
        dsl.inputCampoHash.sendKeys("123");
        dsl.inputCampoHashConfirmacao.sendKeys("123");
        dsl.inputCampoCPF.sendKeys("79013823092");
        dsl.delayClick(dsl.botaoSalvar);
        dsl.delay(dsl.tituloSucesso);
        dsl.delay(dsl.mensagemSucesso);
        assertEquals("Atenção!", dsl.tituloSucesso.getText());
        assertEquals("Cadastro realizado com sucesso!", dsl.mensagemSucesso.getText());
        dsl.systemResult(dsl.tituloSucesso.getText());
        dsl.systemResult(dsl.mensagemSucesso.getText());
        dsl.inputCampoPesquisarUsuario.sendKeys("AUTOMAÇÃO");
        dsl.delay(dsl.linhaUsuario);
        assertTrue(dsl.linhaUsuario.getText().contains("AUTOMAÇÃO"));
        System.out.println("Cadastro de Usuário Operador Efetuado Com Sucesso!");
    }

    /**
     * Acessar Tela Grupo de Permissões
     */
    @Test
    public void TC006_validarMenuGrupoPermissoes() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.acessarModuloConfiguracoes);
        dsl.delayClick(dsl.acessarMenuGrupoPermissoes);
        dsl.validarTexto(dsl.validarTelaGrupoPermissoes, "Grupos - Permissões");
        dsl.delayClick(dsl.botaoNovoCadastroGrupoPermissao);
        dsl.delay(dsl.tituloModalGrupoPermissao);
        dsl.validarTexto(dsl.tituloModalGrupoPermissao, "Cadastro de Grupos de Permissão");
        dsl.botaoFecharGrupoPermissao.click();
        dsl.retornarTelaPrincial();
        dsl.delayClick(dsl.ModuloPericiasAgendadas);
        System.out.println("Acesso ao Menu Grupo de Permissões Validado Com Sucesso!");
    }

    /**
     * Criar Grupo Permissões
     */
    @Test
    public void TC007_cadastrarGrupoPermissoes() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.acessarModuloConfiguracoes);
        dsl.delayClick(dsl.acessarMenuGrupoPermissoes);
        dsl.validarTexto(dsl.validarTelaGrupoPermissoes, "Grupos - Permissões");
        dsl.delayClick(dsl.botaoNovoCadastroGrupoPermissao);
        dsl.delay(dsl.tituloModalGrupoPermissao);
        dsl.validarTexto(dsl.tituloModalGrupoPermissao, "Cadastro de Grupos de Permissão");
        dsl.inputCampoNomeGrupo.sendKeys("Automação");
        dsl.botaoSalvarGrupoPermissao.click();
        dsl.delay(dsl.tituloSucesso);
        dsl.delay(dsl.mensagemSucesso);
        assertEquals("Atenção!", dsl.tituloSucesso.getText());
        assertEquals("Grupo cadastrado com sucesso!", dsl.mensagemSucesso.getText());
        assertTrue(dsl.esperarSumirElemento(dsl.mensagemSucesso));
        dsl.delay(dsl.linhaGrupoPermissao);
        assertTrue(dsl.linhaGrupoPermissao.getText().contains("Automação"));
        dsl.delayClick(dsl.botaoEditarPermissao);
        dsl.delayClick(dsl.checkboxPermissao);
        dsl.botaoSalvarPermissoes.click();
        dsl.delay(dsl.tituloSucesso);
        dsl.delay(dsl.mensagemSucesso);
        assertEquals("Atenção!", dsl.tituloSucesso.getText());
        assertEquals("Cadastro atualizado com sucesso!", dsl.mensagemSucesso.getText());
        System.out.println("Cadastro de Grupo de Permissão Efetuado Com Sucesso!");
    }

    /**
     * Excluir Grupo de Permissões (Negação)
     */
    @Test
    public void TC008_excluirGrupoPermissoesNegar() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.acessarModuloConfiguracoes);
        dsl.delayClick(dsl.acessarMenuGrupoPermissoes);
        dsl.validarTexto(dsl.validarTelaGrupoPermissoes, "Grupos - Permissões");
        dsl.delay(dsl.linhaGrupoPermissao);
        assertTrue(dsl.linhaGrupoPermissao.getText().contains("Automação"));
        dsl.delayClick(dsl.botaoExcluirPermissao);
        Alert alert = driver.switchTo().alert();
        String alerta = alert.getText();
        assertEquals("Deseja Mesmo Confirmar Está Operação?", alerta);
        alert.dismiss();
        dsl.delay(dsl.linhaGrupoPermissao);
        assertTrue(dsl.linhaGrupoPermissao.getText().contains("Automação"));
        System.out.println("Cadastro de Grupo de Permissão Não Excluído!");
    }

    /**
     * Excluir Grupo de Permissões (Aceitação)
     */
    @Test
    public void TC008_excluirGrupoPermissoesAceitar() {
        dsl.efeturarLogin();
        dsl.delay(dsl.tituloTelaInicial);
        dsl.validarTexto(dsl.tituloTelaInicial, "Perícia Médica");
        dsl.delayClick(dsl.acessarModuloConfiguracoes);
        dsl.delayClick(dsl.acessarMenuGrupoPermissoes);
        dsl.validarTexto(dsl.validarTelaGrupoPermissoes, "Grupos - Permissões");
        dsl.delay(dsl.linhaGrupoPermissao);
        assertTrue(dsl.linhaGrupoPermissao.getText().contains("Automação"));
        dsl.delayClick(dsl.botaoExcluirPermissao);
        Alert alert = driver.switchTo().alert();
        String alerta = alert.getText();
        assertEquals("Deseja Mesmo Confirmar Está Operação?", alerta);
        alert.accept();
        dsl.delay(dsl.tituloSucesso);
        dsl.delay(dsl.mensagemSucesso);
        assertEquals("Atenção!", dsl.tituloSucesso.getText());
        assertEquals("Exclusão realizada com sucesso!", dsl.mensagemSucesso.getText());
        System.out.println("Cadastro de Grupo de Permissão Excluído Com Sucesso!");
    }
}

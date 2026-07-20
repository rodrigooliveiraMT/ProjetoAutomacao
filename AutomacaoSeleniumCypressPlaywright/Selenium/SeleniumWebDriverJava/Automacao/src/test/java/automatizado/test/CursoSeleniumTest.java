package automatizado.test;

import java.util.List;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;
import org.openqa.selenium.Alert;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

import automatizado.page.CursoSeleniumPO;
import automatizado.resource.CursoSeleniumUrl;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class CursoSeleniumTest extends BaseTest {

    public static CursoSeleniumPO dsl;

    @BeforeClass
    public static void abrirPagina(){
        dsl = new CursoSeleniumPO(driver);
        driver.get(CursoSeleniumUrl.URL_BASE);
    }

    @Test
    public void TC001_validarTitulo(){
       dsl.ObterTituloPagina("Campo de Treinamento");
    }

    @Test
    public void TC002_preencherCampoNome(){
        dsl.validarElemento(dsl.inputNome);
        dsl.escrever(dsl.inputNome, "Rodrigo");
    }

    @Test
    public void TC003_preencherCampoSobreNome(){
        dsl.validarElemento(dsl.inputSobreNome);
        dsl.escrever(dsl.inputSobreNome, "De Oliveira Costa");
    }

    @Test
    public void TC004_selecionarSexoMasculino(){
        dsl.validarElemento(dsl.radioButtonMasculino);
        dsl.radioButtonMasculino.click();
        Assert.assertTrue(dsl.radioButtonMasculino.isSelected());
    }

    @Test
    public void TC005_selecionarComidaFavoritaCarne(){
        dsl.validarElemento(dsl.radioButtonComida);
        dsl.radioButtonComida.click();
        Assert.assertTrue(dsl.radioButtonComida.isSelected());
    }

    @Test
    public void TC006_selecionarEscolaridadeSuperior(){
        dsl.validarElemento(dsl.selecioneEscolaridade);
        Select escolaridade = new Select(dsl.selecioneEscolaridade);
        escolaridade.selectByVisibleText("Superior");
        String resultado = escolaridade.getFirstSelectedOption().getText();
        Assert.assertEquals("Superior", resultado);
    }

    @Test
    public void TC007_selecionarEsportes(){
        dsl.validarElemento(dsl.selecioneEsportes);
        Select esportes = new Select(dsl.selecioneEsportes);
        esportes.selectByVisibleText("Natacao");
        esportes.selectByVisibleText("Futebol");
        esportes.selectByVisibleText("Corrida");
        List<WebElement> selecionados = esportes.getAllSelectedOptions();
        Assert.assertEquals(3, selecionados.size());
        Assert.assertEquals("Natacao", selecionados.get(0).getText());
        Assert.assertEquals("Futebol", selecionados.get(1).getText());
        Assert.assertEquals("Corrida", selecionados.get(2).getText());
    }

    @Test
    public void TC008_preencherCampoSugestoes(){
        dsl.validarElemento(dsl.inputSugestoes);
        dsl.escrever(dsl.inputSugestoes, "Teste 01\nTeste 02\nTeste 03");
    }

    @Test
    public void TC009_validarLinkVoltar(){
        dsl.validarElemento(dsl.linkVoltar);
        dsl.linkVoltar.click();
        Assert.assertEquals("Voltou!", dsl.resultadoLinkVoltar.getText());
    }

    @Test
    public void TC010_validarAlert(){
        dsl.validarElemento(dsl.alerta);
        dsl.alerta.click();
        Alert alert = driver.switchTo().alert();
        Assert.assertEquals("Alert Simples", alert.getText());
        alert.accept();
    }

    @Test
    public void TC011_validarConfirmarAceitar(){
        dsl.validarElemento(dsl.confirmar);
        dsl.confirmar.click();
        Alert alertaConfirmar = driver.switchTo().alert();
        Assert.assertEquals("Confirm Simples", alertaConfirmar.getText());
        alertaConfirmar.accept();
        Alert alertaResultado = driver.switchTo().alert();
        Assert.assertEquals("Confirmado", alertaResultado.getText());
        alertaResultado.accept();
    }

    @Test
    public void TC012_validarConfirmarNegar(){
        dsl.validarElemento(dsl.confirmar);
        dsl.confirmar.click();
        Alert alertaConfirmar = driver.switchTo().alert();
        Assert.assertEquals("Confirm Simples", alertaConfirmar.getText());
        alertaConfirmar.dismiss();
        Alert alertaResultado = driver.switchTo().alert();
        Assert.assertEquals("Negado", alertaResultado.getText());
        alertaResultado.accept();
    }

    @Test
    public void TC013_validarPrompt(){
        dsl.validarElemento(dsl.prompt);
        dsl.prompt.click();
        Alert alertaPrompt = driver.switchTo().alert();
        Assert.assertEquals("Digite um numero", alertaPrompt.getText());
        String numero = "2";
        alertaPrompt.sendKeys(numero);
        alertaPrompt.accept();
        dsl.esperarAlert();
        Alert resultadoPrompt = driver.switchTo().alert();
        Assert.assertEquals("Era " +numero+ "?", resultadoPrompt.getText());
        resultadoPrompt.accept();
        dsl.esperarAlert();
        Alert resultadoPromptFinal = driver.switchTo().alert();
        Assert.assertEquals(":D", resultadoPromptFinal.getText());
        resultadoPromptFinal.accept();
    }

    @Test
    public void TC014_validarButtonClique(){
        dsl.validarElemento(dsl.buttonCliqueMe);
        dsl.buttonCliqueMe.click();
        Assert.assertEquals("Obrigado!", dsl.buttonCliqueMe.getAttribute("value"));
    }

    @Test
    public void TC015_validarPopupComIdentificao(){
        dsl.validarElemento(dsl.abrirPopupComIdentificao);
        dsl.abrirPopupComIdentificao.click();
        driver.switchTo().window("Popup");
        dsl.escrever(dsl.inputTextarea, "Olá");
        driver.close();
        driver.switchTo().window("");
    }

    @Test
    public void TC016_validarPopupSemIdentificao(){
        dsl.validarElemento(dsl.abrirPopupSemIdentificao);
        dsl.abrirPopupSemIdentificao.click();
        driver.switchTo().window((String) driver.getWindowHandles().toArray()[1]);
        dsl.escrever(dsl.inputTextarea, "Olá");
        driver.close();
        driver.switchTo().window((String) driver.getWindowHandles().toArray()[0]);
    }

    @Test
    public void TC017_validarCampoComDalay(){
        dsl.validarElemento(dsl.inputComDalay);
        dsl.inputComDalay.click();
        dsl.esperarInput(dsl.inputCampoNovo);
        dsl.validarElemento(dsl.inputCampoNovo);
        dsl.escrever(dsl.inputCampoNovo, "Olá");
    }

    @Test
    public void TC018_validarFrame(){
        dsl.validarElemento(dsl.validarFrame);
        driver.switchTo().frame(dsl.validarFrame);
        dsl.buttonFrame.click();
        dsl.esperarAlert();
        Alert alertaFrame = driver.switchTo().alert();
        Assert.assertEquals("Frame OK!", alertaFrame.getText());
        alertaFrame.accept();
        driver.switchTo().defaultContent();
    }

    @Test
    public void TC019_criarCadastro(){
        driver.navigate().refresh();
        
        dsl.inputNome.sendKeys("RODRIGO");
        dsl.inputSobreNome.sendKeys("DE OLIVEIRA");
        dsl.radioButtonMasculino.click();
        dsl.radioButtonComida.click();
        Select escolaridade = new Select(dsl.selecioneEscolaridade);
        escolaridade.selectByVisibleText("Superior");
        Select esportes = new Select(dsl.selecioneEsportes);
        esportes.selectByVisibleText("Natacao");
        esportes.selectByVisibleText("Futebol");
        esportes.selectByVisibleText("Corrida");
        dsl.inputSugestoes.sendKeys("Teste 01\nTeste 02\nTeste 03");

        dsl.buttonCadastrar.click();

        Assert.assertEquals("Cadastrado!", dsl.resultadoDoCadastro.getText());
        Assert.assertTrue(dsl.resultadoNome.getText().endsWith("RODRIGO"));
        Assert.assertTrue(dsl.resultadoSobreNome.getText().endsWith("DE OLIVEIRA"));
        Assert.assertTrue(dsl.resultadoSexo.getText().endsWith("Masculino"));
        Assert.assertTrue(dsl.resultadoComida.getText().endsWith("Carne"));
        Assert.assertTrue(dsl.resultadoEscolaridade.getText().endsWith("superior"));
        Assert.assertTrue(dsl.resultadoEsportes.getText().endsWith("Natacao Futebol Corrida"));
        Assert.assertTrue(dsl.resultadoSugestoes.getText().endsWith("Teste 01 Teste 02 Teste 03"));
    }

}
